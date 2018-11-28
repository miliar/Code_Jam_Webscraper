#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <vector>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <sstream>
using namespace std;

typedef long long ll;
struct Solver
{
	Solver()
	{
	}
	string solve()
	{
		ll n,k;
		cin>>n>>k;
		map<ll,ll> s;
		s[n]=1;
		k--;
		ostringstream out;
		while(true)
		{
			ll sz=s.rbegin()->first;
			ll cnt=s.rbegin()->second;
			s.erase(s.find(s.rbegin()->first));
			if(cnt > k)
			{
				out<<(sz)/2<<" "<<(sz-1)/2;
				break;
			}
			else
			{
				s[(sz-1)/2]+=cnt;
				s[sz/2]+=cnt;
				k-=cnt;
			}
		}
		return out.str();
	}
};

int main()
{
	int T;
	scanf("%d",&T);
	for(int test=1;test<=T;test++)
		cout<<"Case #"<<test<<": "<<Solver().solve()<<endl;
	return 0;
}
