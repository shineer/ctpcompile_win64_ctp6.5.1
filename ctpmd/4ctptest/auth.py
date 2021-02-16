# -*- coding: utf-8 -*-
import win64.thostmduserapi as mdapi  

class CFtdcMdSpi(mdapi.CThostFtdcMdSpi):
    tapi=''
    def __init__(self,tapi):
        mdapi.CThostFtdcMdSpi.__init__(self)
        self.tapi=tapi
    def OnFrontConnected(self):
        print ("OnFrontConnected")
        loginfield = mdapi.CThostFtdcReqUserLoginField()
        loginfield.BrokerID="9999"
        loginfield.UserID="123456"
        loginfield.Password="123456"
        loginfield.UserProductInfo="python dll"
        self.tapi.ReqUserLogin(loginfield,0)
    def OnRspUserLogin(self, *args):
        print ("OnRspUserLogin")
        rsploginfield=args[0]
        rspinfofield=args[1]
        print ("SessionID=",rsploginfield.SessionID)
        print ("ErrorID=",rspinfofield.ErrorID)
        print ("ErrorMsg=",rspinfofield.ErrorMsg)
        ret=self.tapi.SubscribeMarketData([b"ru2105",b"rb2105"],2)

    def OnRtnDepthMarketData(self, *args):
        print ("OnRtnDepthMarketData")
        field=args[0]
        print ("OnRtnDepthMarketData InstrumentID=",field.InstrumentID)
        print ("OnRtnDepthMarketData LastPrice=",field.LastPrice)

    def OnRspSubMarketData(self, *args):
        print ("OnRspSubMarketData")
        field=args[0]
        print ("InstrumentID=",field.InstrumentID)
        rspinfofield=args[1]
        print ("ErrorID=",rspinfofield.ErrorID)
        print ("ErrorMsg=",rspinfofield.ErrorMsg)

def main():
    mduserapi=mdapi.CThostFtdcMdApi_CreateFtdcMdApi()
    mduserspi=CFtdcMdSpi(mduserapi) 
    # 全天
    mduserapi.RegisterFront("tcp://180.168.146.187:10131")
    # 
    # mduserapi.RegisterFront("tcp://180.168.146.187:10111")
    mduserapi.RegisterSpi(mduserspi)
    mduserapi.Init()    
    mduserapi.Join()

if __name__ == '__main__':
    main()