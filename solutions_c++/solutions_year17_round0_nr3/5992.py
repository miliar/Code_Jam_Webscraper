#include <iostream>
#include <map>
using namespace std;

int main() {
    int T;
    cin >> T;
    for(int t = 1; t <= T; ++t) {
        cout << "Case #" << t << ": ";

        map<long long, long long> chunks;
        long long N, K;
        cin >> N >> K;

        chunks[N] = 1;
        while(--K) {
            long long i = chunks.rbegin()->first;
            long long l = (i - 1) / 2;
            long long r = (i - 1) / 2 + (i - 1) % 2;
            if(chunks[i] == 1) {
                chunks.erase(i);
            } else {
                --chunks[i];
            }
            ++chunks[l];
            ++chunks[r];
        }
        long long i = chunks.rbegin()->first;
        long long l = (i - 1) / 2;
        long long r = (i - 1) / 2 + (i - 1) % 2;
        cout << r << " " << l << endl;
    }
    return 0;
}
