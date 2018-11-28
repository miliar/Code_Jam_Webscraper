#include <bits/stdc++.h>
using namespace std;
using ll =long long;
using vl=vector<ll>;
using vb=vector<bool>;
using vs=vector<string>;
using vvl=vector<vl>;
using pll=pair<ll,ll>;
const ll oo =0x3f3f3f3f3f3f3f3fLL;
const double eps=1e-9;
#define sz(c) ll((c).size())
#define all(c) begin(c),end(c)
#define mp make_pair
#define mt make_tuple
#define pb push_back
#define eb emplace_back
#define xx first
#define yy second
#define FOR(i,a,b) for(ll i=(a); i<(b); i++)
#define FORD(i,a,b) for(ll i=ll(b)-1;i>=(a);i--)
#define TR(X) ({if(1) cerr << "TR: " << (#X) << " = " << (X) << endl; })


vector<vector<vector<vector<bool>>>> mem;
vector<vector<vector<vector<char>>>> choose;
void print(ll first, ll R, ll Y, ll B, ll last) {
        if (R == 0 && Y == 0 && B == 0) {
                return;
        }

        cout << choose[R][Y][B][last];

        switch (choose[R][Y][B][last]) {
                case 'R': print(first, R-1, Y, B, 0); break;
                case 'Y': print(first, R, Y-1, B, 1); break;
                case 'B': print(first, R, Y, B-1, 2); break;
        }
}

bool doit(ll first, ll R, ll Y, ll B, ll last) {
        if (R == 0 && Y == 0 && B == 0) {
                return first != last;
        }

        if (choose[R][Y][B][last]) return mem[R][Y][B][last];

        if (R && last != 0 && doit(first, R-1, Y, B, 0)) {
                choose[R][Y][B][last] = 'R';
        } else if (Y && last != 1 && doit(first, R, Y-1, B, 1)) {
                choose[R][Y][B][last] = 'Y';
        } else if (B && last != 2 && doit(first, R, Y, B-1, 2)) {
                choose[R][Y][B][last] = 'B';
        } else {
                choose[R][Y][B][last] = ' ';
                mem[R][Y][B][last] = false;
                return false;
        }
        return mem[R][Y][B][last] = true;
}
int main(){ cin.sync_with_stdio(0);
        ll T; cin >> T;
        FOR(TC, 1, T+1) {
                ll N, R, O, Y, G, B, V; 
                cin >> N >> R >> O >> Y >> G >> B >> V;

                bool possible = false;
                ll solution = -1;
                FOR(first, 0, 3) {
                        mem.assign(R+1, vector<vector<vector<bool>>>(Y+1, vector<vector<bool>>(B+1, vector<bool>(3, false))));
                        choose.assign(R+1, vector<vector<vector<char>>>(Y+1, vector<vector<char>>(B+1, vector<char>(3, 0))));

                        /*
                        FOR(last, 0, 3) {
                                mem[0][0][0][last] = last != first;

                        }
                        FOR(r, 0, R+1) {
                                FOR(y, 0, Y+1) {
                                        FOR(b, 0, B+1) {
                                                FOR(last, 0, 3) {
                                                        if (R == 0 && Y == 0 && B == 0) {
                                                                mem[R][Y][B][last] = last != first;
                                                                continue;
                                                        }


                                                }
                                        }
                                }
                        }
                        */
                        if (first == 0) R--;
                        else if (first == 1) Y --;
                        else if (first == 2) B--;

                        if (R >= 0 && Y >= 0 && B >= 0 && doit(first, R, Y, B, first)) {
                                possible = true;
                                solution = first;
                                break;
                        }
                        if (first == 0) R++;
                        else if (first == 1) Y ++;
                        else if (first == 2) B++;
                }

                cout << "Case #" << TC << ": ";
                if (!possible) {
                        cout << "IMPOSSIBLE" << endl;
                } else {
                        switch(solution) {
                                case 0: cout << 'R';break;
                                case 1: cout << 'Y';break;
                                case 2: cout << 'B';break;
                        }
                        print(solution, R, Y, B, solution);
                        cout << endl;
                }

        }
} //cin.tie(0) bei schnellem Wechseln
