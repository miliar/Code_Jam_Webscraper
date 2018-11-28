#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <queue>

#define LL long long
#define mp(x, y) make_pair(x, y)
#define pb(x) push_back(x)
#define PII pair<int, int>
#define PID pair<int, double>

using namespace std;

int T, n, k;

int main(){
    cin >> T;
    for (int id = 1; id <= T; id++) {
        cin >> n >> k;
        priority_queue<int> Q;
        Q.push(n);
        while (k--) {
            n = Q.top();
            Q.pop();
            int x = n / 2;
            Q.push(x);
            Q.push(n - 1 - x);
        }
        cout << "Case #" << id << ": " << n / 2 << ' ' << n - 1 - n / 2 << endl;
    }
}
