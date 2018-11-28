#include <bits/stdc++.h>
using namespace std;
template <class T> int size(const T &x) { return x.size(); }
#define rep(i,a,b) for (decltype(a) i=(a); i<(b); ++i)
#define iter(it,c) for (decltype((c).begin()) it = (c).begin(); it != (c).end(); ++it)
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef long long ll;
typedef unsigned long long ull;
const int INF = ~(1<<31);

const double EPS = 1e-9;
const double pi = acos(-1);
typedef unsigned long long ull;
typedef vector<vi> vvi;
typedef vector<vii> vvii;
template <class T> T smod(T a, T b) {
  return (a % b + b) % b; }

bool can[1450][2];
int mem[1450][1450][2][2];

int dp(int i, int j, int who, int start)
{
    if(i == 720 && j == 720) return who == start ? 0 : 1;
    if(i+j == 1440) return 2000;
    if(mem[i][j][who][start] == -1)
    {
        if(can[i+j][who])
        {
            if(who == 0)
            {
                mem[i][j][who][start] = min(dp(i+1, j, 0, start), dp(i, j+1, 1, start)+1);
            }
            else if(who == 1)
            {
                mem[i][j][who][start] = min(dp(i+1, j, 0, start) + 1, dp(i, j+1, 1, start));
            }
        }
        else
        {
            mem[i][j][who][start] = 2000;
        }
    }
    return mem[i][j][who][start];
}

int main()
{
    cin.sync_with_stdio(false);
    int T;
    cin >> T;
    rep(t,1,T+1)
    {
        memset(can, 1, sizeof(can));
        memset(mem, -1, sizeof(mem));
        int ac, aj;
        cin >> ac >> aj;
        int c, d, j, k;
        rep(i,0,ac)
        {
            cin >> c >> d;
            rep(b, c, d)
            {
                can[b][0] = false;
            }
        }
        rep(i,0,aj)
        {
            cin >> j >> k;
            rep(b,j,k)
            {
                can[b][1] = false;
            }
        }
        int res = min(dp(0,0,0,0), dp(0,0,1,1));
        cout << "Case #" << t << ": " << res << endl;
    }

    return 0;
}
