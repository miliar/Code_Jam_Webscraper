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
const int E=19;

int p10[E];

int len(int n) {
    int cnt=0;
    F(e,E) if (n >= p10[e])
        cnt++;
    return cnt;
}

int dig(int n, int k) {
    return n/p10[k]%10;
}

signed main() {
    p10[0] = 1;
    F(e,E-1) p10[e+1] = p10[e]*10;
    int nt; cin>>nt;
    F(t,nt) {
        cout<<"Case #"<<t+1<<": ";
        int n; cin>>n;
        while (true) {
            int prob=-1, l=len(n);
            F(e,l-1) if (dig(n,e) < dig(n,e+1)) {
                prob = e;
                break;
            }
            if (prob == -1) break;
            else n -= n % p10[prob+1] + 1;
        }
        P(n);
    }
}
