#include<bits/stdc++.h>
#define mp make_pair
#define PII pair<int,int>
#define fi first
#define se second
#define pb push_back
#define ll long long
#define ull unsigned long long
#define ui unsigned int
#define sci(x) scanf("%d",&x)
#define scs(s) scanf("%s",s)
#define scc(c) scanf("%c",c)
#define scd(d) scanf("%lf",&d)
#define scld(ld) scanf("%Lf",&ld)
using namespace std;

//********************************************
//Error tracking
#define show(args...) { vector<string> _v = split(#args, ','); err(_v.begin(), args); }

vector<string> split(const string& s, char c) {
    vector<string> v;
    stringstream ss(s);
    string x;
    while (getline(ss, x, c))
        v.emplace_back(x);
    return move(v);
}

void err(vector<string>::iterator it) {}
template<typename T, typename... Args>
void err(vector<string>::iterator it, T a, Args... args) {
    cerr << it -> substr((*it)[0] == ' ', it -> length()) << " = " << a << '\n';
    err(++it, args...);
}
//********************************************

const int NMAX = 1005;

int t, n, k, a[NMAX];
char s[NMAX];

int main()
{
    freopen("input","r",stdin);
    freopen("output","w",stdout);
    cin.sync_with_stdio(false);
    
    cin >> t;
    for (int cas = 1; cas <= t; cas++)
    {
        cout << "Case #" << cas << ": ";
        cin >> (s + 1) >> k;
        n = strlen(s + 1);

        int i, j, sol = 0;
        for (i = 1; i <= n; i++)
            if (s[i] == '-')
                a[i] = 1;
            else a[i] = 0;

        for (i = 1; i <= n - k + 1; i++) 
            if (a[i] == 1)
            {
                sol++;
                for (j = i ; j <= i + k - 1; j++) a[j] = 1 - a[j];
            }

        int ok = 1;
        for (i  = 1; i <= n; i++)
            if (a[i] == 1)
                ok = 0;

        if (!ok) cout << "IMPOSSIBLE\n";
        else cout << sol << "\n";
    }
    return 0;   
}