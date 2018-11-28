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
typedef long long LL;
#define fi first
#define se second
#define MP make_pair
#define PB push_back
#define PII pair<LL,LL>
using namespace std;
int Te;
LL K,n;
set<PII> A;
template<class T>
void read(T&x)
{
	char ch=getchar();int mk=1;x=0;for(;ch!='-'&&(ch<'0'||ch>'9');ch=getchar());
	if (ch=='-') mk=-1,ch=getchar();for(;ch>='0'&&ch<='9';ch=getchar()) x=x*10+ch-48;x*=mk;
}
void Insert(LL key,LL cnt)
{
	set<PII>::iterator it=A.lower_bound(MP(key,0));
	if (it!=A.end()&&it->fi==key)
	{
		A.erase(it);
		A.insert(MP(key,cnt+it->se));
	}
	else A.insert(MP(key,cnt));
}
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&Te);
	for(int _=1;_<=Te;_++)
	{
		printf("Case #%d: ",_);
		read(n);read(K);
		A.clear();
		A.insert(MP(-n,1));
		LL Min,Max;
		while (K)
		{
			PII it=*A.begin();
			it.fi*=-1;
			A.erase(A.begin());
			K-=min(K,it.se);
			Max=it.fi/2;Min=(it.fi-1)/2;
			if (Max==Min)
			{
				if (Max>0) Insert(-Max,it.se*2);
			}
			else
			{
				if (Min>0) Insert(-Min,it.se);
				if (Max>0) Insert(-Max,it.se);
			}
		}
		printf("%lld %lld\n",Max,Min);
	}
}


