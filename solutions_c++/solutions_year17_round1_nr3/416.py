#include<bits/stdc++.h>
using namespace std;

int hd,ad,hk,ak,b,d;

int func(int buf,int debuf){
  int HD=hd;
  int AD=ad;
  int HK=hk;
  int AK=ak;

  int last=-1;
  
  int res=0;
  while(1){
    res++;
    if(HK-AD<=0)break;

    int nak=max(0,AK-d);
    if(HD-nak>0 && debuf>0){
      AK=nak;
      HD-=nak;
      debuf--;
      continue;
    }

    if(HD-AK<=0){
      HD=hd-AK;

      if(last!=-1 && last==res-1)return 1e9;
      last=res;
      continue;
    }

    if(buf>0){
      HD-=AK;
      AD+=b;
      buf--;
    }else{
      HD-=AK;
      HK-=AD;
    }
  }
  return res;
}

int main(){
  int Tc;
  cin>>Tc;
  for(int tc=1;tc<=Tc;tc++){
    cin>>hd>>ad>>hk>>ak>>b>>d;

    int I,J;
    int ans=1e9;
    for(int i=0;i<=100;i++)
      for(int j=0;j<=100;j++){
        int pp;
        pp=func(i,j);
        if( ans > pp ){
          ans=pp;
          I=i;
          J=j;
        }

      }
    

    cout<<"Case #"<<tc<<": ";
    if(ans==1e9)cout<<"IMPOSSIBLE"<<endl;
    else cout<<ans<<endl;
  }
  return 0;
}
