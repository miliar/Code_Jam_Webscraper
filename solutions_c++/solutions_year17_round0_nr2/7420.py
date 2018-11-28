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

int t;
long long n, pw[19];

int Count(long long n)
{
    if (n <= 9) return 1;
    return 1 + Count(n / 10);
}

long long Get(int many, int cif)
{
    long long aux = 0;
    for (int i = 1; i <= many; i++) aux = 1LL*aux*10 + cif;

    return aux;
}

int main()
{
    freopen("input","r",stdin);
    freopen("output","w",stdout);
    cin.sync_with_stdio(false);
    
    //prep
    pw[0] = 1;
    for (int i = 1; i < 19; i++) pw[i] = 1LL*pw[i - 1]*10;

    cin >> t;
    for (int cas = 1; cas <= t; cas++)
    {
        cout << "Case #" << cas << ": ";
        
        cin >> n;
        int nr = Count(n);
        if (nr == 1) {cout << n << "\n"; continue;}

        int i, j;
        long long best = 0;
        int last = 0;
        for (i = 1; i <= nr; i++) //at every step get the best character possible
        {
            long long better = best;
            for (j = last; j <= 9; j++)
                if (1LL*best*pw[nr - i + 1] + Get(nr - i + 1, j) <= n)
                    better = best*10 + j;
            best = better;
            last = best % 10;
        }

        cout << best << "\n";
    }
    return 0;   
}