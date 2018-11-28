#include <bits/stdc++.h>
using namespace std;
template <class T> int size(const T &x) { return x.size(); }
#define rep(i,a,b) for (decltype(a) i=(a); i<(b); ++i)
#define iter(it,c) for (decltype((c).begin()) \
  it = (c).begin(); it != (c).end(); ++it)
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef long long ll;
const int INF = ~(1<<31);

const double EPS = 1e-9;
const double pi = acos(-1);
typedef unsigned long long ull;
typedef vector<vi> vvi;
typedef vector<vii> vvii;
template <class T> T smod(T a, T b) {
  return (a % b + b) % b; }

int main()
{
    int T;
    cin >> T;
    rep(t,1,T+1)
    {
        int r,c;
        cin >> r >> c;
        vector<string> grid(r);
        queue<ii> q;
        vector<bool> rem(r);
        rep(i,0,r)
        {
            cin >> grid[i];
            char cur = '?';
            rep(j,0,c)
            {
                if(grid[i][j] == '?')
                {
                    q.push(ii(i,j));
                }
                else
                {
                    cur = grid[i][j];
                    while(!q.empty())
                    {
                        ii p = q.front(); q.pop();
                        grid[p.first][p.second] = cur;
                    }
                }
            }
            if(cur != '?')
            {
                while(!q.empty())
                {
                    ii p = q.front(); q.pop();
                    grid[p.first][p.second] = cur;
                }
            }
            else
            {
                while(!q.empty()) q.pop();
                rem[i] = true;
            }
        }

        while(true)
        {
            bool flag = true;
            rep(i,0,r)
            {
                if(rem[i]) flag = false;
                if(i > 0 && rem[i] && !rem[i-1])
                {
                    rep(j,0,c)
                    {
                        grid[i][j] = grid[i-1][j];
                    }
                    rem[i] = false;
                    continue;
                }
                if(i < r-1 && rem[i] && !rem[i+1])
                {
                    rep(j,0,c)
                    {
                        grid[i][j] = grid[i+1][j];
                    }
                    rem[i] = false;
                }
            }
            if(flag) break;
        }

        cout << "Case #" << t << ":" << endl;
        rep(i,0,r)
        {
            rep(j,0,c)
            {
                cout << grid[i][j];
            }
            cout << endl;
        }
    }
    return 0;
}
