#include<cstdio>
#include<iostream>
#include<algorithm>
using namespace std;
int f[101][101][101][4];
int dfs(int a,int b,int c,int d){
	if(a+b+c==0)
		return 0;
	if(f[a][b][c][d]!=-1)
		return f[a][b][c][d];
	int &ret=f[a][b][c][d];
	if(a)
		ret=max(ret,dfs(a-1,b,c,(d+1)&3));
	if(b)
		ret=max(ret,dfs(a,b-1,c,(d+2)&3));
	if(c)
		ret=max(ret,dfs(a,b,c-1,(d+3)&3));
	ret+=!d;
	return ret;
}
#include<cstring>
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("1.out","w",stdout);
	int T;
	int n,m,a[200],c[4],cases=0;
	cin>>T;
	while(T--){
		
		memset(f,-1,sizeof f);
		c[0]=c[1]=c[2]=c[3]=0;
		cin>>n>>m;
		for(int i=1;i<=n;i++){ 
			cin>>a[i];
			a[i]%=m;
			c[a[i]]++;
		} 
		printf("Case #%d: ",++cases);
		if(m==3)
			cout<<c[0]+min(c[2],c[1])+((max(c[2],c[1])-min(c[1],c[2]))+2)/3<<endl;
		else if(m==2)
			cout<<c[0]+(c[1]+1)/2<<endl;
		else
			cout<<c[0]+dfs(c[1],c[2],c[3],0)<<endl;
	}
}

