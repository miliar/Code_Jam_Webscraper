#include<bits/stdc++.h>
using namespace std;
#define REP(i,a,b)for(int i=(a),i##_end_=(b);i<i##_end_;++i)
#define PER(i,a,b)for(int i=(b)-1,i##_end_=(a);i>=i##_end_;--i)
#define pb push_back
#define fi first
#define se second
template<class T>inline bool umx(T& A,const T& B){return A<B?A=B,1:0;}
template<class T>inline bool umn(T& A,const T& B){return A>B?A=B,1:0;}
typedef long long LL;
typedef double db;
typedef pair<int,int> PII;
typedef pair<db,int> PDI;

const int INF=0x3f3f3f3f;
const int maxn=110;
const int maxm=60;

void solve(){
	int _hd,_ad,_hk,_ak,_b,_d;
	scanf("%d%d%d%d%d%d",&_hd,&_ad,&_hk,&_ak,&_b,&_d);
	int u_debuff=(_d==0 ? 0 : (_ak+_d-1)/_d);
	int u_buff=(_b==0 ? 0 : (_hk+_b-1)/_b);
	int res=INF;
	REP(i,0,u_debuff+1)REP(j,0,u_buff+1){
		int hd=_hd,ad=_ad,hk=_hk,ak=_ak,b=_b,d=_d;
		int debuff=i,buff=j,t=0,t_hd=0;
		while(hd){
			++t;
			if(debuff){
				if(max(0,hd-max(0,ak-d))==0){
					hd=_hd;
					++t_hd;
				}else{
					--debuff;
					ak=max(0,ak-d);
				}
			}else if(buff){
				if(max(0,hd-ak)==0){
					hd=_hd;
					++t_hd;
				}else{
					--buff;
					ad+=b;
				}
			}else{
				if(max(0,hk-ad)>0 && max(0,hd-ak)==0){
					hd=_hd;
					++t_hd;
				}else{
					hk=max(0,hk-ad);
				}
			}
			if(hk==0)break;
			if(t_hd>300)break;
			hd=max(0,hd-ak);
		}
		if(t_hd<=300&&hd){
			umn(res,t);
		}
	}
	if(res==INF)puts("IMPOSSIBLE");
	else printf("%d\n",res);
}

int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int _,__=0;scanf("%d",&_);
	while(_--){
		printf("Case #%d: ",++__);
		solve();
	}
	return 0;
}
