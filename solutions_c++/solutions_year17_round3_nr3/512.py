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

int N, K;
double U;

void solve() {
    cin >> N >> K;
    
    cin >> U;
    
    double ans = 1.0;
    
    vector<double> arr;
    
    for (int i = 0; i < N; ++i) {
        double p;
        cin >> p;
        arr.push_back(p);
    }
    
    sort(arr.begin(), arr.end());
    
    if (arr.back() == 0) {
        for (int i = 0; i < N; ++i) {
            ans = ans * U / N;
        }
    } else {
        double sum = 0;
        for (int i = 0; i < N; ++i) {
            sum += arr[i];
            if (i == N - 1) {
                for (int j = 0; j < N; ++j) {
                    ans = ans * (U + sum) / N;
                }
                break;
            } else {
                if ((i+1) * arr[i+1] - sum >= U) {
                    for (int j = 0; j <= i; ++ j) {
                        ans = ans * (sum + U) / (i+1);
                    }
                    for (int j = i+1; j < N; ++j) {
                        ans = ans * arr[j];
                    }
                    break;
                } else {
                    continue;
                }
            }
        }
    }
    
    printf("%.10lf\n", ans);
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
