#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

#define pll pair<ll, ll>
#define F first
#define S second
#define mp make_pair
#define pb push_back

const int MAX_SIZE = 1e3+10;
const long double PI = 3.141592653589793238;
const double INF = 1e12;
ll A[MAX_SIZE][MAX_SIZE];

int n, k;

vector< pair<ll, ll> > P;

ll dp(int i, int rem, int prev) 
{
	if(rem == 0)
		return P[prev].F * P[prev].F;
	if(i == n)
		return -INF;
	if(A[rem][prev] == -1)
	{
		if(rem == k)
			A[rem][prev] = max(2 * P[i].S * P[i].F + dp(i + 1, rem - 1, i), dp(i + 1, rem, prev));
			// return max(2 * P[i].S * P[i].F + dp(i + 1, rem - 1, P[i].F), dp(i + 1, rem, prev));
		else
			A[rem][prev] = max(2 * P[i].S * P[i].F + (P[prev].F*P[prev].F - P[i].F*P[i].F) + dp(i + 1, rem - 1, i), dp(i + 1, rem, prev));
			// return max(2 * P[i].S * P[i].F + (prev*prev - P[i].F*P[i].F) + dp(i + 1, rem - 1, P[i].F), dp(i + 1, rem, prev));
	}
	return A[rem][prev];
}

int main(){
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++) {
		for(int i = 0; i < MAX_SIZE; i++)
		{
			for(int j = 0; j < MAX_SIZE; j++)
			{
				A[i][j] = -1;
			}
		}
		P.clear();
		// int k;
		cin >> n >> k;
		ll r, h;	
		for(int i = 1; i <= n; i++)
		{
			cin >> r >> h;
			// cin >> P[i].F >> P[i].S;
			P.pb(mp(r, h));
		}
		sort(P.begin(), P.end(), greater<pair<ll, ll> >());
		// cout << P[0].F << " " << P[0].S << endl;
		long double ans = dp(0, k, n) * PI;
		printf("Case #%d: %.8Lf\n", t, ans);
	}
	return 0;
}