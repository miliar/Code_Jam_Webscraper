#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef std::pair<int, int> ii;

char reverse(char x) {
    if (x == '+')
        return '-';
    else
        return '+';
}

void run(const int testcase) {
    string s;
    cin>>s;
    int k;
    cin>>k;
    int n = s.size();
    int steps = 0;
    for (int i = 0; i < n; ++i) {
        if (s[i] == '-') {
            ++steps;
            const int last = i+k-1;
            if (last >= n) {
                steps = -1;
                break;
            }
            for (int j = i; j <= last; ++j)
                s[j] = reverse(s[j]);
        }
    }
    printf("Case #%d: ", testcase);
    if (steps == -1) {
        puts("IMPOSSIBLE");
    } else {
        printf("%d\n", steps);
    }
}

int32_t main() {
    int testcases;
    cin>>testcases;
    for (int testcase = 1; testcase <= testcases; ++testcase) {
        run(testcase);
    }
}
