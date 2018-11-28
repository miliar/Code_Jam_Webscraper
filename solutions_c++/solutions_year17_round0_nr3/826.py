#include <iostream>
#include <map>

using namespace std;

long long n,k,bound,ntest;
map<long long,long long> f;

long long cal(long long u)
{
	if (u<bound) return 0;
	if (f.count(u)) return f[u];
	long long tp=(u-1)/2;
	f[u]=cal(tp)+cal(u-1-tp)+1;
	return f[u];
}

long long co(long long x)
{
	f.clear();
	bound=x;
	return cal(n);
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin >> ntest;
	for (int __=1;__<=ntest;__++)
	{
		cin >> n >> k;
		long long l=1,r=n,res=1;
		while (l<=r)
		{
			long long m=(l+r)/2;
			if (co(m)>=k) res=m,l=m+1;
			else r=m-1;
		}
		cout << "Case #" << __ << ": ";
		cout << max(res-1-((res-1)/2),(res-1)/2) << " " <<min(res-1-((res-1)/2),(res-1)/2) <<"\n";
	}
}