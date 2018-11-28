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
#define int long long
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

const int NMAX = 1000005;

int t;
ll n, k;
priority_queue< pair<ll, ll> , vector< pair<ll, ll> >, less< pair<ll, ll> >>Q;

void Show(long long val)
{
    if (val % 2 == 0) cout << val / 2 << " " << (val / 2) - 1 << "\n";
    else cout << val / 2 << " " << val / 2 << "\n";
}

int32_t main()
{
    freopen("input","r",stdin);
    freopen("output","w",stdout);
    cin.sync_with_stdio(false);
    
    cin >> t;
    for (int cas = 1; cas <= t; cas++)
    {
        cout << "Case #" << cas << ": ";

        cin >> n >> k;

        Q.push(mp(n, 1));

        while (k)
        {
            pair<ll, ll>aux = Q.top(); Q.pop();
            //cout << aux.fi << " " << aux.se << "\n";

            if (aux.se >= k) //here it is
            {
                Show(aux.fi);
                break;
            }
            else
            {
                k -= aux.se; //passed by them

                long long val = aux.fi;
                long long frecv = aux.se;

                if (val & 1) Q.push(mp(val / 2, frecv * 2));
                else
                {
                    Q.push(mp((val / 2) - 1, frecv));
                    Q.push(mp(val / 2, frecv));
                }
            }
        }

        //clean
        while (!Q.empty()) Q.pop();
    }
    return 0;   
}