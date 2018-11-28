#include "bits/stdc++.h"
#define MAXN 100009
#define INF 1000000007
#define mp(x,y) make_pair(x,y)
#define all(v) v.begin(),v.end()
#define pb(x) push_back(x)
#define wr cout<<"----------------"<<endl;
#define ppb() pop_back()
#define tr(ii,c) for(__typeof((c).begin()) ii=(c).begin();ii!=(c).end();ii++)
#define ff first
#define ss second
#define my_little_dodge 46
using namespace std;

typedef long long ll;
typedef pair<int,int> PII;
template<class T>bool umin(T& a,T b){if(a>b){a=b;return 1;}return 0;}
template<class T>bool umax(T& a,T b){if(a<b){a=b;return 1;}return 0;}
int cnt[4];
int main(){
    freopen("file.in", "r", stdin);
    freopen("file.out", "w", stdout);
    int t;
    scanf("%d",&t);
    for(int test=1;test<=t;test++){
		memset(cnt,0,sizeof cnt);
		int n,p;
		scanf("%d%d",&n,&p);
		for(int i=1;i<=n;i++){
			int x;
			scanf("%d",&x);
			cnt[x%p]++;
		}
		int ans=cnt[0];
		if(p==2){
			if(cnt[1])
				ans++;
			int tot=0;
			for(int i=1;i<cnt[1];i++){
				tot=(tot+1)%p;
				ans+=(!tot);
			}
		}
		if(p==3){
			if(cnt[1] or cnt[2])
				ans++;
			int res0=0,res1=0;
			int tot=0,tmp1=cnt[1],tmp2=cnt[2];
			for(int i=1;i<n-cnt[0];i++){
				if(i&1){
					if(cnt[1])
						tot=(tot+1)%p,cnt[1]--;
					else
						tot=(tot+2)%p,cnt[2]--;
				}
				else{
					if(cnt[2])
						tot=(tot+2)%p,cnt[2]--;
					else
						tot=(tot+1)%p,cnt[1]--;
				}
				res0+=(!tot);
			}tot=0;
			cnt[1]=tmp1;cnt[2]=tmp2;
			for(int i=1;i<n-cnt[0];i++){
				if(i&1){
					if(cnt[2])
						tot=(tot+2)%p,cnt[2]--;
					else
						tot=(tot+1)%p,cnt[1]--;
				}
				else{
					if(cnt[1])
						tot=(tot+1)%p,cnt[1]--;
					else
						tot=(tot+2)%p,cnt[2]--;
				}
				res1+=(!tot);
			}
			ans+=max(res0,res1);
		}
		printf("Case #%d: %d\n",test,ans);
	}
	return 0;
}
