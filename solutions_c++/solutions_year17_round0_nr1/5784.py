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

bool debug = 0;

const int MAXN = 2e5 + 100;

int z=1;
void solve()
{
    string s;
    cin >> s;
    int k;
    cin >> k;
    int ans=0;
    for(int i=0;i+k-1<s.size();++i){
        if(s[i]=='-'){
            ans++;
            for(int e=i;e<=i+k-1;++e){
                if(s[e]=='-')
                    s[e]='+';
                else
                    s[e]='-';
            }
        }
    }

    cout <<"Case #"<<(z++)<<": ";
    for(char c:s){
        if(c=='-')
        {
            cout << "IMPOSSIBLE"<<endl;
            return;
        }
    }
    cout << ans<<endl;
}


#define FILE "shifts"
int main()
{
        #ifdef zxc
            freopen("input.txt","r",stdin);
           freopen("output.txt","w",stdout);
        #else
              freopen(FILE".in","r",stdin);
              freopen(FILE".out","w",stdout);
        #endif // zxc

     //   freopen("input.txt","r",stdin);
       // freopen("output.txt","w",stdout);

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
