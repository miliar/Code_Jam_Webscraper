#include<bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for(int i=a;i<b;i++)


int AC, AJ;
int C[101], D[101], J[101], K[101];
//-----------------------------------------------------------------------------------
typedef tuple<int, int, int> Node;
int imos[2020];
vector<Node> makepair() {
    vector<Node> res;
    rep(i, 0, 2020) imos[i] = 0;

    rep(i, 0, AC) imos[C[i]] += 1, imos[D[i]] += -1;
    rep(i, 0, AJ) imos[J[i]] += 2, imos[K[i]] += -2;

    rep(i, 1, 2020) imos[i] += imos[i - 1];

    int pre = imos[0], L = 0;
    rep(R, 1, 1440) {
        if (pre != imos[R]) {
            res.push_back({ L, R, pre });
            L = R; pre = imos[R];
        }
    }
    res.push_back({ L, 1440, pre });

    if (get<2>(res[0]) == get<2>(res[res.size() - 1])) {
        int i = res.size() - 1;
        int a, b, c;
        tie(a, b, c) = res[i];
        int aa, bb, cc;
        tie(aa, bb, cc) = res[0];
        res[i] = { a, bb + 1440, cc };
        res.erase(res.begin());
    }

    return res;
}
//-----------------------------------------------------------------------------------
void sol() {
    cin >> AC >> AJ;
    rep(i, 0, AC) scanf("%d%d", &C[i], &D[i]);
    rep(i, 0, AJ) scanf("%d%d", &J[i], &K[i]);

    auto v = makepair();
    int n = v.size();

    vector<int> no;
    int A = 0, B = 0;
    rep(i, 0, n) {
        auto t = v[i];
        int a, b, c;
        tie(a, b, c) = t;
        if (c == 0) no.push_back(i);
        else if (c == 1) A += b - a;
        else if (c == 2) B += b - a;
    }

    /*cout << endl;
    for (auto t : v) {
        int a, b, c;
        tie(a, b, c) = t;
        printf("[%d %d %d]\n", a, b, c);
    }*/

    sort(no.begin(), no.end(), [&](int a, int b) {
        return get<1>(v[a]) - get<0>(v[a]) < get<1>(v[b]) - get<0>(v[b]);
    });

    rep(_i, 0, no.size()) {
        int i = no[_i];

        int L = get<0>(v[i]);
        int R = get<1>(v[i]);

        int l = (i - 1 + n) % n;
        int r = (i + 1) % n;

        if (get<2>(v[l]) == get<2>(v[r])) {
            if (get<2>(v[l]) == 1) { // A
                if (R - L + A <= 720) {
                    A += R - L;
                    v[i] = { L, R, 1 };
                }
                else if (R - L + B <= 720) {
                    B += R - L;
                    v[i] = { L, R, 2 };
                }
                else {
                    v[i] = { L, R, 3 };
                }
            } else if (get<2>(v[l]) == 2) { // B
                if (R - L + B <= 720) {
                    B += R - L;
                    v[i] = { L, R, 2 };
                }
                else if(R - L + A <= 720) {
                    A += R - L;
                    v[i] = { L, R, 1 };
                }
                else v[i] = { L,R,3 };
            }
        }
    }

    /*cout << endl;
    for (auto t : v) {
        int a, b, c;
        tie(a, b, c) = t;
        printf("[%d %d %d]\n", a, b, c);
    }*/

    int ans = 0;
    int pre = get<2>(v[0]);
    rep(i, 1, n) {
        int t = get<2>(v[i]);
        if (t == pre) continue;
        if (t == 3) {
            ans++;
        }
        else if(t != 0) {
            ans++;
        }

        pre = t;
    }
    if (get<2>(v[0]) != 0) {
        if(get<2>(v[0]) != get<2>(v[n-1])) ans++;
    }
    printf("%d\n", ans);
}
//-----------------------------------------------------------------------------------
int main() {
    int T; cin >> T;
    rep(t, 0, T) {
        printf("Case #%d: ", t + 1);
        sol();
    }
}