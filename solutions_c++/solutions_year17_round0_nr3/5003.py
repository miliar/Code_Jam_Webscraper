#include <iostream>
#include <queue>
using namespace std;
priority_queue<int> q;

pair<int, int> solution(int n, int k) {
    q.push(n);
    k--;
    while(k--) {
        int a = q.top() - 1;
        q.pop();
        q.push(a / 2);
        q.push(a / 2 + (a % 2));
    }
    int a = q.top() - 1;
    while(!q.empty()) {
        q.pop();
    }
    return make_pair(a / 2 + a % 2, a / 2);
}

int main() {
    int z, n, k;
    cin >> z;
    for (int nr = 1; nr <= z; nr++) {
        cin >> n >> k;
        pair<int, int> res = solution(n, k);
        cout << "Case #" << nr << ": " << res.first << " " << res.second << endl;
    }
}