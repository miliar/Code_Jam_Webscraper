#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <map>
#include <cstdlib>
#include <cstdio>
#include <complex>
#include <queue>
#include <stack>
using namespace std;
typedef long long unsigned int ll;

#define REP(i,n) for(int i=0; i<(int)n; i++)
#define rep(n) REP(i,n)
#define EPS (1e-7)
#define INF 1e9
#define PI (acos(-1))

const int MAXN = 1024;

int N,R,O,Y,G,B,V;
char res[MAXN];

const int C = 6;
int u[C];

bool check() {
    REP(i,N) {
        int l = i == 0 ? N-1 : i-1;
        int r = i+1;
        switch (res[i]) {
        case 'R':
            if(res[l] == 'V' || res[l] == 'R' || res[l] == 'O') return false;
            if(res[r] == 'V' || res[r] == 'R' || res[r] == 'O') return false;
            break;
        case 'O':
            if(res[l] == 'R' || res[l] == 'O' || res[l] == 'Y') return false;
            if(res[r] == 'R' || res[r] == 'O' || res[r] == 'Y') return false;
            break;
        case 'Y':
            if(res[l] == 'O' || res[l] == 'Y' || res[l] == 'G') return false;
            if(res[r] == 'O' || res[r] == 'Y' || res[r] == 'G') return false;
            break;
        case 'G':
            if(res[l] == 'Y' || res[l] == 'G' || res[l] == 'B') return false;
            if(res[r] == 'Y' || res[r] == 'G' || res[r] == 'B') return false;
            break;
        case 'B':
            if(res[l] == 'G' || res[l] == 'B' || res[l] == 'V') return false;
            if(res[r] == 'G' || res[r] == 'B' || res[r] == 'V') return false;
            break;
        case 'V':
            if(res[l] == 'B' || res[l] == 'V' || res[l] == 'R') return false;
            if(res[r] == 'B' || res[r] == 'V' || res[r] == 'R') return false;
            break;
        default:
            cout << "ERROR" << endl;
            break;
        }
    }
    return true;
}

char conv[C];

int main() {
    int T,tt = 0;
    cin>>T;
    while(tt++ < T) {
        cin>>N>>R>>O>>Y>>G>>B>>V;
        fill_n(res, MAXN, '-'); fill_n(u, C, 0);
        // cout << N << endl; cout << R << endl; cout << O << endl; cout << Y << endl; cout << G << endl; cout << B << endl; cout << V << endl;
        u[0] = R; u[1] = O; u[2] = Y; u[3] = G; u[4] = B; u[5] = V;
        // REP(i,C) { cout << u[i] << ","; } cout << endl;

        // --
        // N = 6; res[0] = 'R'; res[1] = 'Y'; res[2] = 'B'; res[3] = 'R'; res[4] = 'B'; res[5] = 'Y';
        // N = 6; res[0] = 'R'; res[1] = 'R'; res[2] = 'B'; res[3] = 'R'; res[4] = 'B'; res[5] = 'Y';
        // N = 6; res[0] = 'R'; res[1] = 'O'; res[2] = 'B'; res[3] = 'R'; res[4] = 'B'; res[5] = 'Y';
        // cout << check() << endl;

        // --
        int current = -1;
        REP(i,C) { if(u[i] != 0) { current = i; break; } }
        // cout << current << endl;

        // --
        bool ok = true;
        conv[0] = 'R'; conv[1] = 'O'; conv[2] = 'Y'; conv[3] = 'G'; conv[4] = 'B'; conv[5] = 'V';
        REP(i,N) {
            // cout << current << endl;

            res[i] = conv[current];
            --u[current];

            if(i == N-1) {
                break;
            }

            int l = current == 0 ? C-2 : current - 2;
            int r = current == 4 ? 0 : current + 2;

            if(u[l] == 0 && u[r] == 0) {
                ok = false;
                break;
            }

            int next = -1;
            if(u[l] == 0) {
                next = r;
            }
            else if(u[r] == 0) {
                next = l;
            }
            else {
                if(u[l] == u[r]) {
                    // cout << "!" << endl;
                    // cout << conv[l] << endl;
                    // cout << res[0] << endl;
                    // cout << conv[r] << endl;
                    next = conv[l] == res[0] ? l : r;
                }
                else {
                    next = u[l] > u[r] ? l : r;
                }
            }
            // cout << "# " << i << endl;
            // cout << "current : " << current << endl;
            // cout << "next: " << next << endl;
            // cout << u[current] << endl;
            // cout << u[l] << endl;
            // cout << u[r] << endl << endl;

            if(i == N-2 && res[0] == conv[next]) {
                ok = false;
                break;
            }
            current = next;
        }

        // --
        stringstream ss; ss.str("");
        REP(i,N) ss << res[i];
        if(ok) {
            if(!check()) {
                cout << "not ok" << endl;
            }
            cout << "Case #" << tt << ": " << ss.str() << endl;
        }
        else {
            cout << "Case #" << tt << ": IMPOSSIBLE" << endl;
        }
    }
    return 0;
}
