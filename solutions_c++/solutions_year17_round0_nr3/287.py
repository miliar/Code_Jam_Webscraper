#define STRINGIZE(x) #x
#define STRINGIZE2(x) STRINGIZE(x)
#define FP STRINGIZE2(FILEPATH)

#include <iostream>
#include <cstdio>
#include <cassert>
#include <string>
#include <set>
#include <map>
#include <vector>
using namespace std;

long long n, k;

bool read() {
    cin >> n >> k;
    return true;
}

void solve(int test) {
    printf("Case #%d: ", test + 1);
    
    map<long long, long long> s;
    s[n] = 1;
    
    long long last = 0;
    while (k > 0) {
        map<long long, long long>::iterator it = prev(s.end());
        if (it->second == 0 || it->first == 0) {
            s.erase(it);
            continue;
        }
        
        last = it->first;
        long long cur = min(k, it->second);
        it->second -= cur;
        k -= cur;
        
        long long x = (it->first - 1) / 2;
        long long y = it->first / 2;
        
        s[x] += cur;
        s[y] += cur;
    }
    
    cout << last / 2 << ' ' << (last - 1) / 2 << endl;
}

int main() {
    freopen(FP "input.txt", "rt", stdin);
    freopen(FP "output.txt", "wt", stdout);
    
    int testCount;
    cin >> testCount;
    
    for (int test = 0; test < testCount; test++) {
        assert(read());
        solve(test);
    }
    
    return 0;
}
