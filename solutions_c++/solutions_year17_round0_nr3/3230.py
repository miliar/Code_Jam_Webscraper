#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef long double ld;
const double PI = acos(-1.);

void getTest(ll &N, ll &K) {
    cin >> N >> K;
    //N = rand() % 100 + 1;
    //K = rand() % N + 1;
    //cout << N << " " << K << endl;
    return;
}

vector<ll> brute(ll N, ll K) {
    ll resMin = N, resMax = N;
    priority_queue<ll> pq;
    pq.push(N);
    for (int i = 0; i < K; ++i) {
        ll best = pq.top();
        pq.pop();
        ll  mn = (best - 1) / 2,
            mx = best / 2;
        if (mn == resMin) {
            resMax = min(resMax, mx);
        }
        if (mn < resMin) {
            resMin = mn;
            resMax = mx;
        }
        pq.push(mn);
        pq.push(mx);
    }
    //cout << resMax << " " << resMin << endl;
    return {resMax, resMin};
}

void solve(ll N, ll K) {
    ll pow = 2;
    ll cnt1=1, cnt2=1;
    ll mn = (N - 1) / 2;
    ll mx = N / 2;
    --K;
    while (K > pow) {
        ll a = (mn - 1) / 2;
        ll b = mn / 2;
        ll c = (mx - 1) / 2;
        ll d = mx / 2;
        ll cntA = cnt1, cntB = cnt1, cntC = cnt2, cntD = cnt2;
        cnt1 = cntA;
        cnt2 = cntD;
        if (a == b) {
            cnt1 += cntB;
        }
        else {
            cnt2 += cntB;
        }
        if (c == d) {
            cnt2 += cntC;
        }
        else {
            cnt1 += cntC;
        }
        mn = a;
        mx = d;

        K -= pow;
        pow <<= 1;
    }

    if (K > 0 && K <=cnt2) {
        mn = (mx - 1) / 2;
        mx = mx / 2;
    }
    else if (K > 0) {
        mx = mn / 2;
        mn = (mn - 1) / 2;
    }
    cout << mx << " " << mn << endl;
    return;
}

int main() {
    freopen("/home/york_io/Documents/Code/contest/in.txt", "r", stdin);
    //freopen("/home/york_io/Documents/Code/contest/out.txt", "r", stdin);
    srand(time(nullptr));
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        ll N, K;
        getTest(N, K);
        cout << "Case #" << t << ": ";
        solve(N, K);
//        if (solve(N, K) != brute(N, K)) {
//            cout << "WA\n";
//            cout << N << " " << K << endl;
//            cout << brute(N, K)[0] << " " << brute(N, K)[1] << endl;
//            cout << solve(N, K)[0] << " " << solve(N, K)[1] << endl;
//            return 0;
//        }
//        cout << "OK " << t << endl;
    }
    return 0;
}