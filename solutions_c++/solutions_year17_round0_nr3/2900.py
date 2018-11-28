    #include <bits/stdc++.h>

    using namespace std;

    #define pb push_back
    #define ppb pop_back
    #define mp make_pair
    #define y0 thezeroXname
    #define x0 thezeroYname
    #define fst first
    #define snd second

    typedef long long ll;
    typedef long double ld;

    const int MAXN = 5e6 + 13;
    const int MAXK = 5e6 + 13;
    const int INF = 2e9 + 7;
    const int MD = 1e9 + 7;
    const ld EPS = 1e-9;
    const ld PI = 3.14159265359;

    int main() {
        #ifdef LOCAL
        freopen("t.in", "r", stdin);
        freopen("t.out", "w", stdout);
        #else
        //freopen("bfs.in", "r", stdin);
        //freopen("bfs.out", "w", stdout);
        #endif

        int T;
        cin >> T;
        for (int t = 0; t < T; t++) {
            ll n, k;
            cin >> n >> k;

            ll mx = n - (n + 1) / 2, mn = (n + 1) / 2 - 1;
            vector<pair<pair<ll, ll>, ll> > count;
            count.pb(mp(mp(mn, mx), 1));
            ll curLevel = 1, maxSteps = 0;
            ll ans[2];

            while (true) {
                /*
                for (int i = 0; i < count.size(); i++) {
                    cout << count[i].fst.fst << ' ' << count[i].fst.snd << " = " << count[i].snd << endl;
                }
                cout << "---\n";
                */
                if (maxSteps + curLevel < k) {
                    bool was;
                    vector<pair<pair<ll, ll>, ll> > newCount;
                    for (int i = 0; i < count.size(); i++) {
                        pair<ll, ll> range = count[i].fst;
                        ll cnt = count[i].snd;
                        pair<ll, ll> l = mp((range.fst + 1) / 2 - 1, range.fst - (range.fst + 1) / 2);
                        pair<ll, ll> r = mp((range.snd + 1) / 2 - 1, range.snd - (range.snd + 1) / 2);
                        
                        was = false;
                        for (int j = 0; j < newCount.size(); j++) {
                            if (newCount[j].fst == l) {
                                was = true;
                                newCount[j].snd += cnt;
                                break;
                            }
                        }
                        if (!was) newCount.pb(mp(l, cnt));
                        
                        was = false;
                        for (int j = 0; j < newCount.size(); j++) {
                            if (newCount[j].fst == r) {
                                was = true;
                                newCount[j].snd += cnt;
                                break;
                            }
                        }
                        if (!was) newCount.pb(mp(r, cnt));
                    }
                    sort(newCount.begin(), newCount.end());
                    count = newCount;
                } else {
                    ll need = k - maxSteps;
                    for (int i = count.size() - 1; i > -1; i--) {
                        if (need <= count[i].snd) {
                            ans[0] = count[i].fst.fst, ans[1] = count[i].fst.snd;
                            break;
                        } else need -= count[i].snd;
                    }

                    break;
                }

                maxSteps += curLevel;
                curLevel *= 2ll;
            }

            cout << "Case #" << t + 1 << ": " << ans[1] << ' ' << ans[0] << endl;
        }

        return 0;
    }