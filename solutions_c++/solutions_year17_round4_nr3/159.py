#include <iostream>
#include <algorithm>
#include <vector>
#include <deque>
#include <cassert>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <string>
#include <utility>
#include <cmath>
#include <bitset>
#include <climits>
#include <iomanip>
#include <fstream>
#include <unordered_set>
#include <unordered_map>
#include <cstdio>
#include <cstring>
#include <numeric>
#include <sstream>

using namespace std;

#define ll long long
#define N (ll)(1<<21)
#define INF (ll)(1e18+1)
#define EPS (1e-8)
#define PI (3.14159265358979323846)
#define ld double
#define MOD (ll)(1e9+7)
#define pll pair<ll,ll>
#define pii pair<int,int>
#define pdd pair<ld,ld>
#define fi first
#define se second
#define rep(i,a,n) for (ll i = a; i<n; i++)
#define per(i,a,n) for (ll i = n-1; i>=a; i--)
#define pb push_back

char ch[50][50];
ll status[50][50]; // 0 - free, 1 - horz, 2 - vert
ll statustmp[50][50];
ll r, c;

ll dr[4] = {0,0,1,-1};
ll dc[4] = {1,-1,0,0};

bool work(ll rr, ll cc, ll ss) {
    if (ss == 1) {
        rep(k,2,4) { //scan vert
            rep(m,1,50) {
                ll nr = rr+m*dr[k];
                ll nc = cc+m*dc[k];
                if (nr < 0 || nr >= r || nc < 0 || nc >= c) break;
                if (ch[nr][nc] == '#') break;
                if (ch[nr][nc] == '.') {
                    //force new turrets to be horz
                    bool found = false;
                    rep(k2,0,2) {
                        rep(m2,1,50) {
                            ll nnr = nr+m2*dr[k2], nnc = nc+m2*dc[k2];
                            //cout << nr << " " << nc << " " << nnr << " " << nnc << endl;
                            if (nnr < 0 || nnr >= r || nnc < 0 || nnc >= c) break;
                            if (ch[nnr][nnc] == '#') break;
                            if (ch[nnr][nnc] == '|' || ch[nnr][nnc] == '-') {
                                if (statustmp[nnr][nnc] == 2)
                                    return false;
                                if (statustmp[nnr][nnc] == 0) {
                                    statustmp[nnr][nnc] = 1;
                                    if (!work(nnr,nnc,1))
                                        return false;                                   
                                }
                                found = true;
                                break;
                            }
                        }
                        if (found) break;
                    }
                    if (!found) {
                        return false;
                    }
                }
            }                
        }
    }
    else if (ss == 2) {
        rep(k,0,2) { //scan horz
            rep(m,1,50) {
                ll nr = rr+m*dr[k];
                ll nc = cc+m*dc[k];

                if (nr < 0 || nr >= r || nc < 0 || nc >= c) break;
                if (ch[nr][nc] == '#') break;
                if (ch[nr][nc] == '.') {
                    //force new turrets to be vert
                    bool found = false;
                    rep(k2,2,4) {
                        rep(m2,1,50) {
                            ll nnr = nr+m2*dr[k2], nnc = nc+m2*dc[k2];
                            if (nnr < 0 || nnr >= r || nnc < 0 || nnc >= c) break;
                            if (ch[nnr][nnc] == '#') break;
                            if (ch[nnr][nnc] == '|' || ch[nnr][nnc] == '-') {
                                if (statustmp[nnr][nnc] == 1)
                                    return false;
                                if (statustmp[nnr][nnc] == 0) {
                                    statustmp[nnr][nnc] = 2;
                                    if (!work(nnr,nnc,2))
                                        return false;                                   
                                }
                                found = true;
                                break;
                            }
                        }
                        if (found) break;
                    }
                    if (!found) return false;
                }
            }                
        }
    }
    return true;
}

void resettmp() {
    rep(i,0,r) {
        rep(j,0,c) {
            statustmp[i][j] = status[i][j];
        }
    }
}

void setfromtmp() {
    rep(i,0,r) {
        rep(j,0,c) {
            status[i][j] = statustmp[i][j];
        }
    }
}

void solve() {
    cin >> r >> c;

    memset(status,0,sizeof(status));
    rep(i,0,r) {
        rep(j,0,c) {
            cin >> ch[i][j];
        }
    }

    bool impossible = false;

    rep(i,0,r) {
        rep(j,0,c) {
            if (!(ch[i][j] == '|' || ch[i][j] == '-')) continue;
            rep(k,0,4) {
                rep(m,1,50) {
                    ll nr = i+m*dr[k];
                    ll nc = j+m*dc[k];

                    if (nr < 0 || nr >= r || nc < 0 || nc >= c) break;
                    if (ch[nr][nc] == '#') break;
                    if (ch[nr][nc] == '|' || ch[nr][nc] == '-') {
                        //cout << i << " " << j << " " << nr << " " << nc << endl;
                        if (k <= 1) { //sideways, must be vert
                            if (status[i][j] == 1 || status[nr][nc] == 1)
                                impossible = true;
                            status[i][j] = status[nr][nc] = 2;
                        }
                        else { // updown, must be horz
                            if (status[i][j] == 2 || status[nr][nc] == 2)
                                impossible = true;
                            status[i][j] = status[nr][nc] = 1;
                        }
                        break;
                    }
                }
            }
        }
    }

    if (impossible) {
        cout << "IMPOSSIBLE" << endl;
        return;
    }


    rep(i,0,r) {
        rep(j,0,c) {
            if (!(ch[i][j] == '|' || ch[i][j] == '-')) continue;
            if (status[i][j] != 0) continue;

            //cout << i << " " << j << " try hor" << endl;
            //try horz, then vert neighbors must be filled.
            resettmp();
            statustmp[i][j] = 1;
            if (work(i,j,1)) {
                setfromtmp();
                continue;
            }

            //cout << i << " " << j << " try ver" << endl;
            //try vert, then horz neighbors must be filled.
            resettmp();
            statustmp[i][j] = 2;
            if (work(i,j,2)) {
                setfromtmp();
                continue;
            }

            impossible = true;
        }
    }

    if (impossible) {
        cout << "IMPOSSIBLE" << endl;
        return;
    }

    rep(i,0,r) {
        rep(j,0,c) {
            if (!(ch[i][j] == '.')) continue;
            bool found = false;
            rep(k,0,4) {
                rep(m,1,50) {
                    ll nr = i+m*dr[k];
                    ll nc = j+m*dc[k];

                    if (nr < 0 || nr >= r || nc < 0 || nc >= c) break;
                    if (ch[nr][nc] == '#') break;
                    if (status[nr][nc] == 1 && k < 2) {
                        //cout << i << " " << j << " " << nr << " " << nc << endl;
                        found = true;
                    }
                    else if (status[nr][nc] == 2 && k >= 2) {
                        //cout << i << " " << j << " " << nr << " " << nc << endl;
                        found = true;
                    }
                }
            }
            if (!found) {
                impossible = true;
            }
        }
    }

    if (impossible) {
        cout << "IMPOSSIBLE" << endl;
        return;
    }

    cout << "POSSIBLE" << endl;
    rep(i,0,r) {
        rep(j,0,c) {
            if (!(ch[i][j] == '|' || ch[i][j] == '-')) {
                cout << ch[i][j];
                continue;
            }
            if (status[i][j] == 1) {
                cout << '-';
            }
            else if (status[i][j] == 2) {
                cout << '|';
            }
            else
                throw;
        }
        cout << endl;
    }


}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    ll t;
    cin >> t;
    rep(i,0,t) {
        cout << "Case #" << i+1 << ": ";
        solve();
    }
}