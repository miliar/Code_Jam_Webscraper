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

	freopen("A-large.in", "r", stdin);
	freopen("Out.txt", "w", stdout);

	int t, k, cnt;
	bool f;

	string s;

	cin >> t;

	for (int j=1 ; j<=t ; j++)
	{
		cnt = f = 0;

		cin >> s >> k;

		memset(x,0,sizeof(x));

		for(unsigned int i=0 ; i<s.size()-k+1 ; i++)
		{
			x[i+1] += x[i];
			if((s[i]=='-' && x[i+1]%2==0) || (s[i]=='+' && x[i+1]%2))
				cnt++, x[i+1]++, x[i+k+1]--;
		}

		for(unsigned int i=0 ; i<s.size() ; i++)
		{
			if (i>=s.size()-k+1)
				x[i+1] += x[i];

			f |= ((s[i]=='-' && x[i+1]%2==0) || (s[i]=='+' && x[i+1]%2));
		}

		cout << "Case #" << j << ": ";

		if(f)
			cout << "IMPOSSIBLE";
		else
			cout << cnt;

		cout << '\n';
	}

	return 0;
}
