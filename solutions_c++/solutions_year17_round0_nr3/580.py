#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <climits>

using namespace std;

#define ull unsigned long long

int main() {
    int T; cin >> T;
    for(int cs = 1; cs <= T; cs++) {
        cout << "Case #" << cs << ": ";
        ull N, K; cin >> N >> K;
        map<ull,ull> m;
        m[N] = 1;
        while(true) {
            auto it = m.end();
            it--;
            ull len = it->first, qt = it->second;
            m.erase(it);
            len--;
            if(K <= qt) {
                cout << len - len/2 << " " << len/2 << endl;
                break;
            }
            K -= qt;
            if(m.find(len/2) == m.end())
                m[len/2] = qt;
            else
                m[len/2] += qt;
            if(m.find(len-len/2) == m.end())
                m[len-len/2] = qt;
            else
                m[len-len/2] += qt;
        }
    }
    return 0;
}
