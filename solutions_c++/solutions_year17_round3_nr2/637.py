//In the name of Allah
#include <bits/stdc++.h>
#define fs first
#define sc second
#define mp make_pair
#define pb push_back

using namespace std;

typedef long long ll;

const double PI = 3.14159265358979323846264338327950288419716939937;
const int N=1440, M=721;

int arr[N], dp[N][M][3][2];

int solve (int ind, int x, int y, int pre, int s)
{
	if(ind == N)
		return (s==pre)*-1;

	if((x==M-1 && arr[ind]==0) || (y==M-1 && arr[ind]==1))
		return N+1;

	int &ret = dp[ind][x][pre][s];

	if(ret!=-1)
		return ret;

	if (arr[ind]==0 || y==M-1)
		ret = solve(ind+1, x+1, y, 0, (!ind ? 0 : s))+(pre!=0);

	else if (arr[ind]==1 || x==M-1)
		ret = solve(ind+1, x, y+1, 1, (!ind ? 1 : s))+(pre!=1);

	else
		ret = min(solve(ind+1, x+1, y, 0, (!ind ? 0 : s))+(pre!=0)
				, solve(ind+1, x, y+1, 1, (!ind ? 1 : s))+(pre!=1));

	return ret;
}

int main()
{
	ios::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);

	freopen ("in.in", "r", stdin);
	freopen ("out.txt", "w", stdout);

	int t, c, j, s, e;

	cin >> t;

	for (int tt=1 ; tt<=t ; tt++)
	{
		memset(arr,-1,sizeof arr);
		memset(dp,-1,sizeof dp);

		cin >> c >> j;

		while (c--)
		{
			cin >> s >> e;

			while (s<e)
				arr[s]=0, s++;
		}

		while (j--)
		{
			cin >> s >> e;

			while (s<e)
				arr[s]=1, s++;
		}

		cout << "Case #" << tt << ": " << solve(0,0,0,2,0) << '\n';
	}

	return 0;
}
