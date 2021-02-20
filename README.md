# TCPSHM_interface_python

本项目基于C++项目https://github.com/MengRao/tcpshm ，将共享消息队列的C++接口采用SWIG封装为python接口，实现客户端和服务端之间的消息传输接口。用户可以使用接口完成下游项目需求。

构建方法如下：

    1. 安装swig3.0以上版本，命令行输入swig --version查看版本号
  
    2. 命令行输入 swig -c++ -python -py3 TCPSHM_CLIENT.i
  
    3. 命令行输入  g++ -shared -std=c++11 -fPIC -I/usr/include/python3.5m -lpython3.5m  TCPSHM_CLIENT_wrap.cxx -o _TCPSHM_CLIENT.so -fpermissive -lrt -lpthread
  
    4. 运行mian.py文件测试发送数据结果



项目说明：

    1.此项目只为客户端，服务器端请自行运行原C++项目
 
    2.此项目目前只支持使用共享队列模式，传统TCP模式不支持
  
    3.为了方便交互，对原C++代码做了修改。去除了原项目中的模板以及派生操作，将echo_clent.cc中的若干函数直接实现在了其父类中。以及进行了其他为了适应python语言与C++交互的改动。

    4.为保证python传输的数据能被C++端的接受并发送，新的数据类型结构应该在C++中定义对应的类，tcpshm_client.h中的User_Data类。
