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

const int MAX = 1444;
const int INF = 2222222;

int f[1444][777][2];

int N, M;

vector<pair<pair<int, int>, int> > arr;

void solve() {
    cin >> N >> M;
    arr.clear();
    
    for (int i = 0; i < N; ++i) {
        int s, t;
        cin >> s >> t;
        arr.push_back(make_pair(make_pair(s, t), 0));
    }
    
    for (int i = 0; i < M; ++i) {
        int s, t;
        cin >> s >> t;
        arr.push_back(make_pair(make_pair(s, t), 1));
    }
    
    sort(arr.begin(), arr.end());
    
    // 0 first
    
    int ans = 0;
    
    {
        int ind = 0;
        int s = arr[0].first.first, t = arr[0].first.second;
        int b = arr[0].second;
        
        for (int i = 0; i <= 1440; ++i) {
            for (int j = 0; j <= 720; ++j) {
                for (int k = 0; k < 2; ++k) {
                    f[i][j][k] = INF;
                }
            }
        }
        
        f[0][0][0] = 0;
        
        for (int i = 0; i <= 1440; ++i) {
            for (int j = 0; j <= min(i, 720); ++j) {
                for (int k = 0; k < 2; ++k) {
                    if (f[i][j][k] == INF)  continue;
                    
                    if (i == s) {
                        if (k == b) {
                            f[t][j][1^k] = f[i][j][k] + 1;
                        } else {
                            f[t][j+t-s][k] = f[i][j][k];
                        }
                        ind ++;
                        if (ind < N+M) {
                            s = arr[ind].first.first, t = arr[ind].first.second;
                            b = arr[ind].second;
                        }
                    } else {
                        if (j == 720) {
                            if (k == 0) {
                                f[i+1][j][1] = min(f[i][j][0] + 1, f[i+1][j][1]);
                            } else {
                                f[i+1][j][1] = min(f[i][j][1],f[i+1][j][1]);
                            }
                        } else {
                            if (k == 0) {
                                f[i+1][j+1][0] = min(f[i][j][0], f[i+1][j+1][0]);
                                f[i+1][j][1] = min(f[i][j][0]+1, f[i+1][j][1]);
                            } else {
                                f[i+1][j+1][0] = min(f[i][j][1]+1, f[i+1][j+1][0]);
                                f[i+1][j][1] = min(f[i][j][1], f[i+1][j][1]);
                            }
                        }
                    }
                }
                
            }
        }
        
        ans = min(f[1440][720][0], f[1440][720][1]+1);
    }
    
    {
        int ind = 0;
        int s = arr[0].first.first, t = arr[0].first.second;
        int b = arr[0].second;
        
        for (int i = 0; i <= 1440; ++i) {
            for (int j = 0; j <= 720; ++j) {
                for (int k = 0; k < 2; ++k) {
                    f[i][j][k] = INF;
                }
            }
        }
        
        f[0][0][1] = 0;
        
        for (int i = 0; i <= 1440; ++i) {
            for (int j = 0; j <= min(i, 720); ++j) {
                for (int k = 0; k < 2; ++k) {
                    if (f[i][j][k] == INF)  continue;
                    
                    if (i == s) {
                        if (k == b) {
                            f[t][j][1^k] = f[i][j][k] + 1;
                        } else {
                            f[t][j+t-s][k] = f[i][j][k];
                        }
                        ind ++;
                        if (ind < N+M) {
                            s = arr[ind].first.first, t = arr[ind].first.second;
                            b = arr[ind].second;
                        }
                    } else {
                        if (j == 720) {
                            if (k == 0) {
                                f[i+1][j][1] = min(f[i][j][0] + 1, f[i+1][j][1]);
                            } else {
                                f[i+1][j][1] = min(f[i][j][1],f[i+1][j][1]);
                            }
                        } else {
                            if (k == 0) {
                                f[i+1][j+1][0] = min(f[i][j][0], f[i+1][j+1][0]);
                                f[i+1][j][1] = min(f[i][j][0]+1, f[i+1][j][1]);
                            } else {
                                f[i+1][j+1][0] = min(f[i][j][1]+1, f[i+1][j+1][0]);
                                f[i+1][j][1] = min(f[i][j][1], f[i+1][j][1]);
                            }
                        }
                    }
                }
                
            }
        }
        
        ans = min(f[1440][720][1], f[1440][720][0]+1);
    }
    printf("%d\n", ans);
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
