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

int N, R, O, Y, G, B, V;



void solve() {
    cin >> N >> R >> O >> Y >> G >> B >> V;
    
    vector<pair<int, char> > arr;
    
    arr.push_back(make_pair(R, 'R'));
    arr.push_back(make_pair(B, 'B'));
    arr.push_back(make_pair(Y, 'Y'));
    
    sort(arr.begin(), arr.end());
    
    reverse(arr.begin(), arr.end());
    
    int X = arr[0].first;
    int Y = arr[1].first;
    int Z = arr[2].first;
    
    if (Y == 0 && Z == 0) {
        printf("IMPOSSIBLE\n");
        return;
    }
    
    if (Z == 0) {
        if (X != Y) {
            printf("IMPOSSIBLE\n");
            return;
        }
        
        for (int i = 0; i < X; ++i) {
            printf("%c%c", arr[0].second, arr[1].second);
        }
        printf("\n");
        
        return;
    }
    
    if (X > Y+Z) {
        printf("IMPOSSIBLE\n");
        return;
    }
    
    int cnt = Z - (X-Y);
    
    for (int i = 0; i < cnt; ++i) {
        printf("%c%c%c", arr[0].second, arr[1].second, arr[2].second);
    }
    
    for (int i = cnt; i < Y; ++i) {
        printf("%c%c", arr[0].second, arr[1].second);
    }
    
    for (int i = 0; i < X-Y; ++i) {
        printf("%c%c", arr[0].second, arr[2].second);
    }
    
    printf("\n");
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
