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

const int MAX = 111;

int N, P;
int G[MAX];

void gao2() {
    int sum = 0;
    int cnt = 0;
    for (int i = 0; i < N; ++i) {
        if (G[i] & 1) {
            cnt ++;
        } else {
            sum ++;
        }
    }
    
    if (cnt & 1) {
        sum += (cnt+1)/2;
    } else {
        sum += cnt / 2;
    }
    
    printf("%d\n", sum);
}

void gao3() {
    
    int sum = 0;
    int cnt1 = 0;
    int cnt2 = 0;
    
    for (int i = 0; i < N; ++i) {
        if (G[i] % 3 == 0) {
            sum ++;
        } else if (G[i] % 3 == 1) {
            cnt1 ++;
        } else {
            cnt2 ++;
        }
    }
    
    sum += min(cnt1, cnt2);
    
    int tmp = max(cnt1, cnt2) - min(cnt1, cnt2);
    
    if (tmp % 3 == 0) {
        sum += tmp / 3;
    } else {
        sum += tmp / 3 + 1;
    }
    
    printf("%d\n", sum);
}

void solve() {
    scanf("%d%d", &N, &P);
    
    for (int i = 0; i < N; ++i) {
        scanf("%d", G+i);
    }
    
    if (P == 2) {
        gao2();
        return;
    }
    
    if (P == 3) {
        gao3();
        return;
    }
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
