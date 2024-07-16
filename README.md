
# orne-box
このレポジトリではorne-boxをros2 humbleで動作させることができます

### about orne-box
Platform hardware for autonomous robot

* [Purpose](https://github.com/open-rdc/orne_box/wiki/Initial-Purpose)
* [Design Data (Under Constructing)](https://drive.google.com/drive/folders/1FTzKjHyfmug_UDPVUtk7wh9Z_zvEPqiV?usp=sharing)
* This project is derived from [orne_navigation](https://github.com/open-rdc/orne_navigation)  

## Install
installはそれぞれのREADMEにしたがってください
1. orne-box
```
git clone https://github.com/TakumiIshiguro/orne-box.git -b humble-urg
```
rosdepで依存パッケージをインストールします
```
rosdep install --from-paths . --ignore-src --rosdistro $ROS_DISTRO -y
```
2. emcl2_ros2  
https://github.com/CIT-Autonomous-Robot-Lab/emcl2_ros2
3. ypspur  
https://github.com/openspur/yp-spur/blob/master/doc/README.ja.md
4. urg_node2  
https://github.com/Hokuyo-aut/urg_node2
5. waypoint_manager2  
```
git clone https://github.com/TakumiIshiguro/waypoint_manager2.git -b tsukuba2023
```  
## Excecution
#### Change map
```
/orne-box/orne_box_navigation_executor/launch/navigation2.launch.py
```
```  
/orne-box/orne_box_navigation_executor/launch/costmap_filter_info.launch.py
```  
内のファイルパスを変更してください
#### Change waypoint
```
/waypoint_manager2/waypoint_manager2/waypoint_manager2_node.py
```  
内のファイルパスを変更してください  

### On simulator
```
ros2 launch orne_box_simulation box_cit3f.launch.py
```
```
ros2 launch orne_box_navigation_executor navigation2.launch.py
```  

### On real robot
#### connect to sensors
rulesをコピーする(最初に一回実行すればOK)
```
ros2 run orne_box_setup create_udev_rules
```
動作確認
```
ls /dev/sensors
```
このコマンドを実行すると，icart-miniや，hokuyo_Hxxxxxxx等のデバイスが認識されていることがわかるはずです． 何も表示されない（デバイスが認識されていない）場合，USBケーブルが接続されているか，電源が入っているか等を確認してください．  
#### navigation
```
ros2 launch orne_box_bringup orne_box_drive.launch.py
```
```
ros2 launch orne_box_bringup description.launch.py
```
```
ros2 launch orne_box_bringup urg_node2.launch.py
```
```
ros2 launch orne_box_navigation_executor costmap_filter_info.launch.py
```
```
ros2 launch orne_box_navigation_executor navigation2.launch.py
```
```
ros2 run waypoint_manager2 waypoint_manager2_node
```  

# Hardware
![image](https://user-images.githubusercontent.com/5755200/76318342-eb89c780-6320-11ea-900b-02a052fb53ae.png)

![DSC_0245](https://user-images.githubusercontent.com/5755200/80554308-b0923f00-8a07-11ea-80c8-d2e2097a1d2a.jpg)

# Reference
* [orne-x](https://drive.google.com/drive/folders/1ViINGsmbruIFg-iK9aN-tVQHTLGuMvhR?usp=sharing) (designed in 2017)  

# Movie  
https://youtu.be/aYNsxiJAdHo  

# To Do
・シミュレーターのバグ修正
・installを簡略化(wstool)  
・起動に必要なlaunchを削減  



