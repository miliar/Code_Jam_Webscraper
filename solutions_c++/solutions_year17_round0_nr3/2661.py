#include "bits/stdc++.h"
#define MAXN 100009
#define INF 1000000007
#define mp(x,y) make_pair(x,y)
#define all(v) v.begin(),v.end()
#define pb(x) push_back(x)
#define wr cout<<"----------------"<<endl;
#define ppb() pop_back()
#define tr(ii,c) for(typeof((c).begin()) ii=(c).begin();ii!=(c).end();ii++)
#define ff first
#define ss second
#define my_little_dodge 46
using namespace std;

typedef long long ll;
typedef pair<int,int> PII;
template<class T>bool umin(T& a,T b){if(a>b){a=b;return 1;}return 0;}
template<class T>bool umax(T& a,T b){if(a<b){a=b;return 1;}return 0;}
map<ll,ll>cnt;
priority_queue<ll>q;
int main(){
    freopen("file.in", "r", stdin);
    freopen("file.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int test=1;test<=t;test++){
		ll n,k;
		scanf("%lld%lld",&n,&k);
		q.push(n);cnt[n]=1;
		while(1){
			ll x=q.top();
			q.pop();
			if(cnt[x]>=k){
				if(x&1)
					printf("Case #%d: %lld %lld\n",test,x/2,x/2);
				else
					printf("Case #%d: %lld %lld\n",test,x/2,x/2-1);
				break;
			}
			k-=cnt[x];
			if(x&1){
				if(!cnt[x/2]){
					q.push(x/2);
					cnt[x/2]=cnt[x]*2;
				}
				else
					cnt[x/2]+=cnt[x]*2;
			}
			else{
				if(!cnt[x/2]){
					q.push(x/2);
					cnt[x/2]=cnt[x];
				}
				else
					cnt[x/2]+=cnt[x];
				if(!cnt[x/2-1]){
					q.push(x/2-1);
					cnt[x/2-1]=cnt[x];
				}	
				else
					cnt[x/2-1]+=cnt[x];
			}
			cnt[x]=0;
		}
		while(!q.empty())
			q.pop();
		cnt.clear();	
	}
	return 0;
}
