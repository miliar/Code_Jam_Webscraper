#include <cstdlib>
#include <iostream>
#include <map>
#include <tuple>

using namespace std;

tuple<long long, long long> solve(long long N, long long K) {
    long long L, R, d, r;
    
    map<long long, long long> m;
    m[N] = 1;
    
    long long i = 1;
    while(i <= K) {
        map<long long, long long>::reverse_iterator it = m.rbegin();
        long long length = it->first;
        
        L = length / 2 + length % 2 - 1;
        if(L < 0) {
            L = 0;
        }
        
        R = length - 1 - L;
        if(R < 0) {
            R = 0;
        }
        
        long long count = min(it->second, K - i + 1);
        it->second -= count;
        if(it->second <= 0) {
            m.erase(length);
        }
        
        if(L > 0) {
            m[L] += count;
        }
        
        if(R > 0) {
            m[R] += count;
        }
        
        i += count;
    }
    
    return make_tuple(max(L, R), min(L, R));
}
/*
 * 
 */
int main(int argc, char** argv) {
    int T;
    long long N, K, L;
    tuple<long long, long long> result;
    
    cin >> T;
    for(int i = 1; i <= T; ++i) {
        cin >> N >> K;
        
        result = solve(N, K);
        cout << "Case #" << i << ": " << get<0>(result) << " " << get<1>(result) << "\n";
    }
    
    return 0;
}

