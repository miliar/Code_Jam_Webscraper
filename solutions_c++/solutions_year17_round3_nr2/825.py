#include <bits/stdc++.h>

using namespace std;

#ifndef ONLINE_JUDGE
#define db(...) printf(__VA_ARGS__);
#else
#define db(...)
#endif

#define mp(x,y) make_pair(x,y)
#define pb push_back
#define fst first
#define snd second
#define For(i,n) for(int i = 0; i<n; ++i)

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<ll> vl;

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t<=T; ++t) {
        printf("Case #%d: ", t);
        int ac, aj;
        scanf("%d %d", &ac, &aj);
        vector< pii > cam(ac), jam(aj);

        For(i,ac) scanf("%d %d", &cam[i].fst, &cam[i].snd);
        For(i,aj) scanf("%d %d", &jam[i].fst, &jam[i].snd);
        if (ac + aj == 1) {
            printf("2\n");
            continue;
        }
        if (ac == 1 && aj == 1) {
            printf("2\n");
            continue;
        }
        vector< pii > v;
        if (ac == 2) v = cam;
        else v = jam;
        sort(v.begin(), v.end());
        int u2 = v[0].snd - v[0].fst;
        int u4 = v[1].snd - v[1].fst;
        int u3 = v[1].fst - v[0].snd;
        if (u2+u3+u4 <= 720) {
            printf("2\n");
            continue;
        }
        if (720*2 - u3 <= 720) {
            printf("2\n");
            continue;
        }
        printf("4\n");
    }
    return 0;
}
