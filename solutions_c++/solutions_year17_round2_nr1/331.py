#include <bits/stdc++.h>

using namespace std;
const double pi=acos(-1.0);
const double eps=1e-9;
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define re return
#define vi vector <int> 
#define pii pair <int,int>
#define pll pair <long long , long long>
typedef long long ll;

const double inf = 1e16;
double ans, tt;
ll t,d,n,k,s;

int main()
{
	ios:: sync_with_stdio(false);
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	cin >> t;
	cout << fixed << setprecision(10);
	for(int test = 1; test <= t; test++)
	{
		cin >> d >> n;
		ans = inf;
		for(int i = 0; i < n;i++)
		{
			cin >> k >> s;
			tt = (d - k)/((double)s);
			ans = min(ans, k/((double)tt) + s);
		}
		cout << "Case #" << test << ": " << ans << "\n";
	}
	return 0;
}
