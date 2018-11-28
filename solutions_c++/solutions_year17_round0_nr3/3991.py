#include <iostream>

using namespace std;

struct MinMax {
    long long min, max;
};

int log2(long long n) {
    if(n <= 0)
        throw "wtf";
    
    for(int i=0; true; ++i) {
        if(n == 1)
            return i;
        n = n >> 1;
    }
}

long long pow2(int i) {
    return 1 << i;
}

MinMax solve(long long n, long long k) {
    int i = log2(k);
    long long ni = n + 1 - pow2(i);
    long long ki = pow2(i);
    long long sim1 = ki - 1;
    
    long long smaller = ni / ki;
    long long bigger = smaller + 1;
    
    long long bigger_no = ni - ki * smaller;
    long long no_in_row = k - sim1;
    
    long long length = no_in_row <= bigger_no ? bigger : smaller;
    
    MinMax mm;
    mm.min = (length - 1) / 2;
    mm.max = length / 2;
    return mm;
}

int main(int argc, char** argv) {
    int t;
    long long n, k;
    
    cin >> t;
    
    for(int i=0;i<t;++i) {
        cin >> n >> k;
        MinMax res = solve(n, k);
        
        cout << "Case #" << (i+1) << ": " << res.max << " " << res.min << endl;
    }
    
    return 0;
}
