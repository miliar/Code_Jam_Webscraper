#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cmath>
#include <sstream>
#include <iterator>
#include <queue>
    
using namespace std;

pair<int, int> findLastBathroomStall(int N, int K) {

    priority_queue<int> Q;
    int max = 0;
    int min = 0;
    Q.push(N);
    for (int i = 0; i < K; i++) {
        int top = Q.top();
        max = top/2;
        min = (top - 1)/2;
        Q.pop();
        Q.push(min);
        Q.push(max);
    }

    return make_pair(max, min);
    
}

int main() {
    int n;
    cin >> n;
    vector<pair<int, int> > Z(n);
    for (int i = 0; i < n; i++) {
        int a, b;    
        cin >> a >> b;
        Z[i] = make_pair(a, b);
    }

    for (int i = 0; i < n; i++) {
        cout << "Case #" << (i + 1) << ": ";
        pair<int, int> output = findLastBathroomStall(Z[i].first, Z[i].second);
        cout << output.first << " " << output.second << endl;
    }
    return 0;
}
