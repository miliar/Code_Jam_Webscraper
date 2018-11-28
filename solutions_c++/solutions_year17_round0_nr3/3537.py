
#include <iostream>
#include <vector>
#include <string>
#include <math.h>
#include <set>
#include <unordered_set>
#include <queue>
#include <cstdio>
#include <queue>
#include <stack>
#include <unordered_map>
#include <sstream>

using namespace std;


pair<int, int> stall(int n, int k) {
    priority_queue<int> pq;
    pq.push(n);
    
    int large = 0, small = 0;
    for (int i = 0; i < k; ++i) {
        if (pq.empty() || pq.top() <= 1) return {0, 0};
        int last = pq.top(); pq.pop();
        
        
        large = last / 2;
        small = last - 1 - large;
        
        if (small > 0) pq.push(small);
        pq.push(large);
    }
    
    
    return {large, small};
}

int main(){
    int num; cin >> num;

    int n, k;
    for (int i = 0; i < num; ++i) {
        cin >> n >> k;
        auto res = stall(n, k);
        cout << "Case #" << (i+1) << ": " << res.first << ' ' << res.second << endl;
    }
    
    return 0;
}
