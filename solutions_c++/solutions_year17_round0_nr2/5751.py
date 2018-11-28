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
ll x;
ll ans;
void calc(ll pre,int len,int st=1){
    ll cur_mx=ans;
    int ind=-1;
    for(int i=9;i>=st;--i){
        ll cur = pre;
        int cur_len = len;
        while(cur_len<17 && cur<=x){
            cur = cur * 10 + i;
            cur_len++;
            if(cur <= x && cur>cur_mx){
                cur_mx = cur;
                ind = i;
            }
        }
    }
  //  cout << pre <<" "<<len <<" "<<st<<"  - "<<ind<<endl;
    ans = max(ans,cur_mx);
    if(ind!=-1){
        pre = pre * 10 + ind;
        len = len + 1;
        st = ind;
        calc(pre,len,st);
    }
}

int get_len(ll x){
    int res=0;
    while(x>0){
        res++;
        x=x/10;
    }
    return res;
}
void solve()
{

    cout <<"Case #"<<(z++)<<": ";
    cin >> x;
    ans=0;
    int y = get_len(x) - 1;
    while(y > 0){
        ans=ans*10+9;
        y--;
    }

    calc(0,0,1);

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
