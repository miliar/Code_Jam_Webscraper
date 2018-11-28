#include "bits/stdc++.h"

using namespace std;

#define fr first
#define sc second
#define mp make_pair
#define pb push_back

const int MAXN = 1005;

string solve(int * s, int slen, int k) {
    int answer = 0;
    for (int i = 0; i < slen; i++) {
        if (s[i] == 1) {
            continue;
        }
        if (i + k - 1 >= slen) {
            return "IMPOSSIBLE";
        }
        answer++;
        for (int j = i; j < i + k; j++) {
            s[j] = 1 - s[j];
        }
    }
    return to_string(answer);
}

int main() {
    #ifdef LOCAL_RUN
        freopen("Alg", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif

    int t;
    cin >> t;

    int lens;
    int s[MAXN];
    int k;
    string ss;

    for (int i = 0; i < t; i++) {
        cin >> ss >> k;
        lens = (int) ss.length();
        for (int j = 0; j < lens; j++) {
            s[j] = ss[j] == '+' ? 1 : 0;
        }
        cout << "Case #" << (i + 1) << ": " << solve(s, lens, k) << endl;
    }



    return 0;
}
