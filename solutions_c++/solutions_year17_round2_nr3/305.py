/*
████─████─███─████──███─███─█──█─████─█──█─███
──██─█──█─█───█──██──█──█───█──█─█──█─█──█─█
─██──████─███─████───█──███─████─█────████─███
██───█──█─█───█──██──█────█─█──█─█──█─█──█─█
████─█──█─███─████──███─███─█──█─████─█──█─███

         o###########oo
      o##"          ""##o
    o#"                "##
  o#"                    "#o
 #"  ##              ##   "##
#"                          ##
#  ###################       #
#                            #
#                            #
#                            #
#                            #
#                            #
#                            #
#o                           #
"#o                         ##
 "#o                       ##
  "#o                    o#"
   "#o                  ##
     "#o              o#"
       "#ooo      ooo#######oo
        ###############   "######o
     o###""        "###o      # ###
   o###o     oooo    ###    oo####"
 o###**#     #**#   ############"
 ""##""""""""""###########    #
    # oooooooo#"#**     ##    #
    # #       # # **    ##    #
    #o#       #o#  *****###ooo#
                        ##
                        ##   o###o
                        ## o##***##
               o########## #***#**##o
             o##"   ""###  #***##***#
 o#######o  ###   oo####   ##**####*#
o##"  ""#############""     ##****###
##"         ##              ##*##*###
##          ###              ##### ##
##           ###              # ##  #
##            ##                 #
##             ##
##             ###
##              ###oo
###              ""###
 ###
  ###
*/
#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

typedef long double ld;

void setmax(int &x, int y){
    x = max(x, y);
}

void setmin(int &x, int y){
    x = max(x, y);
}

void setmax(ll &x, ll y){
    x = max(x, y);
}

void setmin(ll &x, ll y){
    x = max(x, y);
}

ll AR = 19, BR = 13, CR = 23, XR = 228, YR = 322, MOD = 1e9 + 993;

const int mod = 1e9 + 7;

ll myrand(){
    ll ZR = (XR * AR + YR * BR + CR) % MOD;
    XR = YR;
    YR = ZR;
    return ZR;
}

string prm(string s){
    string t;
    for (int i = 1; i < s.length(); i++)
        t.push_back(s[i]);
    t.push_back(s[0]);
    return t;
}

ll bpow(ll x, ll y){
    if (y == 0)
        return 1;
    if (y == 1)
        return x;
    ll ret = bpow(x, y >> 1);
    ret = (ret * ret) % mod;
    if (y & 1)
        ret = (ret * x) % mod;
    return ret;
}

ll bdiv(ll x, ll y){
    return (x * bpow(y, mod - 2)) % mod;
}

int md(int x){
    if (x >= mod)
        x -= mod;
    if (x < 0)
        x += mod;
    return x;
}

ll MD(ll x){
    x %= MOD;
    if (x < 0)
        x += MOD;
    return x;
}

const int maxn = 110, inf = 1e9 + 100, sq = 300;

const ll llinf = 1e18;

int n, zap;

int e[maxn][maxn];

ld q[maxn][maxn];

ld ds[maxn], vel[maxn];

int main()
{
    #ifdef ONPC
    //ifstream cin("a.in");
    //ofstream cout("a.out");
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    #else
    //ifstream cin("a.in");
    //ofstream cout("a.out");
    //freopen("trap.in", "r", stdin);
    //freopen("trap.out", "w", stdout);
    #endif // ONPC
    ios::sync_with_stdio(0);
    cout << fixed;
    cout.precision(20);
    int tst;
    cin >> tst;
    for (int iter = 1; iter <= tst; iter++){
        cin >> n >> zap;
        for (int i = 0; i < n; i++){
            int x, y;
            cin >> x >> y;
            ds[i] = x;
            vel[i] = y;
        }
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++){
                cin >> e[i][j];
                if (e[i][j] == -1)
                    q[i][j] = llinf;
                else
                    q[i][j] = e[i][j];
            }
        for (int i = 0; i < n; i++)
            q[i][i] = 0;
        for (int k = 0; k < n; k++)
            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++)
                    if (q[i][k] != llinf && q[k][j] != llinf)
                        q[i][j] = min(q[i][j], q[i][k] + q[k][j]);
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                if (q[i][j] <= ds[i])
                    q[i][j] = q[i][j] / vel[i];
                else
                    q[i][j] = llinf;
        for (int k = 0; k < n; k++)
            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++)
                    if (q[i][k] != llinf && q[k][j] != llinf)
                        q[i][j] = min(q[i][j], q[i][k] + q[k][j]);
        cout << "Case #" << iter << ":";
        for (int i = 0; i < zap; i++){
            int v, u;
            cin >> v >> u;
            cout << ' ' << q[v - 1][u - 1];
        }
        cout << '\n';
    }
}
