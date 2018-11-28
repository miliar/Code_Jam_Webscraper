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
int n,D,T;
PII p[1010];
template<class T>
void read(T&x)
{
	char ch=getchar();int mk=1;x=0;for(;ch!='-'&&(ch<'0'||ch>'9');ch=getchar());
	if (ch=='-') mk=-1,ch=getchar();for(;ch>='0'&&ch<='9';ch=getchar()) x=x*10+ch-48;x*=mk;
}
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	read(T);
	for(int _=1;_<=T;_++)
	{
		printf("Case #%d: ",_);
		read(D);read(n);
		for(int i=1;i<=n;i++) read(p[i].fi),read(p[i].se);
		double Min=0;
		for(int i=1;i<=n;i++)
		{
			bool flag=1;
			for(int j=1;j<i;j++)
				if (p[i].se>p[j].se&&(LL)(p[j].fi-p[i].fi)*p[i].se<(LL)(D-p[i].fi)*(p[i].se-p[j].se))
				{
					flag=0;
					break;
				}
			if (flag) Min=max(Min,(double)(D-p[i].fi)/p[i].se);
		}
		printf("%.7lf\n",D/Min);
	}
	return 0;
}
