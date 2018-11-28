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
    int cases=1;
    while(t--){
        int n, k; cin >> n >> k;
        priority_queue<ii> pq;
        pq.push(ii(n,0));
        cout << "Case #" << cases++ << ": ";
        fori(i,0,k){
            ii cur = pq.top(); pq.pop();
            cur.second *= -1;
            int pos, sz1, sz2;
            if(cur.first&1){
                pos = (cur.second + cur.first/2);
                sz1 = (cur.first-1)/2;
                sz2 = (cur.first-1)/2;
                if(sz1) pq.push(ii(sz1, -(cur.second+1)));
                if(sz2) pq.push(ii(sz2, -(pos+1)));
            }
            else{
                pos = (cur.second + (cur.first-1)/2);
                sz1 = (cur.first)/2 - 1;
                sz2 = (cur.first)/2;
                if(sz1) pq.push(ii(sz1, -(cur.second+1)));
                if(sz2) pq.push(ii(sz2, -(pos+1)));
            }
            if(i==k-1){
                cout << sz2 << " " << sz1 << endl;
            }
        }
    }

	return 0;
}
