# TradeAPi vs2019 + ctp6.5.1 #
# 1 下载交易所api 6.5.1 #
# 2 swig 编译 内容在.i 里面 #
其中包括字符转换
当前目录下运行cmd:

    swig -threads -py3 -c++ -python thosttraderapi.i
生成_wrap.h  
*_wrap.cxx  
thosttradeapi.py
# 3 建立C++工程 #
	应用类型选择DLL 工程名称为  _thosttraderapi
	工程建立64位的，运行库选多线程/MT
	将文件拷贝到_thosttraderapi\文件夹下
	ThostFtdcTraderApi.h
	ThostFtdcUserApiDataType.h
	ThostFtdcUserApiStruct.h
	thosttraderapi.lib
	thosttraderapi_wrap.cxx
	thosttraderapi_wrap.h

添加现有项 6个文件
然后 
	1 将python  头文件 在 include里 包含进来（可以创建虚拟环境包含进来） 
    2 将python.libs静态库文件夹包含进来
    3 添加静态库

编译 64位 release版本
# 4 测试 #

	注意：会有strcpy不安全的问题，用预编译忽略解决
	会有不包含pch.h让thosttraderapi_wrap.cxx include这个文件
	一定要下对应的visualstudio 因为环境就是从那里来的
	下载visual studio C++空项目，就不会出现找不到dll的问题
	strcpy不安全的解决办法
	解决方法：项目属性->配置属性->C/C+±>预处理器->预处理器定义中添加：_CRT_SECURE_NO_WARNINGS

# MDAPI #
	mdapi中需要修改二级指针的转换
    2类似 第二步开始把所有的tradeapi改成mdapi
	swig -threads -c++ -python thostmduserapi.i
	
	

