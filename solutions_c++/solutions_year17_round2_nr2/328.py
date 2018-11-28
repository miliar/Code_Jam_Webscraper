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

const int N = 1005;
int t,n,r,o,y,g,b,v,m,ans[N],mini;

int main()
{
	ios:: sync_with_stdio(false);
	freopen("B-small-attempt1.in","r",stdin);
	freopen("B-small-attempt1.out","w",stdout);
	cin >> t;
	for(int test = 1; test <= t; test++)
	{
		cin >> n >> r >> o >> y >> g >> b >> v;
		cout << "Case #" << test << ": ";
		/*if(o > 2 * b || g > 2 * r || v > 2 * y)
		{
			cout << "IMPOSSIBLE" << "\n";
			continue;
		}*/
		if(r > y + b || y > r + b || b > y + r)
		{
			cout << "IMPOSSIBLE" << "\n";
			continue;
		}
		m = max(r, max(y, b));
		if(r == m)
		{
			ans[0] = 0;
			r--;
		} else
		{
			if(y == m)
			{
				ans[0] = 1;
				y--;
			} else
			{
				ans[0] = 2;
				b--;
			}
		}
		for(int i = 1; i < n; i++)
		{
			int miniCnt = 0;
			m = max(r, max(y, b));
			mini = min(r, min(y,b));
			if(r == mini)
				miniCnt++;
			if(y == mini)
				miniCnt++;
			if(b == mini)
				miniCnt++;
			if(r == m && ans[0] == 0 && ans[i -1] != 0)
			{
				ans[i] = 0;
				r--;
				continue;
			}
			if(y == m && ans[0] == 1 && ans[i -1] != 1)
			{
				ans[i] = 1;
				y--;
				continue;
			}
			if(b == m && ans[0] == 2 && ans[i -1] != 2)
			{
				ans[i] = 2;
				b--;
				continue;
			}
			if(r == m && ans[i - 1] != 0)
			{
				ans[i] = 0;
				r--;
				continue;
			}
			if(y == m && ans[i -1] != 1)
			{
				ans[i] = 1;
				y--;
				continue;
			}
			if(b == m && ans[i-1] != 2)
			{
				ans[i] = 2;
				b--;
				continue;
			}
			if((r != mini || miniCnt == 2)&& ans[0] == 0 && ans[i -1] != 0)
			{
				ans[i] = 0;
				r--;
				continue;
			}
			if((y != mini || miniCnt == 2)&& ans[0] == 1 && ans[i -1] != 1)
			{
				ans[i] = 1;
				y--;
				continue;
			}
			if((b != mini || miniCnt == 2)&& ans[0] == 2 && ans[i -1] != 2)
			{
				ans[i] = 2;
				b--;
				continue;
			}
			if(ans[i - 1] != 0 && (r != mini || miniCnt == 2))
			{
				ans[i] = 0;
				r--;
				continue;
			}
			if(ans[i - 1] != 1 && (y != mini || miniCnt == 2))
			{
				ans[i] = 1;
				y--;
				continue;
			}
			ans[i] = 2;
			b--;
		}
		for(int i = 0; i < n;i++)
		{
			if(ans[i] == 0) cout << "R";
			if(ans[i] == 1) cout << "Y";
			if(ans[i] == 2) cout << "B";
		}
		cout << "\n";
	}
	return 0;
}
