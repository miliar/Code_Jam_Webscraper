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

int T, L;
uInt N;
string S;
int memo[20][12][2];
uInt dp[20][12][2];

uInt func(int pos, int last, int matching) {
    if (pos == L) {
        return 1;
    } else {
        if (memo[pos][last][matching] == -1) {
            uInt& ans = dp[pos][last][matching];

            ans = 0;
            
            for (int i = last; i <= 9; i++) {
                int digit_now = S[pos] - '0';                
                
                if (matching && i > digit_now) continue;
                
                ans += func(pos + 1, i, matching && i == digit_now);
            }            
        }
        
        return dp[pos][last][matching];
    }
}

int brute(uInt n) {
    int ans = 0;

    for (int i = 1; i <= (int) n; i++) {
        int x = i;
        bool valid = true;

        vector<int> vs;
        
        while (x > 0) {
            int now = x % 10;
            x /= 10;

            vs.push_back(now);
        }
        reverse(vs.begin(), vs.end());
        for (int i = 1; i < (int) vs.size(); i++) {
            if (vs[i] < vs[i - 1]) {
                valid = false;
                break;
            }
        }
        if (valid) {
            ans += 1;
        }
    }
    
    return ans;
}

int main(void) {
    cin >> T;

    for (int t = 1; t <= T; t++) {
        cin >> N;

        uInt l = 1, h = N, m = N;
        uInt ans = 1;
        
        /*
        for (int i = 1; i <= 130; i++) {
            memset(memo, -1, sizeof(memo));
            S = to_string(i);
            L = (int) S.size();
            
            uInt counted = func(0, 0, 1) - 1;
            
            cout << counted << " " << brute(i) << "\n";
        }
        */
        memset(memo, -1, sizeof(memo));
        S = to_string(N);
        L = (int) S.size();

        uInt counted = func(0, 0, 1) - 1;
        
        while (l <= h) {
            m = l + (h - l) / 2;
            
            memset(memo, -1, sizeof(memo));
            
            S = to_string(m);
            L = (int) S.size();
            
            uInt now = func(0, 0, 1) - 1;
            //cout << counted << " " << now << " => " << m << endl;
            if (now == counted) {
                ans = m;
                h = m - 1;
            } else if (now < counted) {
                l = m + 1;
            } else {
                h = m - 1;
            }
        }
        cout << "Case #" << t << ": ";
        cout << ans << "\n";
    }
    return 0;
}
