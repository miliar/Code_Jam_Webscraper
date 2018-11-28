#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cstring>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;

#define SIZE(x) (int((x).size()))
#define rep(i,l,r) for (int i=(l); i<=(r); i++)
#define repd(i,r,l) for (int i=(r); i>=(l); i--)
#define rept(i,c) for (typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)

#ifndef ONLINE_JUDGE
#define debug(x) { cerr<<#x<<" = "<<(x)<<endl; }
#else
#define debug(x) {}
#endif

int ans[100], a[100];

int check_ge_k(int len, int v)
{
	repd(i,len,1)
	{
		if (a[i]>v) return 1;
		if (a[i]<v) return 0;
	}
	return 1;
}

void print(int len)
{
	LL z=0;
	repd(i,len,1) z=z*10+ans[i];
	cout<<z<<endl;
}

void lemon()
{
	LL n; cin>>n;
	int len=0;
	while (n) len++, a[len]=n%10, n/=10;
	if (len==1)
	{
		cout<<a[1]<<endl;
		return;
	}
	
	if (!check_ge_k(len,1))
	{
		LL bz=1;
		rep(i,1,len-1) bz*=10;
		bz--;
		cout<<bz<<endl;
		return;
	}
	
	repd(i,len,1)
	{
		ans[i]=a[i];
		if (!check_ge_k(i-1, ans[i]))
		{
			ans[i]=a[i]-1;
			rep(j,1,i-1) ans[j]=9;
			print(len);
			return;
		}
	}
	
	print(len);
}

int main()
{
	ios::sync_with_stdio(true);
	#ifndef ONLINE_JUDGE
		freopen("B.in","r",stdin);
	#endif
	int tcase; scanf("%d",&tcase);
	rep(i,1,tcase)
	{
		printf("Case #%d: ",i);
		lemon();
	}
	return 0;
}

