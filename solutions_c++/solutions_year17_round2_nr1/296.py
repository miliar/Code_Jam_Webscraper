#include <bits/stdc++.h>

using namespace std;
typedef  long long ll;
typedef unsigned long long ull;
int inf_int=1e9;
ll inf_ll=1e16;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
#define pb push_back
const double pi=3.1415926535898;
#define dout if(debug) cout
#define fi first
#define se second
#define sp setprecision
#define siz(a) a.size()
#define next asdfafgasgasg
#define left asfafgasgasgasgalhs
#define right afszfpfzzk
#define free asfasfasfasafg

const int mod = 1e9 + 9;
const int MAXN = 2e5+100;
bool debug = false;

typedef long double dbl;


int z=1;

int s[MAXN],k[MAXN];
void solve()
{
    dbl d;int n;
    cin >>d >> n;

    dbl time=0;
    for(int i=1;i<=n;++i){
        cin>> k[i] >> s[i];
        time = max(time, (d-k[i])/s[i]);
    }
    cout<<fixed << setprecision(15)<<"Case #"<<z++<<": " << d/time<<endl;

}


#define FILE "shifts"
int main()
{
        #ifdef zxc
            freopen("input.txt","r",stdin);
           freopen("output.txt","w",stdout);
        #else
        #endif // zxc


       if(!debug)
       {
            ios_base::sync_with_stdio(0);
            cin.tie(0);
            cout.tie(0);
       }

        int t=1;
        cin >> t;
        while(t--)
           solve();
        return 0;
}
