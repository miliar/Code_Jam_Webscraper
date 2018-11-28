//
//  main.cpp
//  gcj2017_qualification_C-2
//
//  Created by 국헌 김 on 2017. 4. 9..
//  Copyright © 2017년 heonie. All rights reserved.
//

#include <iostream>
#include <queue>
#include <functional>
using namespace std;

int main(int argc, const char * argv[]) {
    int T, t;
    long N, K, i;
    cin >> T;
    for(t=1; t<=T; t++) {
        cin >> N >> K;
        priority_queue<long> max_heap;
        max_heap.push(N);
        for(i=0; i<K-1; i++) {
            long a = max_heap.top();
            max_heap.pop();
            a = a-1;
            if(a % 2 == 0) {
                max_heap.push(a/2);
                max_heap.push(a/2);
            }
            else {
                max_heap.push(((long)a/2)+1);
                max_heap.push((long)a/2);
            }
        }
        long a = max_heap.top();
        a = a-1;
        if(a % 2 == 0) {
            cout << "Case #" << t << ": " << a/2 << " " << a/2 << endl;
        }
        else {
            cout << "Case #" << t << ": " << ((long)a/2)+1 << " " << (long)(a/2) << endl;
        }
    }
    return 0;
}
