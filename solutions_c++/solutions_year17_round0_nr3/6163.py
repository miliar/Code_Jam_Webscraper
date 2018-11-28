#include <iostream>
#include <string>
#include <queue>
#include <vector>
#include <functional>
using namespace std;
int main() {
    int ts;
    cin >> ts;
    for (int t = 1; t <= ts; t++) {
        priority_queue<int, vector<int>, less<int> > q;
        int n,k;
        cin >> n >> k;
        int nowMin = 0;
        int nowMax = 0;
        q.push(n);
        for (int i = 0; i < k; i++) {
            int now;
            now = q.top();
            q.pop();
            now--;
            if((now % 2) == 0) {
                nowMax = now / 2;
                nowMin = now / 2;
            }else {
                nowMax = (now / 2) + 1;
                nowMin = now / 2;
            }
            q.push(nowMax);
            q.push(nowMin);
        }
        cout << "Case #" << t << ": " << nowMax << " " << nowMin << endl;
    }
    return 0;
}
