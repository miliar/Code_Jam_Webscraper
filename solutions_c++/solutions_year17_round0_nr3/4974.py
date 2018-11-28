//
// Created by Taewoo Kim on 4/8/2017.
//

#include <iostream>
#include <queue>
#include <utility>

using namespace std;

pair<long long, long long> stalls(long long n, long long k){
    //if (k > n/2+1) return make_pair(0,0);//wrong

    priority_queue<long long> pq;//max heap

    pq.push(n);
    k--;

    while (k > 0){
        long long c = pq.top();
        pq.pop();
        pq.push(c - 1 - c/2);
        pq.push(c/2);
        k--;
    }
    long long a = pq.top();
    return make_pair(a/2, a - 1 - a/2);
};

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++){
        long long n, k;//n stalls, k people
        cin >> n >> k;
        auto ans = stalls(n, k);
        cout << "Case #" << i << ": " << ans.first << " " << ans.second << endl;
    }
    return 0;
}