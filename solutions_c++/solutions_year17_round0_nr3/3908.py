#include <iostream>
#include <map>
#include <functional>
using namespace std;
int solve()
{
	long long N,K,curr=0;
	cin >> N >> K;
	map<long long ,long long ,greater<long long> > M1,M2 ;
	M1[N]=1;
	while(curr<K)
	{
		for(auto &x:M1)
		{
			long long v1=((x.first-1)/2),v2=x.first/2;
			curr+=x.second;
			if(curr>=K)
			{
				cout << v2 << " " << v1 << endl ;
				return 0 ;
			}
			M2[v1]+=x.second;
			M2[v2]+=x.second;
		}
		M1=M2;
		M2.clear();
	}
	cout << 0 << " " << 0 << endl ;
	return 0;
}
int main()
{
	int T;
	cin >> T;
	for(int i=1;i<=T;i++)
		printf("Case #%d: ",i),solve();
	return 0;
}
/*
 
*/