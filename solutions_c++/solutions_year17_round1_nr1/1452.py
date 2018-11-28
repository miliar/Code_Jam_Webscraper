#include <bits/stdc++.h>
using namespace std;
//look at my code my code is amazing
#define FOR(i, a, b) for (int i = int(a); i < int(b); i++)
#define FOREACH(it, a) for (typeof(a.begin()) it = (a).begin(); it != (a).end(); it++)
#define ROF(i, a, b) for (int i = int(a); i >= int(b); i--)
#define REP(i, a) for (int i = 0; i < int(a); i++)
#define INF 1000000000
#define INFLL 1000000000000000000LL
#define ALL(x) x.begin(), x.end()
#define MP(a, b) make_pair((a), (b))
#define X first
#define Y second
#define EPS 1e-9
#define DEBUG(x)   cerr << #x << ": " << x << " "
#define DEBUGLN(x) cerr << #x << ": " << x << " \n"
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef long long ll;
typedef vector<bool> vb;
//ios_base::sync_with_stdio(0);//fast entrada/salida ;-)
//cin.tie(NULL); cout.tie(NULL);

char mat[30][30];
int caso = 0;

void solve()
{
	int R, C;

	cin >> R >> C;

	char last = '?';
	for (int i = 0; i < R; ++i)
	{
		last = '?';
		for (int j = 0; j < C; ++j)
		{
			cin >> mat[i][j];
			if(mat[i][j] == '?')
				mat[i][j] = last;
			else
				last = mat[i][j];
		}

		last = '?';
		for (int j = C-1; j >= 0; --j)
		{
			if(mat[i][j] == '?')
				mat[i][j] = last;
			else
				last = mat[i][j];
		}
	}

	for (int j = 0; j < C; ++j)
	{
		last = '?';
		for (int i = 0; i < R; ++i)
		{
			if(mat[i][j] == '?')
				mat[i][j] = last;
			else
				last = mat[i][j];
		}

		last = '?';
		for (int i = R-1; i >= 0; --i)
		{
			if(mat[i][j] == '?')
				mat[i][j] = last;
			else
				last = mat[i][j];
		}
	}


	cout << "Case #" << ++caso << ":\n";
	for (int i = 0; i < R; ++i)
	{
		for (int j = 0; j < C; ++j)
		{
			cout << mat[i][j];
		}
		cout << '\n';
	}


}

int main()
{
	int T;

	cin >> T;

	for (int i = 0; i < T; ++i)
	{
		solve();
	}


	return 0;
}