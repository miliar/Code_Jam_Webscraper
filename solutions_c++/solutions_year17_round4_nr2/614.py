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
int n,m,C,T,a[1010],c[1010];
PII p[1010];
template<class T>
void read(T&x)
{
	char ch=getchar();int mk=1;x=0;for(;ch!='-'&&(ch<'0'||ch>'9');ch=getchar());
	if (ch=='-') mk=-1,ch=getchar();for(;ch>='0'&&ch<='9';ch=getchar()) x=x*10+ch-48;x*=mk;
}
int ceil(int a,int b)
{
	if (a%b==0) return a/b;return a/b+1;
}
bool check(int mid)
{
	int S=0;
	for(int i=1;i<=n;i++)
	{
		S+=a[i];
		if (S>mid*i) return 0;
	}
	return 1;
}
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	read(T);
	for(int _=1;_<=T;_++)
	{
		printf("Case #%d: ",_);
		read(n);read(C);read(m);
		for(int i=1;i<=n;i++) a[i]=0;
		for(int i=1;i<=C;i++) c[i]=0;
		for(int i=1;i<=m;i++) 
		{
			read(p[i].fi),read(p[i].se);
			a[p[i].fi]++;
			c[p[i].se]++;
		}
		int L=0,R=m;
		for(int i=1;i<=C;i++) L=max(L,c[i]);
		while (L+1<R)
		{
			int mid=(L+R)>>1;
			if (check(mid)) R=mid;
			else L=mid;
		}
		if (check(L)) R=L;
		int ans=R;
		printf("%d ",ans);
		int cnt=0;
		for(int i=n;i;i--) cnt+=max(0,a[i]-ans);
		printf("%d\n",cnt);
	}
	return 0;
}

