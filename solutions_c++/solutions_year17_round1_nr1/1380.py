#include<bits/stdc++.h>

#define MOD 1000000007
#define MAX 100005
#define ll long long
#define slld(t) scanf("%lld",&t)
#define sd(t) scanf("%d",&t)
#define ss(x) scanf("%s",x)
#define pd(t) printf("%d\n",t)
#define plld(t) printf("%lld\n",t)
#define pii pair<int,int>
#define pll pair<ll,ll>
#define tr(container,it) for(typeof(container.begin()) it=container.begin();it!=container.end();it++)
#define mp(a,b) make_pair(a,b)
#define FF first
#define SS second
#define pb(x) push_back(x)
#define vi vector<int>
#define vpii vector<pii >
#define vll vector<ll>
#define clr(x) memset(x,0,sizeof(x))

using namespace std;

char arr[26][26];
bool ok[26][26];

void solve(){
	int r,c;sd(r);sd(c);
	for(int i=0;i<r;i++) ss(arr[i]);
	clr(ok);
	for(int i=0;i<r;i++) for(int j=0;j<c;j++) if(arr[i][j]=='?') ok[i][j]=1;
	for(int i=0;i<r;i++){
		for(int j=0;j<c;j++){
			if(ok[i][j]) continue;
			int left;
			for(left=j-1;left>=0;left--) if(arr[i][left]!='?') break;
			++left;
			int right;
			for(right=j+1;right<c;right++) if(arr[i][right]!='?') break;
			right--;
			int top;
			for(top=i-1;top>=0;top--){
				bool ok=1;
				for(int jj=left;jj<=right;jj++) if(arr[top][jj]!='?'){
					ok=0;
					break;
				}
				if(!ok) break;
			}
			++top;
			int bottom;
			for(bottom=i+1;bottom<r;bottom++){
				bool ok=1;
				for(int jj=left;jj<=right;jj++){
					if(arr[bottom][jj]!='?'){
						ok=0;
						break;
					}
				}
				if(!ok) break;
			}
			bottom--;
			for(int x=top;x<=bottom;x++) for(int y=left;y<=right;y++) arr[x][y]=arr[i][j];
		}
	}
	for(int i=0;i<r;i++){
		for(int j=0;j<c;j++){
			printf("%c",arr[i][j]);
		}
		printf("\n");
	}
}

#define adkro

int main(){

#ifdef adkroxx
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
#endif
	
	int t;sd(t);	
	for(int tt=1;tt<=t;tt++){
		printf("Case #%d: \n",tt);
		solve();
	}
}
