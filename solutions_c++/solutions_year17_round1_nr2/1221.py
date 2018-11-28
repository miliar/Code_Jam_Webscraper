#include "bits/stdc++.h"
#define MAXN 100009
#define INF 1000000007
#define mp(x,y) make_pair(x,y)
#define all(v) v.begin(),v.end()
#define pb(x) push_back(x)
#define wr cout<<"----------------"<<endl;
#define ppb() pop_back()
#define ff first
#define tr(ii,c) for(typeof((c).begin()) ii=(c).begin();ii!=(c).end();ii++)
#define ss second
#define eps (1e-9)
#define my_little_dodge 46
using namespace std;

typedef long long ll;
typedef pair<int,int> PII;
template<class T>bool umin(T& a,T b){if(a>b){a=b;return 1;}return 0;}
template<class T>bool umax(T& a,T b){if(a<b){a=b;return 1;}return 0;}
const int N=55;
const int L=2e6+9;
vector<PII>add[L],rem[L];
int d[N],arr[N][N],vis[N][N];
set<int>cnt[N];
PII solve(double x,double y,int ind){
	int xx,yy;
	if(x-int(x)>eps)
		xx=int(x)+1;
	else
		xx=int(x);
	if(y-int(y)>eps)
		yy=int(y);
	else
		yy=int(y);
	if(xx%d[ind]==0)
		xx=xx/d[ind];
	else
		xx=xx/d[ind]+1;
	if(yy%d[ind]==0)
		yy=yy/d[ind];
	else
		yy=yy/d[ind];		
	return mp(xx,yy);	
}
int main(){
    freopen("file.in", "r", stdin);
    freopen("file.out", "w", stdout);
    int t;
    scanf("%d",&t);
    for(int test=1;test<=t;test++){
		int n,p;
		scanf("%d%d",&n,&p);
		for(int i=1;i<=n;i++)
			scanf("%d",d+i);
		for(int i=1;i<=n;i++)
			for(int j=1;j<=p;j++)
				scanf("%d",&arr[i][j]);
		for(int i=1;i<=n;i++){
			for(int j=1;j<=p;j++){
				PII res=solve((arr[i][j]*100.0)/110.0,(arr[i][j]*100.0)/90.0,i);
				if(res.ff<=res.ss){
					add[res.ff].pb(mp(i,j));
					rem[res.ss].pb(mp(i,j));
				}
			}
		}
		int ans=0;
		vector<int>cur;
		for(int i=1;i<L;i++){
			tr(it,add[i])
				cnt[it->ff].insert(it->ss);
			while(1){	
				cur.clear();
				for(int j=1;j<=n;j++){
					tr(it,cnt[j])
						if(!vis[j][*it]){
							cur.pb(*it);
							break;
						}
				}	
				if((int)cur.size()==n){
					for(int j=0;j<n;j++)
						vis[j+1][cur[j]]=1;
					ans++;	
				}
				else
					break;
			}
			tr(it,rem[i])
				cnt[it->ff].erase(it->ss);
			add[i].clear();	
			rem[i].clear();	
		}
		memset(vis,0,sizeof vis);
		printf("Case #%d: %d\n",test,ans);
	}
	return 0;
}
