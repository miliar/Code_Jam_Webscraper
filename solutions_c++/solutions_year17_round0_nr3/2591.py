#include<iostream>
using namespace std;

int main() {

    int t, level;
    long long int n, k, sum, lo, hi, p, prev, q, r, ans;
    cin >> t;
    
    for (int x = 0; x < t; x++) {
        
        cin >> n >> k;
        sum = 0; level = 0, p = 1;
        
        while (k > sum) {
            prev = sum;
            sum += p;
            level++;
            p *= 2;
            
        }
        
        k -= prev;
        
        p /= 2;
        
        q = (n+1)/p;
        r = (n+1)%p;
        //cout << "q " << q << " r " << r << endl;
        hi = r;
        lo = level-r;
        
        if (k <= hi) ans = q+1;
        else ans = q;
        
        ans--;
        //cout << k << " " << level << " " << q << endl;
        
        cout << "Case #" << x + 1 << ": ";
        if (ans % 2 == 0) {
            cout << ans/2 << " " << (ans-1)/2 << endl;
        } else {
            cout << ans/2 << " " << ans/2 << endl;
        }
    } 
    
    return 0;
}       
