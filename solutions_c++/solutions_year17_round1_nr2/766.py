#include <bits/stdc++.h>
using namespace std;
char enl = '\n';
#define rep(i, from, to) for (int i = from; i < (to); ++i)
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<pair<int, int>> vii;

long double epsilon = 0.0000000001;

int most(int q, int r) {

    long double rr = (long double)r;
    long double qq = (long double)q;
    long double ni = 0.9;
    rr = ni * rr;
    int lb = 1;
    int ub = 1e7;
    if (rr > qq + epsilon) return 0;
    while (ub != lb + 1) {
        int mid = (lb + ub) / 2;
        if (((long double)mid) * rr > qq + epsilon) {
            //cout << "qq: " << qq << " mr: " << ((long double)mid*rr) << endl;
            ub = mid;
        } else {
            lb = mid;
        }
    }
    return lb;
}

int least(int q, int r) {
    long double rr = (long double)r;
    long double qq = (long double)q;
    long double ni = 1.1;
    rr = ni * rr;
    int lb = 0;
    int ub = 1e7;
    while (ub != lb + 1) {
        int mid = (lb + ub) / 2;
        if (((long double)mid) * rr > qq - epsilon) {
            //cout << "qq: " << qq << " mr: " << ((long double)mid*rr) << endl;
            ub = mid;
        } else {
            lb = mid;
        }
    }
    return ub;

}


void solve() {

    int n, p;
    cin >> n >> p;

    vi r(n);
    rep(i,0,n)
        cin >> r[i];
    vector<vi> q(n, vi(p));
    rep(i,0,n) {
        rep(j,0,p) {
            cin >> q[i][j];
        }
        sort(q[i].begin(), q[i].end());
    }

    vector<int> index(n);

    vector<vector<ii>> rg(n, vector<ii>(p));
    rep(i,0,n) {
        rep(j,0,p) {
            rg[i][j] = make_pair(least(q[i][j], r[i]), most(q[i][j], r[i]));
            //cout << "range for " << i << " pr " << j << ": " << rg[i][j].first << ", " << rg[i][j].second << endl;
        }
    }
    // check least <= most!!!

    int con = 0;
    bool br = false;
    while (true) {
        rep(i,0,n) {
            if (index[i] >= p) {
                br = true;
                break;
            }
            while (rg[i][index[i]].first > rg[i][index[i]].second) {
                index[i]++;
                if (index[i] >= p) break;
            }
            if (index[i] >= p) br = true;
        }
        if (br) break;
        int maxmin = rg[0][index[0]].first;
        int minmax = rg[0][index[0]].second;
        int minmaxdex = 0;
        rep(i,0,n) {
            if (rg[i][index[i]].first > maxmin) maxmin = rg[i][index[i]].first;
            if (rg[i][index[i]].second < minmax) {
                minmax = rg[i][index[i]].second;
                minmaxdex = i;
            }
        }
        if (maxmin > minmax) {
            index[minmaxdex]++;
        } else {
            rep(i,0,n) {
                index[i]++;
            }
            con++;
        }
    }

    cout << con << endl;








}

    
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin.exceptions(cin.failbit);

    int t;
    cin >> t;
    rep(i,0,t) {
        cout << "Case #" << (i+1) << ": ";
        solve();
    }


    return 0;
}
