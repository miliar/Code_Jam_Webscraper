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
const int N = (int) 2e5+5;

double p[N],v[N],d;
int n;

double solve() {
    cin>>d>>n;
    double t=0, res;
    FOR(i,1,n) {
        cin>>p[i]>>v[i];
        t = max(t,(d-p[i])/v[i]);
    }
    res = d/t;
    return res;
}

int main() {
    fileopen;
    int T;cin>>T;
    FOR(i,1,T) {
        double res=solve();
        printf("Case #%i: %.8f\n",i,res);
    }
}
