//#include<stdio.h>
//#include<stdlib.h>
#include<bits/stdc++.h>
//#define Min(a,b,c) min((a),min((b),(c)))
#define mp(a,b) make_pair((a),(b))
#define pii pair<int,int>
#define pll pair<LL,LL>
#define pb(x) push_back(x)
#define x first
#define y second
#define sqr(x) ((x)*(x))
#define EPS 1e-11
#define MEM(x) memset(x,0,sizeof(x))
//#define N 200005
#define M
#define pi 3.14159265359
using namespace std;
typedef long long LL;
int main(){
	int t;
	scanf("%d",&t);
	for(int T=1;T<=t;T++){
		int n,p;
		scanf("%d %d",&n,&p);
		int a[100];
		for(int i=0;i<n;i++)
		scanf("%d",&a[i]);
		vector<pii> v[100];
		for(int i=0;i<n;i++){
			for(int j=0;j<p;j++){
				int x;
				scanf("%d",&x);
				v[i].pb(mp(10*x/(11*a[i])+(10*x%(11*a[i])!=0),10*x/(9*a[i])));
			//	printf("%d %d",v[i].back().x,v[i].back().y);
				if(v[i].back().x>v[i].back().y)
				v[i].pop_back(); 
			}
			sort(v[i].begin(),v[i].end());
		}
		int it[100];
		memset(it,0,sizeof(it));
		int ans=0;
		for(int i=v[0][it[0]].x;i<=1e6;){
			int ok=1;
			for(int j=0;j<n;j++){
				while(v[j][it[j]].y<i&&it[j]<v[j].size())
				it[j]++;
				if(v[j][it[j]].x>i||it[j]==v[j].size())
				ok=0;
			}
			if(ok)
			{
				ans++;
				for(int j=0;j<n;j++)
				it[j]++;
				i=v[0][it[0]].x;
			}
			else{
				i++;
			}
		}
		printf("Case #%d: %d\n",T,ans);
	}
}

/*90 110
180 220
270 330
360 440
450 550
540 660
630 770
*/
