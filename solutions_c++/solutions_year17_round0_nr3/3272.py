#include <iostream>
#include <fstream>
#include <vector>
#include <queue>

using namespace std;

int main() {
    ifstream cin ("in.txt");
    ofstream cout ("out.txt");
    int T;
    int n,k;
    vector<bool> v;
    cin >> T;
    for (int cs = 1; cs <= T; cs++) {
        cin >> n >> k;
        priority_queue<int> q;
        q.push(n);
        int ans_min = n;
        int ans_max = 0;
        while (k--) {
            int temp = q.top() - 1;
            q.pop();
            int l = temp/2;
            int r = temp - l;
            ans_min = min(l, r);
            ans_max = max(l, r);
            q.push(l);
            q.push(r);
        }
        cout << "Case #" << cs << ": " << ans_max << ' ' << ans_min << endl;
    }
}