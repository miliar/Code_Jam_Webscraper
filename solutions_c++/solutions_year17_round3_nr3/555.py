#include <bits/stdc++.h>
#define MAX_N 100100
using namespace std;

#define ll long long
#define ull unsigned long long
#define ii pair<int,int>
#define iii pair<ii, int>

#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define ep emplace_back
#define sz(a) (int) a.size()
#define cl(a) a.clear()

#define vi vector<int>
#define vii vector<ii>

#define LOWBIT(x) ( (x) & -(x) )

#define FOR(x,a,b) for (int x=a;x<=b;x++)
#define FOD(x,a,b) for (int x=a;x>=b;x--)
#define REP(x,a,b) for (int x=a;x<b;x++)
#define RED(x,a,b) for (int x=a;x>b;x--)

const int MAX = 1e5 + 10;
const int MAXN = 1e4 + 10;
const int MOD = 1e9 + 7;
const int inf = 1e9;
const double pi = acos(-1.0);
const double eps = 1e-6;

int dx[] = {0 , -1 , 0 , 1};
int dy[] = {1 , 0 , -1 , 0};

int test;
double p[55];
int n , k;
double U;
bool mark[55];

int main() {
	ios::sync_with_stdio(false);
    cin.tie(0);

    freopen("input.txt", "r" , stdin);
    freopen("output.txt", "w" , stdout);

    cin >> test; int t = test;

    while (test--) {
        cout << "Case #" << t - test << ": ";

        cin >> n >> k;
        cin >> U;

        FOR(i , 1 , n) cin >> p[i];

        FOR(i , 1 , n) mark[i] = false;

        vector <pair <double , int> > V;

        FOR(i , 1 , n) V.pb(mp(p[i] , i));

        while (1) {
            bool check = true;

            double sum = 0.0;
            int N = 0;

            REP(i , 0 , V.size()) {
                double val = V[i].fi;
                int pos = V[i].se;

                if (!mark[pos]) sum += val , N++;
            }

            sum += U;
            double k = sum / (double) N;

            k = min(k , 1.0000);

            REP(i , 0 , V.size()) {
                double val = V[i].fi;
                int pos = V[i].se;

                if (mark[pos]) continue;

                if (k < val) {
                    mark[pos] = true;
                    check = false;
                }
            }

            if (!check) continue;

            REP(i , 0 , V.size()) {
                double val = V[i].fi;
                int pos = V[i].se;

                if (mark[pos]) continue;
                p[pos] = k;
            }

            break;
        }

        double res = 1.000;

        FOR(i , 1 , n) res *= p[i];

        cout << fixed << setprecision(20) << res << endl;
    }

	return 0;
}
