#include <cstdio>
#include <cstring>
#include <ctime>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <string>
#include <queue>
#include <map>
#include <stack>
#include <vector>
#include <algorithm>
#include <set>
#include <deque>
#include <utility>
#include <chrono>
#include <sstream>
#include <iomanip>
using namespace std;
#define MOD 1000000007
#define PI 3.14159265358979
#define rep(i, n) for (int (i) = 0; (i) < (int)(n); (i)++)
#define rer(i, l, r) for (int (i) = (int)(l); (i) <= (int)(r); (i)++)
#define reu(i, l, r) for (int (i) = (int)(l); (i) < (int)(r); (i)++)
#define each(i, v) for (auto i : v)
#define D(x) cout << x << endl
#define d(x) cout << x
#define all(x) (x).begin(), (x).end()
#define pub(x) push_back(x)
#define pob() pop_back()
#define puf(x) push_front(x)
#define pof() pop_front()
#define mp(x, y) make_pair((x), (y))
#define fi first
#define se second
#define setp(x) setprecision(x)
#define mset(m, v) memset(m, v, sizeof(m))
static const int INF = 0x3f3f3f3f;
static const long long INFL = 0x3f3f3f3f3f3f3f3fLL;
typedef long long ll;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<long long> vll;
typedef vector<string> vs;
typedef vector<bool> vb;
typedef pair<int, int> pii;
typedef pair<long, long> pll;
typedef vector<pii> vpii;
typedef vector<pll> vpll;
template<typename T, typename U> inline void amin(T &x, U y) { if (y < x) x = y; }
template<typename T, typename U> inline void amax(T &x, U y) { if (x < y) x = y; }

//static const int dx[] = {1, 0, -1, 0}, dy[] = {0, 1, 0, -1};
//#define int ll
void solve(int t) {
        int n;
        cin >> n;
        int R, O, Y, G, B, V;
        cin >> R >> O >> Y >> G >> B >> V;
        if (O > 0) {
                if (O * 2 > B) {
                        D("Case #" << t + 1 << ": IMPOSSIBLE");
                        return;
                }
                B -= O;
        }
        if (G > 0) {
                if (G * 2 > R) {
                        D("Case #" << t + 1 << ": IMPOSSIBLE");
                        return;
                }
                R -= O;
        }
        if (V > 0) {
                if (V * 2 > Y) {
                        D("Case #" << t + 1 << ": IMPOSSIBLE");
                        return;
                }
                Y -= O;
        }
        int m = max(B, max(R, Y));

        char mm;
        vector<char> tmp1, tmp2;
        if (B >= R && B >= Y) {
                mm = 'B';
                rep(i, Y) tmp1.pub('Y');
                rep(i, R) tmp2.pub('R');
        } else if (R >= B && R >= Y) {
                mm = 'R';
                rep(i, Y) tmp1.pub('Y');
                rep(i, B) tmp2.pub('B');
        } else if (Y >= B && Y >= R) {
                mm = 'Y';
                rep(i, B) tmp1.pub('B');
                rep(i, R) tmp2.pub('R');
        }
        
        if (m >= n / 2 + 1) {
                D("Case #" << t + 1 << ": IMPOSSIBLE");
                return;
        }

        vector<char> ans;

        int tp1 = 0, tp2 = 0;
        rep(i, n) {
                if (i % 2 == 0 && m > 0) {
                        if (mm == 'O' && O > 0) {
                                ans.pub('B');
                                ans.pub('O');
                                ans.pub('B');
                                O --;
                        } else if (mm == 'R' && G > 0) {
                                ans.pub('R');
                                ans.pub('G');
                                ans.pub('R');
                                G --;
                        } else if (mm == 'Y' && V > 0) {
                                ans.pub('Y');
                                ans.pub('V');
                                ans.pub('Y');
                                V --;
                        }
                        ans.pub(mm);
                        m --;
                } else {
                        if (tmp1.size() - tp1 < tmp2.size() - tp2) {
                                if (tmp2[tp2] == 'B' && O > 0) {
                                        ans.pub('B');
                                        ans.pub('O');
                                        ans.pub('B');
                                        O --;
                                } else if (tmp2[tp2] == 'R' && G > 0) {
                                        ans.pub('R');
                                        ans.pub('G');
                                        ans.pub('R');
                                        G --;
                                } else if (tmp2[tp2] == 'Y' && V > 0) {
                                        ans.pub('Y');
                                        ans.pub('V');
                                        ans.pub('Y');
                                        V --;
                                } else {
                                        ans.pub(tmp2[tp2]);
                                }
                                tp2 ++;
                        } else {
                                if (tmp1[tp1] == 'B' && O > 0) {
                                        ans.pub('B');
                                        ans.pub('O');
                                        ans.pub('B');
                                        O --;
                                } else if (tmp1[tp1] == 'R' && G > 0) {
                                        ans.pub('R');
                                        ans.pub('G');
                                        ans.pub('R');
                                        G --;
                                } else if (tmp1[tp1] == 'Y' && V > 0) {
                                        ans.pub('Y');
                                        ans.pub('V');
                                        ans.pub('Y');
                                        V --;
                                } else {
                                        ans.pub(tmp1[tp1]);
                                }
                                tp1 ++;
                        }
                }
        }

        d("Case #" << t + 1 << ": ");
        rep(i, n) {
                d(ans[i]);
        }
        D("");
}

int main() { 
        int t;
        cin >> t;
        rep(i, t) {
                solve(i);
        }
        return 0;
}

