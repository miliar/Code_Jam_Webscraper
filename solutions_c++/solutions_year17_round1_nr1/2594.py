#include<bits/stdc++.h>
using namespace std;
#define pb push_back
#define sz(x) ((int)x.size())
#define clr(a,b) memset(a,b,sizeof(a))
typedef long long ll;
const int maxn=100+7;
const int INF=1e9+7;
int n,m,t;
char a[maxn][maxn];

map<char,bool> M;
bool subcheck(int i,int j){
	int i1=i,j1=j,i2=i,j2=j;
	char c=a[i][j];
	while(i1-1>=0&&a[i1-1][j1]==c)i1--;
	while(j1-1>=0&&a[i1][j1-1]==c)j1--;
	while(i1+1>=0&&a[i1+1][j1]==c)i1++;
	while(j1+1>=0&&a[i1][j1+1]==c)j1++;
	for(int i=i1;i<=i2;i++)
		for(int j=j1;j<=j2;j++)
			if(a[i][j]!=c)return false;
	return true;
}
bool check(){
	M.clear();
	for(int i=0;i<n;i++)
		for(int j=0;j<m;j++){
			char c=a[i][j];
			if(c=='?')return false;
			if(M.find(c)!=M.end())continue;
			M[c]=true;
			if(!subcheck(i,j))return false;
		}
	return true;
}

void dfs(int x,int y){
	int i1=x,j1=y;
	char c=a[x][y];
	if(c=='?')return;
	while(j1-1>=0&&a[i1][j1-1]=='?')a[i1][j1-1]=c,j1--;
	i1=x,j1=y;
	while(j1+1>=0&&a[i1][j1+1]=='?')a[i1][j1+1]=c,j1++;
}
char udfs(int x,int y){
	if(x<0||y<0||x>=n||y>=m)return '?';
	if(a[x][y]!='?')return a[x][y];
	char uc=udfs(x-1,y);
	if(uc!='?')return a[x][y]=uc;
	return a[x][y];
}
char ddfs(int x,int y){
	if(x<0||y<0||x>=n||y>=m)return '?';
	if(a[x][y]!='?')return a[x][y];
	char uc=ddfs(x+1,y);
	if(uc!='?')return a[x][y]=uc;
	return a[x][y];
}
int main(){
#ifdef AC
freopen("A-large.in","r",stdin);
freopen("data.out","w",stdout);
#endif
	int T;
	cin>>T;
	int tcase=1;
	while(T--){
		printf("Case #%d:\n",tcase++);
		cin>>n>>m;
		for(int i=0;i<n;i++)
			for(int j=0;j<m;j++)
				cin>>a[i][j];
		for(int i=0;i<n;i++)
			for(int j=0;j<m;j++)
				dfs(i,j);
		for(int i=0;i<n;i++)
			for(int j=0;j<m;j++)
			if(a[i][j]=='?')if(udfs(i,j)=='?')ddfs(i,j);
		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				cout<<a[i][j];
			}
			cout<<endl;
		}
	}
	return 0;
}

