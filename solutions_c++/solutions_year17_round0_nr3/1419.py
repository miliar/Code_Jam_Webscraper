//This template was originally written by zscoder and copied by duckmoon.
#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace std;
using namespace __gnu_pbds;

#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define fbo find_by_order
#define ook order_of_key
#define INF 2e18

typedef long long ll;
typedef pair<ll,ll> ii;
typedef vector< pair<ll, ll> > vii;
typedef vector<int> vi;
typedef long double ld;
typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> pbds;
typedef set<int>::iterator sit;
typedef map<int,int>::iterator mit;
typedef vector<int>::iterator vit;

ll t, n, k, a, b, ans1, ans2;
priority_queue <ii, vii > pq;

int main(){
    freopen("C-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> t;
    for(int x = 1; x <= t; x++){
        cin >> n >> k;
        pq.push(mp(n, 1));
        while(k > 0){
            a = pq.top().fi;
            b = pq.top().se;
            pq.pop();
            while(!pq.empty()){
                if(pq.top().fi == a){
                    b += pq.top().se;
                    pq.pop();
                }
                else{
                    break;
                }
            }
            if(b < k){
                if(a%2 == 1){
                    pq.push(mp(a/2, 2*b));
                }
                else{
                    pq.push(mp(max(ll(0),a/2-1), b));
                    pq.push(mp(a/2, b));
                }
            }
            else{
                if(a%2 == 0){
                    ans1 = max(ll(0),a/2-1);
                    ans2 = a/2;
                }
                else{
                    ans1 = a/2;
                    ans2 = a/2;
                }
            }
            k -= b;
        }
        cout << "Case #" << x << ": " << ans2 << " " << ans1 << endl;
        while(!pq.empty()){
            pq.pop();
        }
    }
    return 0;
}
