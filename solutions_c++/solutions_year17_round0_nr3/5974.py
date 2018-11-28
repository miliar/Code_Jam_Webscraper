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

struct obj{
    int l,r;
    int size;

    bool operator < (const obj o) const{
        if(size == o.size) {
            return l > o.l;
        }
        return size < o.size;
    }
};


int z=1;
void solve()
{
    priority_queue<obj> p;
    int n,k;
    cin >> n >> k;
    cout <<"Case #"<<(z++)<<": ";
    if(n==k){
        cout <<"0 0"<<endl;
        return;
    }
    obj temp = {1,n,n-1+1};
    p.push(temp);
    for(int j=1;j<=k-1;++j){
        obj cur = p.top();
        p.pop();
        int l1 = cur.l, m = (cur.l + cur.r)/2, r1 = cur.r;
        if(l1<=m-1){
            obj temp = {l1,m-1, m-l1};
            p.push(temp);
        }
        if(m+1<=r1){
            obj temp = {m+1,r1, r1-m};
            p.push(temp);
        }
    }

    obj  ans = p.top();
    cout <<ans.size/2<<" "<< (ans.size-1)/2<<endl;

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
