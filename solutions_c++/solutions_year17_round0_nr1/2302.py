#include <bits/stdc++.h>
using namespace std;

#define fi          "input.txt"
#define fo          "output.txt"
#define fileopen    freopen(fi,"r",stdin);freopen(fo,"w",stdout)
#define FOR(i,l,r)  for(int i=(int)(l);i<=(int)(r);i++)
#define FORD(i,l,r) for(int i=(int)(l);i>=(int)(r);i--)
#define xy          pair<int64,int>
#define int64       long long
#define ld          long double
#define X           first
#define Y           second
#define pb          push_back
#define init(a,v)   memset(a,v,sizeof(a))
#define Sz(s)       (int)(s.size())
#define EL          cout<<endl
#define digit(x)    ('0'<=x&&x<='9')
#define forever     while (true)
#define ran(l,r)    ((1LL*rand()*rand())%((int)(r)-(int)(l)+1)+(int)(l))

const int OO = (int) 2e9+5;
const int MOD = (int) 1e9+7;
const long double Pi = 3.141592653589793238;
const int N = (int) 1e3+5;

char s[N];
int d[N],n,k,x;

int64 solve() {
    cin>>(s+1)>>k;
    n = strlen(s+1);
    init(d,0);
    x = 0;
    int64 res = 0;
    FOR(i,1,n) {
        if (i<=n-k+1) {
            res+= (s[i]=='-')^x;
            d[i+k-1]^= (s[i]=='-')^x;
            x^= (s[i]=='-')^x^d[i];
        } else {
            if ((s[i]=='-')!=x)
                return -1;
            x^= d[i];
        }
    }
    return res;
}

int main() {
    fileopen;
    int T;
    cin>>T;
    FOR(_,1,T) {
        int64 res = solve();
        if (res>=0) {
            cout<<"Case #"<<_<<": "<<res<<endl;
        } else {
            cout<<"Case #"<<_<<": "<<"IMPOSSIBLE"<<endl;
        }
    }
}
