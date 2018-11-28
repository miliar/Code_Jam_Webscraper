#include <bits/stdc++.h>
#define PI                3.14159265358979323846264338327950
#define pb                push_back
#define mp                make_pair
#define all(a)            (a).begin(), (a).end()
#define clr(a,h)          memset(a, (h), sizeof(a))
#define F first
#define S second
int in() {int r = 0, c; for (c = getchar(); c <= 32; c = getchar()); if (c == '-') return -in(); for (; c > 32; r = (r << 1) + (r << 3) + c - '0', c = getchar()); return r;}

using namespace std;

const int INF = int(1e9 + 7);
typedef pair<int, int>  ii;
typedef vector<int>     vi;
typedef vector<ii>      vii;
typedef long long       ll;
typedef vector<ll>      vll;

char M[30][30];
bool vis[30][30];
int n, m;

bool check(int i, int j, int y, int x, char c)
{
	for (; i <= y; i++)
	{
		for (int k = j; k <= x; k++)
		{
			if (M[i][k] != '?' && M[i][k] != c && !vis[i][k]) return false;
		}
	}
	return true;
}

void fill(int i, int j, int y, int x, char c)
{
	for (; i <= y; i++)
	{
		for (int k = j; k <= x; k++)
		{
			M[i][k] = c;
			vis[i][k] = true;
		}
	}
}

void printt()
{
	cout << "matriz:\n";
	for (int i = 0; i < n; ++i)
	{
		for (int j = 0; j < m; ++j)
		{
			cout << M[i][j];
		}
		cout << endl;
	}
}


int main()
{
	//std::ios::sync_with_stdio(false);
	freopen("A-small-attempt0 (1).in","r",stdin);
	freopen("A-small-attempt0 (1).out","w",stdout);
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t)
	{
		cin >> n >> m;
		clr(vis, false);
		for (int i = 0; i < n; ++i)
		{
			for (int j = 0; j < m; ++j)
			{
				cin >> M[i][j];
			}
		}
		for (int i = 0; i < n; ++i)
		{
			for (int j = 0; j < m; ++j)
			{
				if (vis[i][j]) continue;
				int a = i, b = j, maxArea = 0;
				char x;
				for (int k = i; k < n; k++)
				{
					for (int l = j; l < m; l++)
					{
						if (M[k][l] != '?')
						{
							char c = M[k][l];
							//cout<<c<<endl;
							if (!check( i, j, k, l, c )) break;
							for (int o = k; o < n; o++)
							{
								for (int p = l; p < m; p++)
								{
									if (check(i, j, o, p, c) && maxArea < (o - i + 1) * (p - j + 1))
									{
										maxArea = (o - i + 1) * (p - j + 1);
										a = o;
										b = p;
										x = c;
									}
								}
							}
						}
					}
				}
				fill(i, j, a, b, x);
				//cout<<"area: "<<maxArea<<endl;
				//cout<<"dir: "<<i<<" "<<j<<" to: "<<a<<" "<<b<<endl;
				//printt();
			}
		}
		cout << "Case #" << t << ":\n";
		for (int i = 0; i < n; ++i)
		{
			for (int j = 0; j < m; ++j)
			{
				cout << M[i][j];
			}
			cout << endl;
		}
	}
	return 0;
}
