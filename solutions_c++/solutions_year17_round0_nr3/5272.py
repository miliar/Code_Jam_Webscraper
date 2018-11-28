//
//  main.cpp
//  Dev
//
//  Created by 王启明 on 4/8/17.
//  Copyright © 2017 dom. All rights reserved.
//

#include <iostream>
#include <unordered_set>
#include <unordered_map>
#include <vector>
#include <cassert>
#include <string>
#include <bitset>
#include <queue>

using namespace std;

void testCase(){
    unsigned long long N, K;
    cin >> N >> K;
    
    vector<unsigned long long> container;
    container.reserve(N);
    priority_queue<unsigned long long, std::vector<unsigned long long>> pq (std::less<unsigned long long>(), std::move(container));
    pq.push(N);
    unsigned long long l, s;
    unsigned long long top;
    for(int i = 1; i < K; i++){
        top = pq.top();
        pq.pop();
        if(top % 2){
            l = s = top / 2;
        }
        else{
            l = top/2;
            s = l -1;
        }
        if(l > 0)
            pq.push(l);
        if(s > 0)
            pq.push(s);
    }
    top = pq.top();
    if(top % 2){
        l = s = top / 2;
    }
    else{
        l = top/2;
        s = l -1;
    }

    cout << l << ' ' << s;
}

int main(void){
    freopen("output.txt", "w", stdout);
    if(!freopen("input1-2.txt", "r", stdin)){
        cout << "File not exists" << endl;
        return 0;
    }
    int N;
    cin >> N;
    for(int i = 1; i <= N; i++){
        cout << "Case #" << i << ": ";
        testCase();
        cout << endl;
    }
    return 0;
}
