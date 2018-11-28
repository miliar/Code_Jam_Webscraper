//In the name of Allah
#include <bits/stdc++.h>
#define fs first
#define sc second
#define mp make_pair
#define pb push_back

using namespace std;

typedef long long ll;
const int N=10000;

int x[N];

int main()
{
	ios::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);

	freopen("B-large.in", "r", stdin);
	freopen("Out.txt", "w", stdout);

	int t, x;

	string s;

	cin >> t;

	for (int j=1 ; j<=t ; j++)
	{
		cin >> s;

		x=s.size();

		for(int i=s.size()-1 ; i ; i--)
		{
			if(s[i]<s[i-1])
			{
				while(s[i-1]=='0')
					i--;

				x=i, s[i-1]--;
			}
		}

		cout << "Case #" << j << ": ";

		for(int i=(s[0]=='0') ; i<x ; i++)
			cout << s[i];

		for(unsigned int i=x ; i<s.size() ; i++)
			cout << 9;

		cout << '\n';
	}

	return 0;
}
