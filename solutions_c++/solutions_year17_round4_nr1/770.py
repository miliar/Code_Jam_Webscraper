#include <bits/stdc++.h>

using namespace std;

template<typename T>
void sci(T &t) {
    cin >> t;
}

template<typename T, typename... Ts>
void sci(T &t, Ts &... ts) {
    sci(t);
    sci(ts...);
}

#define scid(vars...) int vars; sci(vars)
#define scidl(vars...) lint vars; sci(vars)
#define scidd(vars...) double vars; sci(vars)
#define scids(vars...) string vars; sci(vars)

template<typename T, typename Cmp=std::greater<T>>
using heap = priority_queue<T, std::vector<T>, Cmp>;

typedef long long lint;

int d2[2][111][111];
int d3[3][111][111][111];
//int d4[4][111][111][111][111];
int cnt[4];

void solve2(int n) {
    int p = 2;
    for (int i = 0; i < n; i++) {
        scid(x);
        cnt[x % p]++;
    }
//    cout << cnt[0] + (cnt[1] + 1) / 2 << "\n";
    for (int i0 = 0; i0 < 111; i0++) {
        for (int i1 = 0; i1 < 111; i1++) {
            for (int l = 0; l < p; l++) {
                int c = l == 0;
                d2[l][i0][i1] = 0;
                if (i0 > 0) {
                    d2[l][i0][i1] = max(d2[l][i0][i1], d2[l][i0 - 1][i1] + c);
                }
                if (i1 > 0) {
                    d2[l][i0][i1] = max(d2[l][i0][i1], d2[(l - 1 + p) % p][i0][i1 - 1] + c);
                }
            }
        }
    }
    cout << d2[0][cnt[0]][cnt[1]] << "\n";
}

void solve3(int n) {
    int p = 3;
    for (int i = 0; i < n; i++) {
        scid(x);
        cnt[x % p]++;
    }
    for (int i0 = 0; i0 < 111; i0++) {
        for (int i1 = 0; i1 < 111; i1++) {
            for (int i2 = 0; i2 < 111; i2++) {
                for (int l = 0; l < p; l++) {
                    int c = l == 0;
                    d3[l][i0][i1][i2] = 0;
                    if (i0 > 0) {
                        d3[l][i0][i1][i2] = max(d3[l][i0][i1][i2], d3[l][i0 - 1][i1][i2] + c);
                    }
                    if (i1 > 0) {
                        d3[l][i0][i1][i2] = max(d3[l][i0][i1][i2], d3[(l - 1 + p) % p][i0][i1 - 1][i2] + c);
                    }
                    if (i2 > 0) {
                        d3[l][i0][i1][i2] = max(d3[l][i0][i1][i2], d3[(l - 2 + p) % p][i0][i1][i2 - 1] + c);
                    }
                }
            }
        }
    }
//    for (int l = 0; l < p; l++) {
//        for (int i0 = 0; i0 < 2; i0++) {
//            for (int i1 = 0; i1 < 3; i1++) {
//                for (int i2 = 0; i2 < 2; i2++) {
//                    printf("%d %d %d %d: %d\n", l, i0, i1, i2, d3[l][i0][i1][i2]);
//                }
//            }
//        }
//    }
    cout << d3[0][cnt[0]][cnt[1]][cnt[2]] << "\n";
}

//void solve4(int n) {
//    int p = 4;
//    for (int i = 0; i < n; i++) {
//        scid(x);
//        cnt[x % p]++;
//    }
//    for (int l = 0; l < p; l++) {
//        int c = l == 0;
//        for (int i0 = 0; i0 < 111; i0++) {
//            for (int i1 = 0; i1 < 111; i1++) {
//                for (int i2 = 0; i2 < 111; i2++) {
//                    for (int i3 = 0; i3 < 111; i3++) {
//                        d4[l][i0][i1][i2][i3] = 0;
//                        if (i0 > 0) {
//                            d4[l][i0][i1][i2][i3] = max(d4[l][i0][i1][i2][i3], d4[l][i0 - 1][i1][i2][i3] + c);
//                        }
//                        if (i1 > 0) {
//                            d4[l][i0][i1][i2][i3] = max(d4[l][i0][i1][i2][i3], d4[(l - 1 + p) % p][i0][i1 - 1][i2][i3] + c);
//                        }
//                        if (i2 > 0) {
//                            d4[l][i0][i1][i2][i3] = max(d4[l][i0][i1][i2][i3], d4[(l - 2 + p) % p][i0][i1][i2 - 1][i3] + c);
//                        }
//                        if (i3 > 0) {
//                            d4[l][i0][i1][i2][i3] = max(d4[l][i0][i1][i2][i3], d4[(l - 1 + p) % p][i0][i1][i2][i3 - 1] + c);
//                        }
//                    }
//                }
//            }
//        }
//    }
//    cout << d4[0][cnt[0]][cnt[1]][cnt[2]][cnt[3]] << "\n";
//}

void solve() {
    scid(n, p);
    memset(cnt, 0, sizeof(cnt));
    if (p == 2) {
        solve2(n);
    } else if (p == 3) {
        solve3(n);
    } else if (p == 4) {
        assert(false);
//        solve4(n);
    }
}

int main() {
#ifdef TOXA31
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    scid(t);
    for (int it = 1; it <= t; ++it) {
        cout << "Case #" << it << ": ";
        solve();
    }


    return 0;
}