#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <stdlib.h>     /* abs */

using namespace std;

#define MAX 1e17
 

int main(){
    std::set<long long>::iterator it;
    int t;
    cin >> t;
    for(int Case=1; Case<=t; Case++){
        long long mx,   mi;
        long long n, k;
        cin >> n >> k;
        set<long long>s;
        map<long long, long long> m;
        s.insert(n);
        m[n] = 1;
        while( k>0 ){
            it = s.end();
            it--;
            long long val = *it;
            if(val%2)
                mi = val/2;
            else if(val>0)
                mi = val/2-1;

            if(val%2)
                mx = val/2;
            else
                mx = val/2;

            if (m[val] >= k)
                break;
            k -= m[val];
            s.erase(val);
            m[mi] += m[val];
            s.insert(mi);
            m[mx] += m[val];
            s.insert(mx);
            m[val] = 0;
        }
        cout << "Case #" << Case << ": " << mx << " " <<  mi << endl;
    }
    return 0;
}