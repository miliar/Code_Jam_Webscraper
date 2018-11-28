#include <bits/stdc++.h>
#define int long long
#define P(x) cout << x << endl
#define D(x) P(#x << ": " << x)
#define F(i,n) for (int i=0; i<(int)(n); i++)
#define DEC(i,n) for (int i=(int)(n); --i>=0;)
#define $(s) (int)((s).size())
#define ALL(v) v.begin(), v.end()
#define V vector
#define pb push_back
using namespace std;
void MI(int &a, int v) {a = min(a,v);}
void MA(int &a, int v) {a = max(a,v);}

signed main() {
    int nt; cin>>nt;
    F(t,nt) {
        int n; int d; cin>>d>>n;
        double maxt=0;
        //D(n);
        F(i,n) {
            double k,s; cin>>k>>s;
            maxt = max(maxt, (d-k)/s);
        }
        printf("Case #%lld: %.8f\n", t+1, d/maxt);
    }
}
