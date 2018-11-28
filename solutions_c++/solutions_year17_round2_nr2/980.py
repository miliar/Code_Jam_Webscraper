#include<bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for(int i=a;i<b;i++)




int N, R, O, Y, G, B, V;
//-----------------------------------------------------------------------------------
pair<int, string> cnt[3];
string sol() {
    cnt[0] = { R, "R" };
    cnt[1] = { Y, "Y" };
    cnt[2] = { B,"B" };
    sort(cnt, cnt + 3);

    int ma = max(R, max(Y, B));
    int mi = min(R, min(Y, B));
    int md = R + Y + B - ma - mi;

    if (ma == md) {
        string res = "";
        rep(i, 0, ma) {
            res = res + cnt[1].second;
            res = res + cnt[2].second;
            if (0 < mi) res = res + cnt[0].second, mi--;
        }
        return res;
    }

    if (mi < ma - md) return "IMPOSSIBLE";

    string res = "";
    rep(i, 0, ma) {
        res += cnt[2].second;
        if (0 < md) res += cnt[1].second, md--;
        else if (0 < mi) res += cnt[0].second, mi--;
    }

    string res2 = "";
    rep(i, 0, res.size() - 1) {
        if (res[i] != cnt[0].second[0] && res[i + 1] != cnt[0].second[0] && 0 < mi) {
            res2 += res[i];
            res2 += cnt[0].second;
            res2 += res[i + 1];
            i++; mi--;
        }
        else res2 += res[i];
    }

    if (res[res.size() - 1] != res2[res2.size() - 1]) res2 += res[res.size() - 1];
    return res2;
}
//-----------------------------------------------------------------------------------
int main() {
    cin.tie(0);
    ios::sync_with_stdio(false);

    int T; cin >> T;
    rep(t, 1, T + 1) {
        cin >> N >> R >> O >> Y >> G >> B >> V;
        printf("Case #%d: %s\n", t, sol().c_str());
        fprintf(stderr, "Finish : %d\n", t);
    }
}