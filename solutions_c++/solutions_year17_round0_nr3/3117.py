#include<stdio.h>
#include<string.h>
#include<memory.h>
#include<algorithm>
#include <map>
#include <unordered_map>
#include<utility>
#include<iostream>
#include<math.h>
#include<vector>
#include <queue>

using namespace std;

pair<long long, long long> Div2(long long sz) {
    return {sz/2+ sz%2, sz/2};
};
pair<long long, long long>  solveCase(long long n, long long k) {
    long long levelCov;
    levelCov = 0;
    while (levelCov * 2 +1 < k) {
            levelCov  = levelCov * 2 + 1;
    }

    long long remCells = n-levelCov;
    long long intervals = levelCov + 1;
    long long size = remCells / intervals;
    long long largerIntervals = remCells % intervals;
    if(k-levelCov <=largerIntervals) {
        return Div2(size);
        } else {
        return Div2(size-1);
    }

}



pair<long long, long long>  solveCase2(long long n, long long k) {
    priority_queue<long long> Q;
    Q.push(n);
    for(int i=0;i<k;i++) {
        long long el = Q.top();
        Q.pop();
        auto nel = Div2(el-1);
        if(i==k-1)
            return {nel.first, nel.second};
        else {
            Q.push(nel.first);
            Q.push(nel.second);
        }
    }

}

int main() {
    int testCases;
    cin >> testCases;
    for(int i=0;i<testCases; i++) {
        long long n,k;
        cin >> n>>k;
        auto ans = solveCase(n,k);
        cout << "Case #" << (i+1) <<": " << ans.first << " " << ans.second << endl;
    }

}