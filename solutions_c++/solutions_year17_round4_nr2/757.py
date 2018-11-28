// three hidden code extras enter the website's html markup - one of them leaves (it up to you to find the others)
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <cstring>
#include <cassert>
using namespace std;
#define rep(i,a,n) for (int i=a;i<(int)(n);i++)
#define per(i,a,n) for (int i=(n)-1;i>=(int)(a);i--)
template<typename T> ostream& operator<<(ostream& s, vector<T> t) {rep(i, 0, t.size()) s << (i ? " " : "") << t[i]; return s;}
template<typename T> istream& operator>>(istream& s, vector<T> &t) {rep(i, 0, t.size()) s >> t[i]; return s;}
template<typename T, typename U> ostream& operator<<(ostream& s, pair<T, U> t) {s << "(" << t.first << "," << t.second << ")"; return s;}
template<typename T, typename U> istream& operator>>(istream& s, pair<T, U> &t) {s >> t.first >> t.second; return s;}
typedef long long ll;
const int N = 1111;

int cnt[2][N];

void solve() {
    memset(cnt, 0, sizeof(cnt));
    int n, c, m;
    cin >> n >> c >> m;
    assert(c == 2);
    vector<pair<int, int>> a(m);
    cin >> a;
    vector<int> customers = {0, 0};
    rep(i, 0, m) {
        cnt[a[i].second - 1][a[i].first - 1]++;
        customers[a[i].second - 1]++;
    }
    
    int r1 = 0, r2 = 0;
    /*cout << cnt[0][0] << " " << cnt[0][1] << endl;
    rep(i, 0, N) {
        while (cnt[0][i]) {
    
            int bi = -1;
            int bn = 0;
            rep(j, 0, N) {
                if (j != i && (min(cnt[0][j], cnt[1][j]) > bn)) {
                    bi = j;
                    bn = min(cnt[0][j], cnt[1][j]);
                }
            }
            if (bi == -1) {
                rep(j, 0, N) {
                    if (j != i && cnt[1][j] > bn) {
                        bi = j;
                        bn = cnt[1][j];
                    }
                }
            }
            cnt[0][i]--;
            r1++;
            if (bi != -1) {
                cnt[1][bi]--;
            } else {
                r2++;
            }
        }
    }
    rep(i, 0, N) {
        while (cnt[1][i]) {
            int bi = -1;
            int bn = 0;
            rep(j, 0, N) {
                if (j != i && min(cnt[0][j], cnt[1][j]) > bn) {
                    bi = j;
                    bn = min(cnt[0][j], cnt[1][j]);
                }
            }
            if (bi == -1) {
                rep(j, 0, N) {
                    if (j != i && cnt[0][j] > bn) {
                        bi = j;
                        bn = cnt[0][j];
                    }
                }
            }
            cnt[1][i]--;
            r1++;
            if (bi != -1) {
                cnt[0][bi]--;
            } else {
                r2++;
            }
        }
    }*/
    
    r1 = max(max(customers[0], customers[1]), cnt[0][0] + cnt[1][0]);
    rep(i, 0, N) {
        r2 = max(r2, cnt[0][i] + cnt[1][i] - r1);
    }
    cout << r1 << " " << r2;
}

int main() {
    ios_base::sync_with_stdio(false);
    int q;
    cin >> q;
    rep(i, 0, q) {
        cout << "Case #" << (i + 1) << ": ";
        solve();
        cout << endl;
    }
}
