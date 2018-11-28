#include <algorithm>
#include <bitset>
#include <ctime>
#include <cstdlib>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>
using namespace std;

int main() {
    int NC;
    cin >> NC;
    for (int nc = 1; nc <= NC; nc++) {
        int N, K;
        cin >> N >> K;
        int minn = 0;
        int maxn = 0;
        priority_queue<int> pq;
        pq.push(N);
        for (int k = 0; k < K; k++) {
            int newn = pq.top();
            pq.pop();
            if (newn % 2) {
                minn = newn/2;
                maxn = minn;
                if (newn > 2) {
                    pq.push(minn);
                    pq.push(minn);
                }
            } else {
                    minn = (newn / 2) - 1;
                    maxn = minn + 1;
                    if (minn > 0) pq.push(minn);
                    pq.push(maxn);
            }
        }
        cout << "Case #" << nc << ": ";
        cout << maxn << " " << minn;
        cout << endl;
    }
}
