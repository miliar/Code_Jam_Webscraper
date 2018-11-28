#include<bits/stdc++.h>
using namespace std;
#define int long long
typedef tuple<int,int,int,int> P;
signed main(){
  int T;
  cin>>T;
  for(int t=1;t<=T;t++){
    cout<<"Case #"<<t<<": ";
    int hd,ad,hk,ak,b,d;
    cin>>hd>>ad>>hk>>ak>>b>>d;
    int ans=-1;
    queue<P> q;
    q.emplace(hd,ad,hk,ak);
    map<P,int> m;
    m[make_tuple(hd,ad,hk,ak)]=0;
    while(!q.empty()){
      P p=q.front();q.pop();
      int a[4];
      {
	a[0]=get<0>(p);a[1]=get<1>(p);
	a[2]=get<2>(p);a[3]=get<3>(p);
	a[2]-=a[1];
	if(a[2]<=0){
	  ans=m[p]+1;
	  break;
	}
	a[0]-=a[3];
	if(a[0]>0&&!m.count(make_tuple(a[0],a[1],a[2],a[3]))){
	  m[make_tuple(a[0],a[1],a[2],a[3])]=m[p]+1;
	  q.emplace(a[0],a[1],a[2],a[3]);
	}
      }
      {
	a[0]=get<0>(p);a[1]=get<1>(p);
	a[2]=get<2>(p);a[3]=get<3>(p);
	a[1]+=b;
	a[0]-=a[3];
	if(a[0]>0&&!m.count(make_tuple(a[0],a[1],a[2],a[3]))){
	  m[make_tuple(a[0],a[1],a[2],a[3])]=m[p]+1;
	  q.emplace(a[0],a[1],a[2],a[3]);
	}
      }
      {
	a[0]=get<0>(p);a[1]=get<1>(p);
	a[2]=get<2>(p);a[3]=get<3>(p);
	a[0]=hd;
	a[0]-=a[3];
	if(a[0]>0&&!m.count(make_tuple(a[0],a[1],a[2],a[3]))){
	  m[make_tuple(a[0],a[1],a[2],a[3])]=m[p]+1;
	  q.emplace(a[0],a[1],a[2],a[3]);
	}
      }
      {
	a[0]=get<0>(p);a[1]=get<1>(p);
	a[2]=get<2>(p);a[3]=get<3>(p);
	a[3]-=d;
	if(a[3]<0) a[3]=0;
	a[0]-=a[3];
	if(a[0]>0&&!m.count(make_tuple(a[0],a[1],a[2],a[3]))){
	  m[make_tuple(a[0],a[1],a[2],a[3])]=m[p]+1;
	  q.emplace(a[0],a[1],a[2],a[3]);
	}
      }
    }
    if(ans<0) cout<<"IMPOSSIBLE"<<endl;
    else cout<<ans<<endl;
  }
  return 0;
}
