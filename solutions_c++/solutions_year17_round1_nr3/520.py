#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <tuple>
#include <unordered_set>
#include <set>

using namespace std;

int solve(int Hd, int Ad, int Hk, int Ak, int B, int D) {
    set<vector<int>> s;
    priority_queue<tuple<int, int, int, int, int>> q;

    q.push(make_tuple(0, -Hk, -Hd, -Ak, -Ad));

    while (!q.empty()) {
        auto c = q.top();
        q.pop();

        int turn = -get<0>(c);
        int hk = -get<1>(c);
        int hd = -get<2>(c);
        int ak = -get<3>(c);
        int ad = -get<4>(c);

//        printf("Hd(%d), Ad(%d), Hk(%d), Ak(%d)\n", hd, ad, hk, ak);

        if (s.find({hk, hd, ak, ad}) != s.end())
            continue;

        s.insert({hk, hd, ak, ad});

        if (hk <= 0)
            return turn;
        if (hd <= 0)
            continue;

        q.push(make_tuple(-1 * (turn+1), -(hk - ad), -(hd - ak), -ak, -ad));
        q.push(make_tuple(-1 * (turn+1), -(hk), -(hd - ak), -ak, -(ad+B)));
        q.push(make_tuple(-1 * (turn+1), -(hk), -(Hd - ak), -ak, -ad));

        ak = max(ak - D, 0);
        q.push(make_tuple(-1 * (turn+1), -(hk), -(hd - ak), -ak, -ad));
    }

    return -1;
}

int main() {
    int T;
    cin >> T;
    for (int kase = 1; kase <= T; ++kase) {
        int hd, ad, hk, ak, b, d;
        cin >> hd >> ad >> hk >> ak >> b >> d;

        int ret = solve(hd, ad, hk, ak, b, d);

        printf("Case #%d: %s\n", kase, ret > 0 ? to_string(ret).data() : "IMPOSSIBLE");
    }

    return 0;
}
