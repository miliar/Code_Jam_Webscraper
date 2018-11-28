#include<bits/stdc++.h>
using namespace std;

int main() {
    int tc = 0, N = 0, K = 0, tmpN = 0, last = 0, x = 0, y = 0;
    cin >> tc;
    for(int t = 1; t <= tc; ++t) {
        multiset<int> MS;
        cin >> N >> K;
        MS.insert(N);
        for(int i = 1 ; i < K; ++i) {
            tmpN = *MS.rbegin();
            MS.erase(prev(MS.end()));
            if(tmpN % 2 == 0) {
                MS.insert(tmpN / 2);
                MS.insert((tmpN / 2) - 1);
            }
            else {
                MS.insert(tmpN / 2);
                MS.insert(tmpN / 2);
            }
        }
        last = *MS.rbegin();
        x = last / 2;
        y = last % 2 == 0 ? (last / 2) - 1 : last / 2;
        cout << "Case #" << t << ": " << x << " " << y << endl;
    }
    return 0;
}
