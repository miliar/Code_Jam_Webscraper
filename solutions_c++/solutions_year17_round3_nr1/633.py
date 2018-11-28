//In the name of Allah
#include <bits/stdc++.h>
#define fs first
#define sc second
#define mp make_pair
#define pb push_back

using namespace std;

typedef long long ll;

const double PI = 3.14159265358979323846264338327950288419716939937;
const int N=1e3;

pair <double,double> x[N];

int main()
{
	ios::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);

	freopen ("in.in", "r", stdin);
	freopen ("out.txt", "w", stdout);

	int n, k, t, r, h;
	double ans, tmp;

	cin >> t;

	for (int tt=1 ; tt<=t ; tt++)
	{
		cin >> n >> k;
		ans = 0;

		for(int i=0 ; i<n ; i++)
		{
			cin >> r >> h;

			x[i].fs = 2*PI*r*h;
			x[i].sc = PI*r*r;
		}

		sort(x,x+n);

		for(int i=0 ; i<n ; i++)
		{
			tmp = x[i].sc+x[i].fs;

			for(int j=n-1, l=1 ; l<k ; j--)
				if(j!=i)
					tmp += x[j].fs, l++;

			ans = max(ans,tmp);
		}

		cout << "Case #" << tt << ": ";
		cout << fixed << setprecision(11) << ans << '\n';
	}
	return 0;
}
