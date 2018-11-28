#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long int llu;
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define mem(a, v) memset(a, v, sizeof(a))
#define PI acos(-1)
#define S(a) scanf("%d",&a)
#define SL(a) scanf("%lld",&a)
#define S2(a, b) scanf("%d%d",&a,&b)
#define nl printf("\n")
#define deb(x) cout<<#x<<" : "<<x<<endl;
#define deb2(x, y) cout<<#x<<" : "<<x<<" | "<<#y<<" : "<<y<<endl;
#define deb3(x, y, z) cout<<#x<<" : "<<x<<" | "<<#y<<" : "<<y<<" | "<<#z<<" : "<<z<<endl;
#define debv(x) {cout<<#x<<" : "<<endl; for(int ii =0; ii < x.size(); ii++) cout<<x[ii]<<" "; cout<<endl; }
#define debarr(x, xs) {cout<<#x<<" : "<<endl; for(int ii =0; ii < xs; ii++) cout<<x[ii]<<" "; cout<<endl; }
//auto T=clock(); 
//cout<<double(clock()-T)/CLOCKS_PER_SEC<<'\n';
//cout << fixed << setprecision(10) << f(0, 0, 0) << "\n";
const ll mod = 1000000007LL;
const int lmt = 1000005;

string s;
int a[1005];

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    S(t);
    for(int tst = 1; tst <= t; tst++) {
        int k;
        cin >> s >> k;

        int n = s.size();
        for(int i = 0; i < n; i++) {
            if(s[i] == '+')
                a[i] = 1;
            else
                a[i] = 0;
        }

        bool flag = true;
        int ans = 0;

        for(int i = 0; i < n; i++) {
            if(a[i] == 0) {
                if((i+k) > n) {
                    flag = false;
                    break;
                } else {
                    for(int j = 0; j < k; j++)
                        a[i+j] = 1-a[i+j];
                    ans++;
                }
            }
        }
        if(flag)
            printf("Case #%d: %d\n",tst, ans);
        else
            printf("Case #%d: IMPOSSIBLE\n",tst);            
    }
    return 0;
}