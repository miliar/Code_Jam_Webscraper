#include <iostream>
#include <queue>
#include <set>
using namespace std;        
# define ll unsigned long long

int main(){

    ll a;
    cin >> a;
    int cases = 1;
    priority_queue<ll> pq;
    while(a --){
        ll b, c;
        cin >> b >> c;
        pq.push(b);
        ll lx = 0;
        ll rx = 0;
        while(c--){
            ll mx = pq.top();
            pq.pop();
            if(mx == 1){
                lx = 0;
                rx = 0;
                continue;
            }
            int parity = !(mx & 1);
            lx = mx/2;
            rx = lx - parity;

            if(lx)
            pq.push(lx);

            if(rx)
            pq.push(rx);
        }
        cout << "Case #" << cases++ << ": " << lx << " "  << rx << endl;
        pq = priority_queue<ll>();
    }
    return 0;
}
