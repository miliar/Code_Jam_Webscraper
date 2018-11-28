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

const ll llinf = 1e18;

const int maxn = 1e5 + 100, inf = 1e9 + 100, sq = 300;

int tst;

int n, r, o, y, g, b, v;

pair<int, char> q[3];

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
    cin >> tst;
    for (int iter = 1; iter <= tst; iter++){
        cout << "Case #" << iter << ": ";
        cin >> n >> r >> o >> y >> g >> b >> v;
        //if (o > 0 || g > 0 || v > 0)
        //    continue;
        q[0] = make_pair(r, 'R');
        q[1] = make_pair(y, 'Y');
        q[2] = make_pair(b, 'B');
        sort(q, q + 3);
        reverse(q, q + 3);
        if (q[0].first > q[1].first + q[2].first){
            cout << "IMPOSSIBLE\n";
            continue;
        }
        string s;
        for (int j = 0; j < 3; j++)
        for (int i = 0; i < q[j].first; i++)
            s.push_back(q[j].second);
        int i1 = 0, i2 = (n + 1) / 2;
        string w;
        while (1){
            if (i1 == (n + 1) / 2)
                break;
            w.push_back(s[i1]);
            cout << s[i1];
            i1++;
            if (i2 == n)
                break;
            w.push_back(s[i2]);
            cout << s[i2];
            i2++;
        }
        cout << '\n';
        if (w.length() != n){
            cout << -1;
            return 0;
        }
        for (int i = 1; i < n; i++)
            if (w[i] == w[i - 1]){
                cout << i;
                return 0;
            }
        if (w[0] == w[n - 1]){
            cout << 0;
            return 0;
        }
    }
}
