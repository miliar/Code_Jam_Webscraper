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
        int n, p;
        int res;
        cin >> n >> p;
        vi arr(n);
        rep(i,0,n) cin >> arr[i];

        if(p == 2)
        {
            int even = 0, odd = 0;
            rep(i,0,n)
            {
                if(arr[i]%2 == 0) even++;
                else odd++;
            }

            res = even + (odd+1)/2;
        }
        else if(p == 3)
        {
            vi cnt(3);
            rep(i,0,n) cnt[arr[i]%3]++;
            int tmp = min(cnt[1], cnt[2]);
            res = cnt[0] + tmp + (max(cnt[1],cnt[2])-tmp+2)/3;
        }
        else if(p == 4)
        {
            vi cnt(4);
            rep(i,0,n) cnt[arr[i]%4]++;

            res = cnt[0] + (cnt[2]+1)/2;
            if(cnt[2] % 2 == 0)
            {
                res += min(cnt[1], cnt[3]) + (abs(cnt[3]-cnt[1])+3)/4;
            }
            else
            {
                if (cnt[1] > cnt[3]) cnt[1] -= 2;
                else cnt[3] -= 2;
                res += min(cnt[1], cnt[3]) + (abs(cnt[3]-cnt[1])+3)/4;
            }
        }

        cout << "Case #" << t << ": " << res << endl;
    }
    return 0;
}
