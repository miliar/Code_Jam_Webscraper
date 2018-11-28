#include <algorithm>
#include <iostream>
#include <cstdio>
#include <map>
#include <numeric>
#include <cmath>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <complex>
#include <string.h>
#include <unordered_set>
#include <unordered_map>
#include <bitset>
#include <iomanip>
#include <sys/time.h>
#include <tuple>
#include <random>
using namespace std;

#define endl '\n'
#define ALL(v) (v).begin(), (v).end()
#define RALL(v) (v).rbegin(), (v).rend()
#define UNIQ(v) (v).erase(unique((v).begin(), (v).end()), (v).end())

typedef long long ll;
typedef long double ld;
typedef pair<int, char> P;
typedef pair<P, string> PP;
typedef complex<double> comp;
typedef vector< vector<ld> > matrix;
struct pairhash {
public:
    template<typename T, typename U>
    size_t operator()(const pair<T, U> &x) const {
	size_t seed = hash<T>()(x.first);
	return hash<U>()(x.second) + 0x9e3779b9 + (seed<<6) + (seed>>2);
    }
};
const int inf = 1e9 + 9;
const ll mod = 1e9 + 7;
const double eps = 1e-8;
const double pi = acos(-1);
const string yes = "YES", no = "NO";

int n;
int m[6];
const char c[6] = {'R', 'O', 'Y', 'G', 'B', 'V'};


string solve() {
    vector<PP> vec;
    for (int i = 0; i < 6; i+=2) {
        int j = (i + 3) % 6;
        if (m[i] < m[j]) return "IMPOSSIBLE";
        if (m[i] == m[j] && m[i] > 0) {
            if (n == m[i] + m[j]) {
                stringstream res;
                for (int k = 0; k < m[i]; k++) res << c[i] << c[j];
                return res.str();
            } else {
                return "IMPOSSIBLE";
            }
        }
        stringstream ss;
        for (int k = 0; k < m[j]; k++) ss << c[i] << c[j];
        ss << c[i];
        P p = make_pair(m[i]-m[j], c[i]);
        vec.push_back(make_pair(p, ss.str()));
    }
    sort(ALL(vec));
    int rem = vec[0].first.first + vec[1].first.first;
    if (vec[2].first.first > rem) return "IMPOSSIBLE";

    int t = vec[2].first.first - vec[1].first.first;
    int s = vec[0].first.first - t;
    stringstream res;
    for (int i = 0; i < s; i++) res << vec[2].first.second << vec[1].first.second << vec[0].first.second;
    for (int i = 0; i < vec[1].first.first - s; i++) res << vec[2].first.second << vec[1].first.second;
    for (int i = 0; i < t; i++) res << vec[2].first.second << vec[0].first.second;

    bool used[3];
    memset(used, false, sizeof(used));
    string ress = res.str();
    stringstream rres;
    for (int i = 0; i < ress.size(); i++) {
        bool f = false;
        for (int j = 0; j < 3; j++) {
            if (ress[i] == vec[j].first.second && !used[j]) {
                rres << vec[j].second;
                used[j] = true;
                f = true;
            }
        }
        if (!f) {
            rres << ress[i];
        }
    }
    return rres.str();
}

void input() {
    cin >> n;
    for (int i = 0; i < 6; i++) cin >> m[i];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout << fixed << setprecision(15);

    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        input();
	cout << "Case #" << i << ": " << solve() << endl;
    }
}
