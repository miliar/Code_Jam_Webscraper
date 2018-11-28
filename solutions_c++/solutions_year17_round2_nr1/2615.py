#include <bits/stdc++.h>

#define INF 2139062143
#define debug(x) cout << #x << " = " << x << endl
#define fori(i, ini, lim) for(int i= int(ini); i<(int)lim; ++i)
#define ford(i, ini, lim) for(int i= int(ini); i>=(int)lim; --i)
using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<int, int> ii;

int main(){
	ios_base::sync_with_stdio(false);

    int t; cin >> t;
    int cases =  1;
    while(t--){
        double d; int n; cin >> d >> n;
        double ans = 0;
        fori(i,0,n){
            double start, sp; cin >> start >> sp;
            double cur = (d - start)/sp;
            ans = max(ans, cur);
        }
        cout << "Case #" << cases++ << fixed << setprecision(6) << ": " << d/ans << endl;
    }

	return 0;
}
