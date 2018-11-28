#include <bits/stdc++.h>
using namespace std;
#define mp(X,Y) make_pair(X,Y)
#define F first
#define S second
typedef long long ll;
typedef pair<int,int> PII;
typedef pair<ll,ll> PLL;
long double p[110];
int main(){
    ios::sync_with_stdio(0);
    freopen("3.in","r",stdin);
    freopen("3.out","w",stdout);
    int cas = 1;
    int t;
    long double pi = acos(-1.0);
    cin >> t;
    while(t--){
        cout << "Case #" << cas ++ << ": ";
        int n,k;
        cin >> n >>k;
        long double U;
        cin >> U;
        for(int i=  0 ; i <n ; i ++){
            cin >> p[i];
        }
        sort(p,p+n);
        for(int i = n - 1; i >= 0 ; i--){
            long double sum = 0;
            for(int j = 0 ; j < i ; j ++){
                sum += p[i] - p[j];
            }
            long double avg = p[i];
            if(U - sum > -1e-9){
                avg += (U - sum) / (i + 1);
                long double ans = 1.0;
                for(int j = 0 ; j <= i ; j ++){
                    ans *= avg;
                }
                for(int j = i+1;j < n ; j ++){
                    ans *= p[j];
                }
                long double maxx = 1.0;
                cout << fixed<< setprecision(100) <<min(ans,maxx) << endl;
                break;
            }

        }
    }
    return 0;
}
