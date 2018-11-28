#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define pb push_back
#define F first
#define S second
#define all(v) v.begin(),v.end()
#define make0(a) memset(a,0,sizeof(a))
#define make1(a) memset(a,-1,sizeof(a))
#define fast_cin() ios::sync_with_stdio(false);

const int mod = 1e9+7;

int main()
{
	fast_cin();
	int T;
	cin >> T;	
	for(int f=1;f<=T;f++)
	{
		double D,N;
		cin >> D >> N;
		pair <double,double> A[(int)N];
		for(int i=0;i<(int)N;i++)
			cin >> A[i].F >> A[i].S;
		double t[(int)N];
		double mn=0;
		for(int i=0;i<N;i++)
		{
			double dist = D-A[i].F;
			t[i] = dist/A[i].S;
			mn = max(t[i],mn);
		}
		double ans = D/mn;
		printf("Case #%d: %.7lf\n",f, ans);
	}
	return 0;
}