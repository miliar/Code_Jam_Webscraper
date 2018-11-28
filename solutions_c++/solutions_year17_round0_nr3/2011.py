#include <bits/stdc++.h>

#define icin(x) scanf("%d",&x)
#define lcin(x) scanf("%lld",&x)
#define pb push_back
#define LL long long
#define F first
#define S second
#define VPI vector< pair<int,int> >
#define VVI vector< vector<int> > 
#define BC(x) __builtin_popcount(x)

using namespace std;

pair<LL,LL> f(LL n, LL k)
{
	//cout << k << endl;
	if(k == 1)
	{
		LL tmp = (n+1)/2; 
		return {n - tmp,tmp-1};
	}
	else
	{
		LL m1 = (n-1)/2;
		LL m2 = n-1-m1;

		if(m2 <= m1)
		{
			if(k%2)
				return f(m2,(k-1)/2);
			else
				return f(m1,k/2);
		}
		else
		{
			if(k%2 == 1)
				return f(m1,(k-1)/2);
			else
				return f(m2,k/2);
		}
	}
}

int main()
{
	int t;
	icin(t);
	for(int tc=1; tc<=t; tc++)
	{
		LL n,k;
		cin >> n >> k;
		auto p = f(n,k);
		printf("Case #%d: %lld %lld\n",tc,p.F,p.S);
	}
	return 0;
}