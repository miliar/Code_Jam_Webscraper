#include<bits/stdc++.h>
#define F first
#define S second
using namespace std;
typedef pair<int,string> P;

int main(){
  
  int T;
  cin>>T;

  for(int t=1;t<=T;t++){

    int n,r,o,y,g,b,v;

    cin>>n>>r>>o>>y>>g>>b>>v;
    
    P d[3];
    
    d[0]=P(r,"R");
    d[1]=P(y,"Y");
    d[2]=P(b,"B");

    sort(d,d+3,greater<P>() );
    
    string ans;
    if(d[0].F>d[1].F+d[2].F){
      ans="IMPOSSIBLE";
    }else{
      
      while(d[1].F){
	ans+=d[0].S+d[1].S;
	d[0].F--; d[1].F--;
      }

      while(min(d[0].F,d[2].F)){
	ans+=d[0].S+d[2].S;
	d[0].F--; d[2].F--;
      }

      string tmp;
      int idx=0;
      while(d[2].F){
	tmp+=ans[idx++]+d[2].S;
	d[2].F--;
      }
      
      for(int i=idx;i<ans.size();i++)
	tmp+=ans[i];

      ans=tmp;
    }

    cout<<"Case #"<<t<<": "<<ans<<endl;
  }
  
  return 0;
}
