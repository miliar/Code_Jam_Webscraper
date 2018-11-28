#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
using ll = long long;

ll answerl, answerr, answerm;

string auxil(ll k)
{
	string ret;

	while(k > 1)
	{
		ret.push_back((k&1) + '0');
		k >>= 1;
	}

//	reverse(ret.begin(), ret.end());

//	cout<<ret<<'\n';
	return ret;
}

ll solve(ll t, ll k)
{
	string s = auxil(k);	

	ll left, right, mid, n;
	ll lsize, rsize;
	left = 0;
	right = t + 1;

	for(int i = 0 ; i < s.size() ; i++)
	{
		char c = s[i];

		n = right - left - 1;
		mid = (left + right) / 2;

		lsize = mid - left - 1;
		rsize = right - mid - 1;

		if(lsize < rsize)
		{
			if(rsize <= 0)
			{
				right = mid;
			}
			else if(c == '0')
			{
				left = mid;
			}
			else
			{
				right = mid;
			}
		}
		else
		{
			if(lsize <= 0)
				left = mid;
			else if(c == '0')
			{
				right = mid;
			}
			else
			{
				left = mid;
			}
		}
	}

	mid = (left + right) / 2;
	lsize = mid - left - 1;
	rsize = right - mid - 1;
//
//	if(rsize < 0) rsize = 0;
//	if(lsize < 0) lsize = 0;
//
	answerl = max(lsize, rsize);
	answerr = min(lsize, rsize);

//	cout<<left<<' '<<right<<'\n';
	return 0;
}

int main()
{
	ios_base::sync_with_stdio(0);cin.tie(0);

	freopen("C-large.in", "r", stdin);
  freopen("output4.txt", "w", stdout);

	int tt;
	cin>>tt;

	for(int tc = 1; tc <= tt ; tc++)
	{
		cout<<"Case #"<<tc<<": ";
		ll t,k;
		cin>>t>>k;
		solve(t, k);
		cout<<answerl<<' '<<answerr<<'\n';
	}	

	return 0;
}
