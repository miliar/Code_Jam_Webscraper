#include <iostream>
#include <cmath>
#include <string>
#include <cstring>
#include <queue>
#include <algorithm>

using namespace std;

int T, N, K, clargest, lx, ly, depth;


int main() {
    cin >> T;
    for (int i = 1; i <= T; i++) {
        cin >> N >> K;
        std::priority_queue<int, std::vector<int>, std::less<int> > q;
        q.push(N);
        for (int j = 0; j < K; j++) {
            int largest = q.top();
            q.pop();
            // cout << largest << endl;
            int x;
            int y;
            if (largest % 2 == 0) {
                x = largest/2;
                y = x-1;
            }
            else {
                x = largest /2;
                y = x;
            }
            if (j == K -1) {
                cout << "Case #" << i << ": " << x << " " << y << endl;
                break;
            }
            q.push(x);
            q.push(y);

            
            // if (j == K -1) {
            //     cout << "Case #" << i << ": " << y-mid << " " << mid-x << endl;
            //     break;
            // }
            

        }
    }


}