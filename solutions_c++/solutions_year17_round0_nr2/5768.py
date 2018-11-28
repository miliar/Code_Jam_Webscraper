#include <bits/stdc++.h>
#define ll long long
using namespace std;

int T, N;
char NUM[25];

bool ended;
stack <int> ldu; // Last digit used
ll acum, resGen;

void gen(int i) {
    if(i == N) {
        if(!ended) {
            printf("%lld\n", resGen);
            ended = true;
        }
        return;
    }

    acum = acum * 10 + (NUM[i] - '0');

    for(int k = 9; k >= 0 && !ended; k--){
        if(k >= ldu.top()) {
            resGen = resGen * 10 + k;
            if(resGen <= acum) {
                ldu.push(k);

                gen(i+1);

                ldu.pop();
            }
            resGen /= 10;
        } else {
            acum /= 10;
            return;
        }
    }
}

void solve() {
    ldu = stack <int> ();
    ldu.push(0);

    N = strlen(NUM);
    ended = acum = resGen = 0;

    gen(0);
}

int main() {
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);

    scanf("%d", &T);

    for(int cs = 1; cs <= T; cs++) {
        scanf("%s", NUM);

        printf("Case #%d: ", cs);
        solve();
    }

    return 0;
}
