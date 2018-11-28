#include <bits/stdc++.h>
#define int long long
#define P(x) cout << x << endl
#define D(x) P(#x << ": " << x)
#define F(i,n) for (int i=0; i<(int)(n); i++)
#define DEC(i,n) for (int i=(int)(n); --i>=0;)
#define pb push_back
#define all(v) v.begin(), v.end()
using namespace std;
void MI(int &a, int v) {a = min(a,v);}
void MA(int &a, int v) {a = max(a,v);}

signed main() {
    int nt; cin>>nt;
    F(t,nt) {
        cout<<"Case #"<<t+1<<": ";
        int n,k; cin>>n>>k;
        k--;
        int rem=n, p=1;
        while (k >= p) {
            k -= p;
            rem -= p;
            p *= 2;
        }
        int lo=rem/p, hi=rem/p+1;
        int nhi=rem%p;
        if (k < nhi)
            P(hi/2<<' '<<(hi-1)/2);
        else {
            P(lo/2<<' '<<(lo-1)/2);
        }
    }
}
