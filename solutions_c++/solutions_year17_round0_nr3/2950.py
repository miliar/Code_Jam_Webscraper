#include <iostream>
#include <map>

using namespace std;

int main() {
    int tc;
    cin >> tc;
    for (int c = 1; c <= tc; ++c) {
        long long n, k;
        cin >> n >> k;
        map<long long, long long> cnt;   
        cnt[n] = 1;
        pair<long long, long long> p = *(--cnt.end());
        while (k > p.second) {
            k -= p.second;
            cnt.erase(p.first);
            cnt[p.first / 2] += p.second;
            cnt[(p.first - 1) / 2] += p.second;
            p = *(--cnt.end()); 
        }
        cout << "Case #" << c << ": " << p.first / 2 << " " << (p.first - 1) / 2 << endl;
    }
    return 0;
}
