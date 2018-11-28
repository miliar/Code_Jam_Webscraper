#include <bits/stdc++.h>

using namespace std;

#ifndef ONLINE_JUDGE
#define db(...) printf(__VA_ARGS__);
#else
#define db(...)
#endif

#define mp(x,y) make_pair(x,y)
#define For(i,n) for(int i = 0; i<n; ++i)

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<ll> vl;

int hd, ad, hk, ak, b, d;

int fun() {
    queue< int > qhd, qad, qhk, qak, qv;
    qhd.push(hd); qad.push(ad); qhk.push(hk); qak.push(ak); qv.push(0);
    map< tuple<int, int, int, int>, int > m;
    while (!qv.empty()) {
        int ahd, aad, ahk, aak, av;
        ahd = qhd.front(); qhd.pop();
        aad = qad.front(); qad.pop();
        ahk = qhk.front(); qhk.pop();
        aak = qak.front(); qak.pop();
        av = qv.front(); qv.pop();
        if (m.count(tie(ahd, aad, ahk, aak)) > 0) {
            continue;
        }
        m[tie(ahd, aad, ahk, aak)] = av;
        if (ahk <= 0) return av;
        if (ahd <= 0) continue;
        // attack
        qhd.push(ahd - aak);
        qad.push(aad);
        qhk.push(ahk-aad);
        qak.push(aak);
        qv.push(av+1);
        if (b > 0) {
            // buff
            qhd.push(ahd-aak);
            qad.push(aad+b);
            qhk.push(ahk);
            qak.push(aak);
            qv.push(av+1);
        }
        if (aak > 0) {
            // debuff
            if (d > 0) {
                int nbuf = max(aak-d, 0);
                qhd.push(ahd-nbuf);
                qad.push(aad);
                qhk.push(ahk);
                qak.push(nbuf);
                qv.push(av+1);
            }

            if (hd - aak > ahd - aak) {
                // cure
                qhd.push(hd-aak);
                qad.push(aad);
                qhk.push(ahk);
                qak.push(aak);
                qv.push(av+1);
            }
        }
    }
    return -47;
}

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t<=T; ++t) {
        scanf("%d %d %d %d %d %d", &hd, &ad, &hk, &ak, &b, &d);
        printf("Case #%d: ", t);
        int res = fun();
        if (res == -47) {
            printf("IMPOSSIBLE\n");
        } else {
            printf("%d\n", res);
        }
    }
    return 0;
}
