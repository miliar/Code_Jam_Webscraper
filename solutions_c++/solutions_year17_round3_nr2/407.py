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
const int N=755;
int vis[N*2],dp[N][N][2][2];
int rec(int x,int y,int turn,int st){
	if(x>720 or y>720)
		return INF;
	if(x==720 and y==720)
		return (st!=turn);
	int &ret=dp[x][y][turn][st];
	if(~ret)
		return ret;
	if(!turn){
		if(vis[x+y]==2)
			return ret=rec(x,y+1,1,st)+1;
		if(vis[x+y]==1)
			return ret=rec(x+1,y,0,st);
		return ret=min(rec(x+1,y,0,st),rec(x,y+1,1,st)+1);
	}	
	if(vis[x+y]==2)
		return ret=rec(x,y+1,1,st);
	if(vis[x+y]==1)
		return ret=rec(x+1,y,0,st)+1;
	return ret=min(rec(x+1,y,0,st)+1,rec(x,y+1,1,st));
}
int main(){
    freopen("file.in", "r", stdin);
    freopen("file.out", "w", stdout);
	int t;
	scanf("%d",&t);
	for(int test=1;test<=t;test++){
		memset(dp,-1,sizeof dp);
		memset(vis,0,sizeof vis);
		int a,b;
		scanf("%d%d",&a,&b);
		while(a--){
			int l,r;
			scanf("%d%d",&l,&r);
			for(int i=l;i<r;i++)
				vis[i]=1;	
		}
		while(b--){
			int l,r;
			scanf("%d%d",&l,&r);
			for(int i=l;i<r;i++)
				vis[i]=2;
		}	
		printf("Case #%d: %d\n",test,min(rec(0,0,1,1),rec(0,0,0,0)));
	}
	return 0;
}
