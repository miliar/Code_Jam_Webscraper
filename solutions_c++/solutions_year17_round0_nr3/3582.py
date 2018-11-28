#include <iostream>
#include <functional>
#include <string>
#include <vector>
#include <queue>
using namespace std;

void bathroom(int n, int k) {
//    if (k > n/2) {
//        cout << "0 0";
//        return;
//    }
    priority_queue<int> pq;
    pq.push(n);
    for (int i = 0; i < k - 1; i++) {
        int curr = pq.top();
        pq.pop();
        pq.push((curr-1)/2);
        pq.push(curr - (curr-1)/2 - 1);
    }
    int curr = pq.top();
    cout << curr - (curr-1)/2 - 1 << " " << (curr-1)/2;
}

int main() {
    int t, n, k;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        cin >> n >> k;
        cout << "Case #" << i << ": ";
        bathroom(n, k);
        cout << endl;
    }
    return 0;
}
