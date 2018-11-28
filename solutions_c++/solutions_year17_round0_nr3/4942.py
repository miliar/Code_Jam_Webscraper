#include <queue>
#include <iostream>
using namespace std;

int n, k;
priority_queue<int> pq;

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int cases;
    cin >> cases;

    for(int tt = 1;tt <= cases;tt++){

        while(!pq.empty()) pq.pop();

        cin >> n >> k;
        pq.push(n);

        int r1 = 0, r2 = 0;

        for(int i = 1;i <= k;i++){

            int cur = pq.top();
            pq.pop();

            r1 = (cur)/2;
            r2 = (cur-1)/2;

            pq.push(r1);
            pq.push(r2);
        }

        cout << "Case #" << tt << ": " << r1 << " " << r2 << endl;
    }
    return 0;
}
