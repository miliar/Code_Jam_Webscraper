#include<bits/stdc++.h>
using namespace std;
#define pb push_back
#define sz(x) ((int)x.size())
#define clr(a,b) memset(a,b,sizeof(a))
typedef long long ll;
const int maxn=1e3+7;
const int INF=1e9+7;
int m,T;
ll n,k;
struct node{
	ll l,r,cnt;
	node(){}
	node(ll a,ll b,ll c):l(a),r(b),cnt(c){}
	bool operator < (const node &x)const{
		int l1=r-l+1,l2=x.r-x.l+1;
		return l1<l2;
	}
};
void solve(){
	priority_queue<node> q;
	q.push(node(1,n,k));
	int AS=0;
	ll ans1,ans2;
	while(!q.empty()){
		node cur=q.top();q.pop();
		ll len=(cur.r-cur.l+1);
		ll mid=cur.l+(cur.r-cur.l)/2;
		cur.cnt--;
//			cout<<cur.l<<" "<<mid<<" "<<cur.r<<endl;
			ll res=cur.r-cur.l;
			ll lq=res/2;
			ll rq=res-lq;
			ans1=max(lq,rq);
			ans2=min(lq,rq);
		if(len&1){
			ll rcnt=cur.cnt/2;
			ll lcnt=cur.cnt-rcnt;
			if(lcnt>=rcnt){
				if(lcnt>0)q.push(node(cur.l,mid-1,lcnt));
			}else{
				if(rcnt>0)q.push(node(mid+1,cur.r,rcnt));
			}
		}else{
			ll lcnt=cur.cnt/2;
			ll rcnt=cur.cnt-lcnt;
			if(lcnt==rcnt){
				if(lcnt>0)q.push(node(cur.l,mid-1,lcnt));
			}else{
				if(rcnt>0)q.push(node(mid+1,cur.r,rcnt));
			}
		}
	}
	printf("%lld %lld\n",ans1,ans2);
}

int main(){
#ifdef AC
freopen("data.in","r",stdin);
freopen("data.out","w",stdout);
#endif
	cin>>T;
	for(int tc=1;tc<=T;tc++){
		printf("Case #%d: ",tc);
		cin>>n>>k;
		solve();
	}
	return 0;
}

