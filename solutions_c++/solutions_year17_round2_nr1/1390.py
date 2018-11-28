#include<iostream>
#include<vector>
using namespace std;
#define fs first
#define sc second
#define MAX 100000
#define pb push_back
#define mp make_pair
#define INF (1LL<<61)
#define MOD 1000000007
typedef long long Int;
typedef pair<Int,Int> pii;
typedef vector<Int> vi;
typedef vector<pii> vii;
int main()
{
	Int T;
	cin>>T;
	for (Int k=1;k<=T;++k)
	{
		double mx=0.00;
		Int D,N;
		cin>>D>>N;
		for (Int i=0;i<N;++i)
		{
			Int d,s;
			cin>>d>>s;
			mx=max(mx,(D-d)*1.00/s);
		}
		double ans=D/mx;
		printf("Case #%lld: %lf\n",k,ans);
	}
	return 0;
}