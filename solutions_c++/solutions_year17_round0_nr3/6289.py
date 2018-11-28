//
//  main.cpp
//  BathroomStalls
//
//  Created by Armaan Sethi on 4/8/17.
//  Copyright © 2017 Armaan Sethi. All rights reserved.
//

#include <iostream>
#include <queue>
#include <vector>

using namespace std;
void solve(long n, long k, long solution[]){
    priority_queue<long> partitions;
    partitions.push(n);
    long top;
    for(int i = 0; i < k-1; i++){
        top = partitions.top();
        partitions.pop();
        if(top%2 == 1){//odd
            partitions.push(top/2);
            partitions.push(top/2);
        }else{//even
            partitions.push(top/2);
            partitions.push(top/2 -1);
        }
    }
    if(partitions.top()%2 == 1){
        solution[0] = partitions.top()/2;
        solution[1] = solution[0];
    }else{
        solution[0] = partitions.top()/2;
        solution[1] = solution[0] - 1;
    }
}

int main(int argc, const char * argv[]) {
    // insert code here...
    int T;
    cin >> T;
    long N,K;
    long answer[2];

    for(int i = 0; i < T; ++i){
        cin >> N;
        cin >> K; //N>K
        solve(N,K, answer);
        cout << "Case #" << i+1 << ": " << answer[0] << " " << answer[1] << endl;
    }
    return 0;
}

