//In the name of Allah
#include <bits/stdc++.h>
#define fs first
#define sc second
#define mp make_pair
#define pb push_back

using namespace std;

typedef long long ll;
const int N=10000;

int main()
{
	ios::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);

	freopen("C-large.in", "r", stdin);
	freopen("Out.txt", "w", stdout);

	int t;
	ll n, m, k;
	map <ll,ll> x;
	set <ll> y;
	set <ll>::iterator it;

	cin >> t;

	for (int j=1 ; j<=t ; j++)
	{
		cin >> n >> k;

		y.clear(), y.insert(n);
		x.clear(), m=x[n]=1;
		it = y.end(), it--;

		while(m<k)
		{
			k -= m;
			x[n] = 0;
			y.erase(it);
			x[n/2] += m, x[(n-1)/2]+= m;
			y.insert(n/2), y.insert((n-1)/2);
			it = y.end(), it--;
			m = x[n=*it];
		}

		cout << "Case #" << j << ": " << n/2 << ' ' << (n-1)/2 << '\n';
	}

	return 0;
}
