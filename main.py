import TCPSHM_CLIENT

def onsServerMsg(data):

    # 将从服务器接收到的数据做处理
    print('onsServerMsg: %d  %f'%(data.name,data.accurate))
    return True



def run(use_shm,server_ipv4,server_port):
    if Client.Connect(use_shm,server_ipv4,server_port,0)==False:
        return
    conn=Client.GetConnection()
    i=0
    if use_shm==True:
        while conn.IsClosed()==False:               #若连接不关闭则一直循环
            if i==100:                              #传输100个数据包
                break
            Client.Push_User_Data(data)             #数据放入队列
            print('i:%d'%(i))
            i+=1
            get_data=Client.PollShm()               #从队列中取出数据
            if onsServerMsg(get_data)==True:
                conn.Pop()



if __name__ == '__main__':

    #设置传输数据内容
    data = TCPSHM_CLIENT.User_Data()
    data.name = 99
    data.accurate = 1.245

    #设定传输参数
    ptcp_dir='client'
    name='client'
    use_shm=True
    server_port=12345
    server_ipv4='127.0.0.1'

    #实例化TCPSHM类 并启动连接
    Client=TCPSHM_CLIENT.TcpShmClient(ptcp_dir,name)
    run(use_shm,server_ipv4,server_port)



