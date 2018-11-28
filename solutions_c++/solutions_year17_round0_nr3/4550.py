#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
using namespace std;
typedef long long ll;
typedef struct {
    ll gap, i,j;
}Data;


bool compare(Data d1, Data d2){
    if (d1.gap == d2.gap) {
        return d1.i > d2.i;
    }
    return d1.gap < d2.gap;
}
int main(){
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++){
        ll n, k;
        cin >> n >> k;
        priority_queue<Data, vector<Data>, decltype(&compare)> pq(&compare);
        Data x = {n, 0, n+1};
        pq.push(x);
        ll l = n+2, r = n+2;
        for (ll i = 0; i < k; i++) {
            //int tl = n+2, tr = n+2;
            Data t = pq.top();
            pq.pop();
            ll pos = (t.j+t.i)/2;
            l = pos-t.i-1;
            r = t.j-pos-1;
            Data t1 = {l-1, t.i, pos};
            Data t2 = {r-1, pos, t.j};
            pq.push(t1);
            pq.push(t2);
        }
        cout << "Case #" << t << ": " << max(l,r) << " " << min(l,r) << endl;
    }
    return 0;
}