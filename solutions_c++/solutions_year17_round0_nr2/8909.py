#include <bits/stdc++.h>

template<typename T> T gcd(T a, T b) {
    if(!b) return a;
    return gcd(b, a % b);
}
template<typename T> T lcm(T a, T b) {
    return a * b / gcd(a, b);
}

template<typename T> void chmin(T& a, T b) { a = (a > b) ? b : a; }
template<typename T> void chmax(T& a, T b) { a = (a < b) ? b : a; }
int in() { int x; scanf("%d", &x); return x; }

using namespace std;

typedef long long Int;
typedef unsigned long long uInt;
typedef unsigned uint;

int T, N;

bool check(int x) {
    int ant = x % 10;
    x /= 10;
    while(x) {
        int m = x % 10;
        if(m > ant) return false;
        x /= 10;
        ant = m;
    }
    return true;
}

int main(void) {

    cin >> T;

    for(int t=1; t<=T; t++) {
        cin >> N;

        int ans;
        for(ans=N; ans>=0; --ans) {
            if(check(ans)) break;
        }
        cout << "Case #" << t << ": " << ans << "\n";
    }

    return 0;
}
