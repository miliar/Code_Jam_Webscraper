#include <cstdio>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <vector>
#include <cstring>
#include <map>
#include <set>
#include <unordered_map>
#include <queue>
#include <sstream>
#include <iomanip>
using namespace std;

//#pragma comment(linker, "/STACK:102400000,102400000")

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<int, double> pid;
typedef pair<ll, ll> pll;

const double PI = acos(-1.);

vector<pair<double, double> > arr;

int N, K;

void solve() {
    cin >> N >> K;
    arr.clear();
    
    for (int i = 0; i < N; ++i) {
        double x, y;
        cin >> x >> y;
        arr.push_back(make_pair(x, y));
    }
    
    double ans = 0;
    
    for (int i = 0; i < N; ++i) {
        double now = arr[i].first * arr[i].first + 2.0 * arr[i].first * arr[i].second;
        vector<double> tmp;
        for (int j = 0; j < N; ++j) {
            if (i == j) continue;
            tmp.push_back(2.0*arr[j].first*arr[j].second);
        }
        if (tmp.size() < K-1)   continue;
        sort(tmp.begin(), tmp.end());
        reverse(tmp.begin(), tmp.end());
        for (int j = 0; j+1 < K; ++j) {
            now += tmp[j];
        }
        if (now > ans) {
            ans = now;
        }
    }
    
    printf("%.10lf\n", ans*PI);
}

int main() {
    
    //freopen("/Users/zyeric/Desktop/workspace/workspace/in.txt", "r", stdin);
    
    ios::sync_with_stdio(false);
    cout << fixed << setprecision(16);
    
    int T;
    cin >> T;
    
    for (int kase = 1; kase <= T; ++ kase) {
        cout << "Case #" << kase << ": ";
        solve();
        cerr << "solved " << kase << endl;
    }
    
    return 0;
}
