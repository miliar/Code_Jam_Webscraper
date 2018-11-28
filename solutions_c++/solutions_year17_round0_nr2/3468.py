#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

long long len(long long n) {
    int i = 0;
    while(n>0) {
        n/=10;
        ++i;
    }
    return i;
}

long long index(long long n, int idx) {
    vector<int> a;
    while(n>0) {
        a.insert(a.begin(), n%10);
        n/=10;
    }
    return a[idx];
}

long long michev(long long n, int idx) {
    vector<int> a;
    while(n>0) {
        a.insert(a.begin(), n%10);
        n/=10;
    }
    long long ans=0;
    for(int i=0; i<idx; ++i) {
        ans *= 10;
        ans += a[i];
    }
    return ans;
}

long long ans;

bool solve(long long n, long long val, int i, int k) {
    if(i==k-1) {
        for(long long j=9; j>=val%10; --j) {
            if(val < n/10) {
                ans = val*10 + j;
                return true;
            }
            else {
                if(val > n/10)
                    cout << "ERROOOOOOR " << val << ' ' << n << endl;
                if(val*10 + j <= n) {
                    ans = val*10 + j;
                    return true;
                }
            }
        }
        return false;
    }
    if(val < michev(n, i)) {
        if(!solve(n, val*10 + 9, i+1, k))
            cout << "ERRORRR 2 " << endl;
        return true;
    }
    else {
        if(val%10>index(n, i))
            return false;
        if(solve(n, val*10 + index(n, i), i+1, k))
            return true;
        if(val%10>index(n, i)-1)
            return false;
        if(!solve(n, val*10 + index(n, i)-1, i+1, k))
            cout << "ERRORR 3" << endl;
        return true;
    }
}

int main() {
    long long t, n, tt;
    fin >> t;
    for(int tt = 1; tt <= t; ++tt) {
        fin >> n;
        solve(n, 0, 0, len(n));
        fout << "Case #" << tt << ": " << ans << endl;
    }
    return 0;
}