#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define fst first
#define snd second
#define fore(i,a,b) for(int i=a,ThxDem=b;i<ThxDem;++i)
using namespace std;
typedef long long ll;
typedef pair<int,int> ii;
int t1,t2;
bool can[2][100500];
int dp1[800][800][2];
int dp2[800][800][2];
int f1(int i, int j, bool b) {
	if(i>720||j>720) return 1<<28;
	if(i==720&&j==720)return b==1;
	if(dp1[i][j][b]!=-1) return dp1[i][j][b];
	int r=1<<28;
	if(can[b][i+j])
		r=f1(i+!b,j+b,b);
	if(i+j>0)
		r=min(r,1+f1(i+b,j+!b,!b));
	return dp1[i][j][b]=r;
}
int f2(int i, int j, bool b) {
	if(i>720||j>720) return 1<<28;
	if(i==720&&j==720)return b==0;
	if(dp2[i][j][b]!=-1) return dp2[i][j][b];
	int r=1<<28;
	if(can[b][i+j])
		r=f2(i+!b,j+b,b);
	if(i+j>0)
		r=min(r,1+f2(i+b,j+!b,!b));
	return dp2[i][j][b]=r;
}
int main(){
	int tn;
	scanf("%d",&tn);
	fore(tc,0,tn) {
		memset(dp1,-1,sizeof dp1);
		memset(dp2,-1,sizeof dp2);
		memset(can,1,sizeof can);
		int a,b;
		scanf("%d%d",&a,&b);
		fore(i,0,a){
			int u,v;
			scanf("%d%d",&u,&v);
			fore(j,u,v+1) can[0][j]=0;
		}
		fore(i,a,a+b){
			int u,v;
			scanf("%d%d",&u,&v);
			fore(j,u,v+1) can[1][j]=0;
		}
		int ans=1<<28;
		if(can[0][0]) ans=f1(0,0,0);
		if(can[1][0]) ans=min(ans,f2(0,0,1));
		printf("Case #%d: %d\n",tc+1,ans);
	}
	return 0;
}
