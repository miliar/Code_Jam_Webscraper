#include <bits/stdc++.h>

using namespace std;

#define sqr(x) ((x) * (x))
#define pb push_back
#define mp make_pair
#define ins insert
#define f first
#define s second
#define fin(name) freopen(name, "r", stdin)
#define fout(name) freopen(name, "w", stdout)
#define files(name) fin(name".in"); fout(name".out")
//#define endl "\n"
#define fi(st,n) for (int i = (st); i <= (int)(n); ++i)
#define fj(st,n) for (int j = (st); j <= (int)(n); ++j)
#define fk(st,n) for (int k = (st); k <= (int)(n); ++k)
#define fq(st,n) for (int q = (st); q <= (int)(n); ++q)
#define fw(st,n) for (int w = (st); w <= (int)(n); ++w)
#define ff(i, st, n) for (int (i) = (st); (i) <= (int)(n); ++(i))
#define ei(st,n) for (int i = (st); i >= (int)(n); --i)
#define ej(st,n) for (int j = (st); j >= (int)(n); --j)
#define ek(st,n) for (int k = (st); k >= (int)(n); --k)
#define ef(i, st, n) for (int (i) = (st); (i) >= (int)(n); --(i))
#define ri(st,n) for (int i = (st); i < (int)(n); ++i)
#define rj(st,n) for (int j = (st); j < (int)(n); ++j)
#define rk(st,n) for (int k = (st); k < (int)(n); ++k)
#define rq(st,n) for (int q = (st); q < (int)(n); ++q)
#define rf(i, st, n) for (int (i) = (st); (i) < (int)(n); ++(i))
#define clean(a) memset((a),0,sizeof (a))
#define sync ios_base::sync_with_stdio(0);cin.tie(0)
#define y1 dsklmlvmd
#define move move1usad

typedef long long ll;
typedef unsigned long long ull;
typedef double dbl;
typedef long double ldbl;

const int inf = (int)1e9;
const ll linf = (ll)1e18;
const dbl eps = (dbl) 1e-8;
const int mod = (int) 1e9 + 7;
const int maxn = (int) 50 * 50 + 5;
//const dbl M_PI = (dbl)2 * (dbl)acos(0);

//cout<<fixed<<setprecision(10);
//srand(time(0));

vector<int> g[4 * maxn], gt[4 * maxn];
int used[4 * maxn], comp[4 * maxn];
vector<int> order;
int ver_cnt;
pair <int, int> num[55][55][2];

void dfs1 (int v) {
    used[v] = true;
    for (size_t i=0; i<g[v].size(); ++i) {
        int to = g[v][i];
        if (!used[to])
            dfs1 (to);
    }
    order.push_back (v);
}

void dfs2 (int v, int cl) {
    comp[v] = cl;
    for (size_t i=0; i<gt[v].size(); ++i) {
        int to = gt[v][i];
        if (comp[to] == -1)
            dfs2 (to, cl);
    }
}

void add_edge(int v, int u) {
    g[v].pb(u);
    gt[u].pb(v);
}

void add_conj(int v, int u) {
    add_edge(v ^ 1, u);
    add_edge(u ^ 1, v);
}

char a[55][55];
int b[55][55][2];
pair <int, int> move[4];
int kp;
int n, m;
int fl;
int oba[55][55];
int vert[55][55], hor[55][55];

void dfs(int x, int y, int dir) {
    if (a[x][y] == '#') {
        return;
    }
    if (a[x][y] == '.') {
        b[x][y][(dir > 1)] = ver_cnt;
//        return;
    }
    int td;
    if (a[x][y] == '\\') {
        if (dir == 0)
            td = 2;
        if (dir == 1)
            td = 3;
        if (dir == 2)
            td = 0;
        if (dir == 3)
            td = 1; 
        dfs(x + move[td].f, y + move[td].s, td);
        return;
    }
    if (a[x][y] == '/') {
        if (dir == 0)
            td = 3;
        if (dir == 1)
            td = 2;
        if (dir == 2)
            td = 1;
        if (dir == 3)
            td = 0; 
        dfs(x + move[td].f, y + move[td].s, td);
        return;

    }
    dfs(x + move[dir].f, y + move[dir].s, dir);
}


int check(int x, int y, int dir) {
    if (a[x][y] == '#') {
        return 1;
    }
    if (a[x][y] == '|' || a[x][y] == '-') {
        ++kp;
        if (kp == 2) {
            return 0;
        }
    }

    int td;
    if (a[x][y] == '\\') {
        if (dir == 0)
            td = 2;
        if (dir == 1)
            td = 3;
        if (dir == 2)
            td = 0;
        if (dir == 3)
            td = 1; 
        return check(x + move[td].f, y + move[td].s, td);
    }
    if (a[x][y] == '/') {
        if (dir == 0)
            td = 3;
        if (dir == 1)
            td = 2;
        if (dir == 2)
            td = 1;
        if (dir == 3)
            td = 0; 
        return check(x + move[td].f, y + move[td].s, td);

    }
    return check(x + move[dir].f, y + move[dir].s, dir);
}



int main() {
    fin("t.in");
    fout("t.out");
    sync;
    move[0] = mp(1, 0);
    move[1] = mp(-1, 0);
    move[2] = mp(0, 1);
    move[3] = mp(0, -1);
    
    int T;
    cin >> T;

    ff(numt, 1, T) {
        clean(a);
        fl = 1;
        cin >> n >> m;
        fi(0, n + 1) {
            a[i][0] = '#';
            a[i][m + 1] = '#';
        }
        fj(0, m + 1) {
            a[0][j] = '#';
            a[n + 1][j] = '#';
        }

        ver_cnt = 0;
        fi(0, 4 * 50 * 50) {
            g[i].clear();
            gt[i].clear();
        }


        memset(b, -1, sizeof b);
        clean(num);

        clean(oba);
        

        string str;
//        cout << n << " " << m << endl;
        fi(1, n) {
//          cout << i << endl;
            cin >> str;
//            cout << str << endl;
            fj(1, m) {
                a[i][j] = str[j - 1];
            }
        }
//        if (numt == 2)
//            return 0;
        clean(vert);
        clean(hor);
        fi(1, n) {
            fj(1, m) {
                if (a[i][j] == '|' || a[i][j] == '-') {
                    int fl1 = 0;
                    kp = 0;
                    if (check(i, j, 0)) {
                    kp = 0;
                    if (check(i, j, 1)) {
                        vert[i][j] = 1;
                        fl1 = 1;
                        num[i][j][0].f = ver_cnt;
                        num[i][j][0].s = ver_cnt + 1;
                        dfs(i, j, 0);
                        dfs(i, j, 1);
                        ver_cnt += 2;
                    }
                    }
                    kp = 0;
                    if (check(i, j, 2)) {
                    kp = 0; 
                    if (check(i, j, 3)) {
                        hor[i][j] = 1;
                        num[i][j][1].f = ver_cnt;
                        num[i][j][1].s = ver_cnt + 1;
                        dfs(i, j, 2);
                        dfs(i, j, 3);
                        if (fl1) {
                            oba[i][j] = 1;
//                            add_conj(num[i][j][1].f, num[i][j][0].f);
//                            add_conj(num[i][j][1].s, num[i][j][0].s);
                        }
                        ver_cnt += 2;
                    }
                    }
                }
            }
        }

        memset(comp, -1, sizeof comp);

        cout << "Case #" << numt << ": ";
        fi(1, n) {
            fj(1, m) {
                if (a[i][j] != '.')
                    continue;
                if (b[i][j][0] == -1 && b[i][j][1] == -1) {
                    fl = 0;
                    continue;
                }
                if (b[i][j][0] == -1 || b[i][j][1] == -1) {
                    int v = max(b[i][j][1], b[i][j][0]);
                    add_conj(v, v);
                }
            }
        }

        fi(1, n) {
            fj(1, m) {
                if (oba[i][j] == 1) {
                    add_conj(num[i][j][1].f, num[i][j][0].f);
                    add_conj(num[i][j][1].s, num[i][j][0].s);
                }
            }
        }
        
        fi(1, n) {
            fj(1, m) {
                if (b[i][j][0] == -1 || b[i][j][1] == -1) {
                    continue;
                }
                if (a[i][j] != '.')
                    continue;
                if (b[i][j][0] != -1 && b[i][j][1] != -1) {
                    add_conj(b[i][j][0], b[i][j][1]);
                }
            }
        }


        order.clear();
        clean(used);
        for (int i=0; i<ver_cnt; ++i)
            if (!used[i])
                dfs1(i);

        for (int i=0, j=0; i<ver_cnt; ++i) {
            int v = order[ver_cnt-i-1];
            if (comp[v] == -1)
                dfs2 (v, j++);
        }

        for (int i=0; i<ver_cnt; ++i)
            if (comp[i] == comp[i^1]) {
                fl = 0;
            }

            fi(1, n) {
                fj(1, m) {

                    if (a[i][j] == '|' || a[i][j] == '-') {
                        if (vert[i][j] && comp[num[i][j][0].f] > comp[num[i][j][0].s]) {
                            if (hor[i][j] && comp[num[i][j][1].f] > comp[num[i][j][1].s]) {
                                fl = 0;
                            }
                        }
                        else
                        if (hor[i][j] && comp[num[i][j][1].f] > comp[num[i][j][1].s]) {
                        }
                        else {
                            fl = 0;
                        }
                    }
                }
            }


        if (fl) {
            cout << "POSSIBLE" << endl;
            fi(1, n) {
                fj(1, m) {
                    if (a[i][j] == '|' || a[i][j] == '-') {
                        if (vert[i][j] && comp[num[i][j][0].f] > comp[num[i][j][0].s]) {
                            if (hor[i][j] && comp[num[i][j][1].f] > comp[num[i][j][1].s])
                                return 123;
                            cout << "|";
                        }
                        else
                        if (hor[i][j] && comp[num[i][j][1].f] > comp[num[i][j][1].s])
                            cout << "-";
                        else {
                            return 123;
                        }

                    } else {
                        cout << a[i][j];
                    }
                }
                cout << endl;
            }
            continue;
        } else {
            cout << "IMPOSSIBLE" << endl;
            continue;
        }
        
    }
    return 0;
}