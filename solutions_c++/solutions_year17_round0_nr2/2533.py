#include <iostream>
#include <algorithm>
#include <string>
#include <cmath>
#include <vector>
#include <sstream>
#include <stack>
#include <queue>
#include <map>
#include <climits>
#include <cstdio>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <iomanip>
#include <functional>
using namespace std;
#define db(a) (cout << (#a) << " = " << (a) << endl)
typedef long long ll;

bool tidy(ll n)
{
	ll d = 9;
	while(n>0)
	{
		if(n%10 > d) return false;
		d = n % 10;
		n = n / 10;
	}
	return true;
}

ll dec(ll in)
{
	ll n = in;
	ll d = 9;
	ll r = 1;
	ll last = 0;
	while(n>0)
	{
		if(n%10 > d)
		{
			last = r;
		}
		d = n % 10;
		n = n / 10;
		r *= 10;
	}	
	ll de = ((in%last)+1);
	return in-de;
}

int main()
{
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int T;
	cin>>T;
	for(int t=0;t<T;t++)
	{
		ll N;
		cin>>N;
		//while(!tidy(N)) N--;
		while(!tidy(N)) N = dec(N);
		cout << "Case #" << t+1 << ": " << N << "\n";
	}
  return 0;
}
