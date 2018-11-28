//In the name of Allah
#include <bits/stdc++.h>
#define fs first
#define sc second
#define mp make_pair
#define pb push_back

using namespace std;

typedef long long ll;
const int N=1e3+7;

int seats[N], person[N];

int main()
{
	ios::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
	freopen ("Out.txt","w",stdout);
	freopen ("in.in","r",stdin);

	int t, n, m, mx1, c, p, b, mx2, sum;

	cin >> t;

	for(int tt=1 ; tt<=t ; tt++)
	{
		cin >> n >> c >> m;

		sum = mx1 = mx2 = 0;
		memset(seats, 0, sizeof seats);
		memset(person, 0, sizeof person);

		for(int i=0 ; i<m ; i++)
		{
			cin >> p >> b;

			seats[p]++, person[b]++;
			mx1 = max(mx1, person[b]);
		}

		while (mx1*n < m)
			mx1++;

		for(int i=1 ; i<=n ; i++)
		{
			if(seats[i] > mx1+sum)
				mx1++, i=0, sum=mx2=0;

			else
			{
				mx2 += max(0,seats[i]-mx1);
				sum += mx1-seats[i];
			}
		}

		cout << "Case #" << tt << ": " << mx1 << ' ' << mx2 << '\n';
	}

	return 0;
}
