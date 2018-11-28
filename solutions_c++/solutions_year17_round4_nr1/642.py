#include<cstdio>
#include<cstring>
#include<string>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<cmath>
#include<iostream>
#define fi first
#define se second
#define MP make_pair
#define PB push_back
#define PII pair<int,int>
typedef long long LL;
using namespace std;
int T,n,P,f[110][110][110][4],c[10],a[110];
template<class T>
void read(T&x)
{
	char ch=getchar();int mk=1;x=0;for(;ch!='-'&&(ch<'0'||ch>'9');ch=getchar());
	if (ch=='-') mk=-1,ch=getchar();for(;ch>='0'&&ch<='9';ch=getchar()) x=x*10+ch-48;x*=mk;
}
int dfs(int x,int y,int z,int k)
{
	if (f[x][y][z][k]!=-1) return f[x][y][z][k];
	if (x==0&&y==0&&z==0) return 0;
	int&res=f[x][y][z][k];
	if (x) res=max(res,dfs(x-1,y,z,(k+1)%P)+(k==0));
	if (y) res=max(res,dfs(x,y-1,z,(k+2)%P)+(k==0));
	if (z) res=max(res,dfs(x,y,z-1,(k+3)%P)+(k==0));
	return res;
}
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	read(T);
	for(int _=1;_<=T;_++)
	{
		printf("Case #%d: ",_);
		read(n);read(P);
		memset(c,0,sizeof(c));
		for(int i=1;i<=n;i++) 
		{
			read(a[i]);
			a[i]=a[i]%P;
			c[a[i]]++;
		}
		memset(f,-1,sizeof(f));
		printf("%d\n",c[0]+dfs(c[1],c[2],c[3],0));
	}
	return 0;
}
