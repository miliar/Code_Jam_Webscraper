#include<vector>
#include<cmath>
#include<map>
#include<cstdlib>
#include<iostream>
#include<sstream>
#include<fstream>
#include<string>
#include<algorithm>
#include<cstring>
#include<cstdio>
#include<set>
#include<stack>
#include<bitset>
#include<functional>
#include<ctime>
#include<queue>
#include<deque>
#include<complex>
#include<cassert>
using namespace std;
#define pb push_back
#define pf push_front
typedef long long lint;
typedef complex<double> P;
#define mp make_pair
#define fi first
#define se second
typedef pair<int,int> pint;
#define All(s) s.begin(),s.end()
#define rAll(s) s.rbegin(),s.rend()
#define REP(i,a,b) for(int i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)
int inf=1919;
int ca(int hd,int ak,int d,int x,int at){
	int np=hd,i;
	for(i=0;i<inf+5;i++){
		//cout<<at<<' '<<np<<endl;
		if(x>0){
			if(np<=ak-d) np=hd-ak;
			else{
				ak-=d;np-=ak;x--;
			}
		}
		else if(at>0){
			if(np<=ak && at>1) np=hd-ak;
			else{
				at--;np-=ak;
			}
		}
		else return i;
	}
	return inf;
}
int cal(){
	int hd,ad,hk,ak,b,d,ret=inf+5;
	int miatk=114;
	cin>>hd>>ad>>hk>>ak>>b>>d;
	rep(i,103){
		int at=ad+b*i;
		miatk=min(miatk,i+(hk+at-1)/at);
	}
	//cout<<miatk<<endl;
	rep(i,103){
		if(d<1 && i>0) continue;
		ret=min(ret,ca(hd,ak,d,i,miatk));
	}
	return ret;
}
int main()
{
	int t;
	cin>>t;
	rep(i,t){
		int ret=cal();
		printf("Case #%d: ",i+1);
		if(ret<inf) cout<<ret<<endl;else cout<<"IMPOSSIBLE"<<endl;
	}
}
