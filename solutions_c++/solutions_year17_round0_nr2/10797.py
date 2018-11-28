#include <bits/stdc++.h>
using namespace std;

bool solv (long long n)
{
	vector <int> v;
	while(n)
	{
		v.push_back(n%10);
		n /= 10;
	}
	reverse (v.begin(),v.end());
	for (int i = 0; i < v.size()-1 ; ++i)
	{
		if (v[i] > v[i+1])
			return 0;
	}
	return 1;
}
int main ()
{
	freopen("B-small-attempt5.in","r",stdin);
    freopen("ansr.txt","w",stdout);
	int tc;
	long long n;
	cin >> tc;
	for (int i = 1; i < tc+1 ;i++)
	{
		cin >> n;
		while(true)
		{
			if (solv(n))
			{
				cout << "Case #"<< i <<": " << n << '\n';
				break;
			}
			else
				-- n;

		}
	}
	return 0;
}
