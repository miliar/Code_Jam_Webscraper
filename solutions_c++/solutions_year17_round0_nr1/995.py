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
        string s; int k;
        cin>>s>>k;
        int cnt=0;
        F(i,(int)s.size()-k+1) {
            if (s[i] == '-') {
                cnt++;
                F(j,k) {
                    if (s[i+j] == '-')
                        s[i+j] = '+';
                    else
                        s[i+j] = '-';
                }
            }
        }
        bool ok=true;
        for (char c : s) if (c == '-')
            ok = false;
        cout<<"Case #"<<t+1<<": ";
        if (ok) P(cnt);
        else P("IMPOSSIBLE");
    }
}
