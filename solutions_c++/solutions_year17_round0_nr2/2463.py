#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <algorithm>
#include <cstring>
#include <string>
#include <cmath>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <iomanip>
#include <queue>
#include <functional>
#include <list>
#include <set>
#include <sstream>
#define ll long long
#define INF 1000000007

using namespace std;

bool check(ll x)
{
	ll tmp=10;
	while(x>0)
	{
		if(x%10<=tmp)
			tmp=x%10;
		else
			return false;
		x/=10;
	}
	return true;
}

int main()
{
	ios::sync_with_stdio(false);

	//while(cin>>n)

	int T;
	cin>>T;
	for(int cas=1;cas<=T;cas++)
	{
		ll n,ans=-1;
		cin>>n;

		if(check(n))
			ans=n;
		else
		{
			ll p=n,q=1;
			while(p>0)
			{
				p/=10,q*=10;
				if(check(p-1))
				{
					ans=p*q-1;
					break;
				}
			}
		}
		assert(ans!=-1);
		cout<<"Case #"<<cas<<": "<<ans<<endl;
		//cout<<"Case "<<cas<<": ";
	}

	return 0;
}
