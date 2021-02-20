%module TCPSHM_CLIENT
%include"std_string.i"
%include"stl.i"
%{
#include"tcpshm_client.h"
%}

%include"mmap.h"
%include"tcpshm_conn.h"
%include"tcpshm_client.h"
