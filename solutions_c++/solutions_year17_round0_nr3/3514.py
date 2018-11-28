//
//  main.cpp
//  Bathroom
//
//  Created by Guanyao Huang on 4/7/17.
//  Copyright © 2017 Guanyao Huang. All rights reserved.
//

#include <iostream>
#include <queue>  
#include <utility> 

using namespace std;
typedef unsigned long long ull;
bool compare(pair<ull, ull> lhs, pair<ull, ull> rhs){
    if(lhs.second-lhs.first > rhs.second-rhs.first){
        return false;
    }
    else if(lhs.second-lhs.first < rhs.second-rhs.first){
        return true;
    }
    else{
        if (lhs.first < rhs.first)
            return false;
        else
            return true;
    }
}
int main(int argc, const char * argv[]) {
    // insert code here...
    int T;
    cin >> T;
    for(int i=0; i<T; i++){
        ull N, K;
        cin >> N >> K;
        if(N == K){
            cout<< "Case #"<<i+1<<": 0 0"<<endl;
            continue;
        }
        priority_queue<pair<ull, ull>, vector<pair<ull,ull> >, std::function<bool(pair<ull,ull>, pair<ull,ull>) > > pq(compare);
        pair<ull, ull> start((ull)1, N);
        pq.push(start);
        ull maxR, minR;
        ull added = 0;
        while(pq.size()>0 && added<K){
            pair<ull, ull> topV = pq.top();
            pq.pop();
            if(topV.second > topV.first){
                ull mid = (topV.first) + (topV.second-topV.first)/(ull)2;
                maxR = topV.second - mid;
                minR = mid - topV.first;
                if(maxR>0){
                    pair<ull, ull> newP(mid+(ull)1, topV.second);
                    pq.push(newP);
                }
                if(minR>0){
                    pair<ull, ull> newP(topV.first, mid-(ull)1);
                    pq.push(newP);
                }
            }
            else{
                maxR = 0;
                minR = 0;
            }
            added ++;
        }
        cout<< "Case #"<<i+1<<": "<<maxR<<" "<<minR<<endl;
    }
    return 0;
}
