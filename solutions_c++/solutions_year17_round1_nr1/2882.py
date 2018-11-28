#include<iostream>
#include<cmath>
#include<cstdio>
#include<map>
#include<algorithm>

typedef long long ll;

using namespace std;

int K;
int l;

int main() {
    int T;
    cin >> T;
    map<char, int[2]> m;
    for (int c=1; c<=T;++c) {
        int R, C;
        cin >> R >> C;
        char cake[R][C];
        //cout << endl;
        for (ll r = 0; r<R;++r) {
            for (ll c=0;c<C;++c) {
                cin >> cake[r][c];
                if (cake[r][c] >= 'A' && cake[r][c] <= 'Z') {
                    m[cake[r][c]][0] = r;
                    m[cake[r][c]][1] = c;
                }
                //cout << cake[r][c];
            }
            //cout << endl;
        }
        for (map<char, int[2]>::iterator it = m.begin(); it != m.end(); ++it) {
            char init = it->first;
            //cout << init << endl;
            // original
            ll orr = it->second[0];
            ll orc = it->second[1];
            // top right bottom left
            ll trr = it->second[0];
            ll trc = it->second[1];
            ll blr = it->second[0];
            ll blc = it->second[1];
            ll besttr[2] = {trr, trc};
            ll bestbl[2] = {blr, blc};
            ll best = (trc-blc+1)*(trr-blr+1);
            cake[orr][orc] = '?';
            while (trc < C && cake[trr][trc] == '?') {
                ++trc;
            }
            --trc;
            while (blc >= 0 && cake[blr][blc] == '?') {
                --blc;
            }
            ++blc;
            if ((trr-blr+1)*(trc-blc+1) >= best) {
                besttr[0] = trr;
                besttr[1] = trc;
                bestbl[0] = blr;
                bestbl[1] = blc;
                best = (trc-blc+1)*(trr-blr+1);
            }
            //cout << best << endl;
            //cout << "tr = [" << trr << " " << trc << "] bl = [" << blr << " " << blc << "]"  << endl;
            ++trr;
            for (;trr < R;++trr) {
                if (cake[trr][orc] != '?') break;
                // go left
                for (int i = orc; i >= blc; --i) {
                    if (cake[trr][i] != '?') {
                        blc = i+1;
                        break;
                    }
                }
                // go right
                for (int i = orc; i <= trc; ++i) {
                    if (cake[trr][i] != '?') {
                        trc = i-1;
                        break;
                    }
                }
                if ((trr-blr+1)*(trc-blc+1) >= best) {
                    besttr[0] = trr;
                    besttr[1] = trc;
                    bestbl[0] = blr;
                    bestbl[1] = blc;
                    best = (trc-blc+1)*(trr-blr+1);
                }
            }
            --trr;
            //cout << best << endl;
            --blr;
            for (;blr >= 0;--blr) {
                if (cake[blr][orc] != '?') break;
                // go left
                for (int i = orc; i >= blc; --i) {
                    if (cake[blr][i] != '?') {
                        blc = i+1;
                        break;
                    }
                }
                // go right
                for (int i = orc; i <= trc; ++i) {
                    if (cake[blr][i] != '?') {
                        trc = i-1;
                        break;
                    }
                }
                if ((trr-blr+1)*(trc-blc+1) >= best) {
                    besttr[0] = trr;
                    besttr[1] = trc;
                    bestbl[0] = blr;
                    bestbl[1] = blc;
                    best = (trc-blc+1)*(trr-blr+1);
                }

            //cout << "tr = [" << trr << " " << trc << "] bl = [" << blr << " " << blc << "]"  << endl;
            //cout << "currscore: " << (trr-blr+1)*(trc-blc+1) << endl;
            }
            ++blr;
            //cout << best << endl;
            for (ll r = bestbl[0]; r <= besttr[0]; ++r) {
                for (ll c = bestbl[1]; c <= besttr[1]; ++c ) {
                    cake[r][c] = init;
                }
            }
            /*
            for (int r = 0; r < R; ++r) {
                for (int c = 0; c < C; ++c ) {
                    cout << cake[r][c];
                }
                cout << endl;
            }
            */
        }

        cout << "Case #" << c << ":" << endl;
        for (int r = 0; r < R; ++r) {
            for (int c = 0; c < C; ++c ) {
                cout << cake[r][c];
            }
            cout << endl;
        }
        m.clear();
    }
}

