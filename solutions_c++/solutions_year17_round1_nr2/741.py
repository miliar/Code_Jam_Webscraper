#include <bits/stdc++.h>
using namespace std;
#define forsn(i, s, n) for (tint i = (tint)(s); i < (tint)(n); i++)
#define forn(i, n) forsn(i, 0, n)
#define dforsn(i, s, n) for (tint i = (tint)(n) - 1; i >= (tint)(s); i--)
#define dforn(i, n) dforsn(i, 0, n)
#define pb push_back
#define fst first
#define snd second
#define tint long long
#define uint unsigned tint
#define debug(v) cerr << #v << " = " << v << '\n';

int main() {
    uint t;

    cin >> t;

    forn(tt,t) {
        cout << "Case #" << tt+1 << ": ";

        uint n, p;

        cin >> n >> p;

        vector<tint> grIng(n);
        forn(i, n) {
            cin >> grIng[i];
        }

        vector<vector<pair<tint,tint>>> v(n);

        forn(i,n) {
            //v[i].reserve(p);
            forn(j, p) {
                tint gr;
                cin >> gr;
                gr *= 10;

                tint mn = (gr-1) / (grIng[i] * 11) + 1;
                tint mx = gr / (grIng[i] * 9);
                if(mn > mx) continue;

                //cerr << mn << "-" << mx << " gr " << gr << "g mn " << (grIng[i] * mn * 11) << "g mx " << (grIng[i] * mx * 9) << "g" << endl;

                assert(grIng[i] * mn * 9 <= gr and grIng[i] * mn * 11 >= gr);
                assert(grIng[i] * (mn-1) * 9 < gr and grIng[i] * (mn-1) * 11 < gr);
                assert(grIng[i] * mx * 9 <= gr and grIng[i] * mx * 11 >= gr);
                assert(grIng[i] * (mx+1) * 9 > gr and grIng[i] * (mx+1) * 11 > gr);

                v[i].pb({mx,mn});
            }

            if(v[i].size())
                sort(v[i].begin(),v[i].end());
        }

        tint res = 0;
        bool anyEmpty = v[0].size() == 0;

        while(not anyEmpty) {
            tint minMax = v[0].rbegin()->first;
            tint minMin = v[0].rbegin()->second;

            forsn(i,1,n) {
                if(not v[i].size()) {
                    anyEmpty = true;
                    break;
                }
                minMax = min(minMax, v[i].rbegin()->first);
                minMin = min(minMin, v[i].rbegin()->second);
            }
            if(anyEmpty) break;

            bool badMinMax = false;
            forn(i,n) {
                while(v[i].size() and v[i].rbegin()->second > minMax) {
                    v[i].pop_back();
                }
                if(!v[i].size()) {
                    anyEmpty = true;
                    break;
                }
                if(v[i].rbegin()->first < minMin) {
                    badMinMax = true;
                    break;
                }
            }
            if(anyEmpty) break;
            if(badMinMax) continue;

            forn(i,n) {
                v[i].pop_back();
            }
            res++;
        }

        cout << res << endl;
    }

    return 0;
}
