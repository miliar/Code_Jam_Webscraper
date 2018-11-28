#include <cmath>
#include <cstdio>
#include <vector>
#include <queue>
#include <iterator>
#include <numeric>
#include <memory>
#include <set>
#include <map>
#include <unordered_map>
#include <cstring>
#include <climits>
#include <iostream>
#include <algorithm>
using namespace std;

// #define DEBUG

uint64_t empty_score(uint64_t size, uint64_t N){
    return N - size;
}

void solve(int Tn) {
    int N, K;
    int i;
    cin >> N >> K;

    uint8_t stalls[N+2];
    for (i = 0; i < N+2; ++i) {
        stalls[i] = 0;
    }
    stalls[0] = 1;
    stalls[N+1] = 1;

    priority_queue<pair<uint64_t, uint64_t>, 
        std::vector<pair<uint64_t, uint64_t>>, 
        std::greater<pair<uint64_t, uint64_t>>> pq_space;

    pq_space.push(make_pair(empty_score(N, N + 2), 1));

    // every person
    uint64_t LS = 0;
    uint64_t RS = 0;
    for (i = 0; i < K; ++i) {
        auto space = pq_space.top();
        pq_space.pop();
        uint64_t max_size_score = space.first;
        uint64_t max_size = N +2 - max_size_score;
        uint64_t offset = (max_size - ((max_size+1) % 2)) / 2;
        uint64_t real_pos = space.second + offset;
        stalls[real_pos] = 1;


        uint64_t left_size = offset;
        uint64_t right_size = max_size - offset - 1;

        #ifdef DEBUG
        cout << "offset " << offset << endl;
        cout << "selecting " << real_pos << " stall" << endl;
        cout << "max_size " << max_size << endl;
        cout << "LS " << left_size << " RS " << right_size << endl;
        #endif

        LS = left_size;
        RS = right_size;
        

        // left
        if (LS != 0) {
            auto left_space = make_pair(empty_score(left_size, N + 2), space.second);
            pq_space.push(left_space);
        } 

        if (RS != 0) {
            auto right_space = make_pair(empty_score(right_size, N + 2), real_pos + 1);
            pq_space.push(right_space);
        }
    }


    cout << "Case #" << Tn + 1 << ": ";
    cout << max(LS, RS) << " " << min(LS, RS);
    cout << endl;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   

    int T;
    cin >> T;

    int i;
    for (i = 0; i < T; ++i) {
        solve(i);
        #ifdef DEBUG
        cout << endl;
        #endif
    }
    return 0;
}

