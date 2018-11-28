#include <cstdio>
#include <algorithm>
#include <string>
#include <map>
#include <vector>
#include <iostream>

typedef unsigned long long ull;
using namespace std;
int T;
ull N, K, depth;
ull decision(ull n, ull k) {
    // 왼쪽 true, 오른쪽 false
    if(k == 1)
        return n;
    map<ull, ull> lhsh, rhsh;
    depth = 1;
    while(true) {
        ull po = (ull)1 << depth;
        if(k < po) {
            depth--;
            break;
        }
        depth++;
    }
    if(n % 2) {
        lhsh[n / 2] = 1;
        rhsh[n / 2] = 1;
    }
    else {
        lhsh[n / 2 - 1] = 1;
        rhsh[n / 2] = 1;
    }
    for(int i = 1; i < depth; ++i) {
        map<ull, ull> newlhsh, newrhsh;
        for(auto it : lhsh) {
            if(it.first % 2) {
                if(newlhsh.find(it.first / 2) == newlhsh.end())
                    newlhsh[it.first / 2] = it.second * 2;
                else
                    newlhsh[it.first / 2] += it.second * 2;
            }
            else {
                if(newlhsh.find(it.first / 2) == newlhsh.end())
                    newlhsh[it.first / 2] = it.second;
                else
                    newlhsh[it.first / 2] += it.second;

                if(newlhsh.find(it.first / 2 - 1) == newlhsh.end())
                    newlhsh[it.first / 2 - 1] = it.second;
                else
                    newlhsh[it.first / 2 - 1] += it.second;
            }
        }
        lhsh = newlhsh;

        for(auto it : rhsh) {
            if(it.first % 2) {
                if(newrhsh.find(it.first / 2) == newrhsh.end())
                    newrhsh[it.first / 2] = it.second * 2;
                else
                    newrhsh[it.first / 2] += it.second * 2;
            }
            else {
                if(newrhsh.find(it.first / 2) == newrhsh.end())
                    newrhsh[it.first / 2] = it.second;
                else
                    newrhsh[it.first / 2] += it.second;

                if(newrhsh.find(it.first / 2 - 1) == newrhsh.end())
                    newrhsh[it.first / 2 - 1] = it.second;
                else
                    newrhsh[it.first / 2 - 1] += it.second;
            }
        }
        rhsh = newrhsh;

    }
    ull haha = (ull)1 << depth;
    haha--;
    auto lit = lhsh.rbegin();
    auto rit = rhsh.rbegin();
   // cout << "hsh size " << lhsh.size() << " " << rhsh.size() << endl;
    while(true) {
        if(lit == lhsh.rend() && rit == rhsh.rend())
            break;
        if(lit == lhsh.rend()) {
            haha += rit->second;
            if(k <= haha)
                return rit->first;
            rit++;
        }
        else if(rit == rhsh.rend()) {
            haha += lit->second;

            if(k <= haha)
                return lit->first;
            lit++;
        }
        else if(lit->first >= rit->first)
        {
            haha += lit->second;
            if(k <= haha)
                return lit->first;
            lit++;

        }
        else {
            haha += rit->second;
            if(k <= haha)
                return rit->first;
            rit++;
        }
    }
    cout << "error" << lhsh.size() << " " << rhsh.size() << endl;
    return true;
}
int main() {
    freopen("C-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> T;
    for(int test = 1; test <= T; ++test) {
        cin >> N >> K;
        ull ret = decision(N, K);
        if(ret % 2) {
            printf("Case #%d: %llu %llu\n", test, ret / 2, ret / 2);
        }
        else {
            printf("Case #%d: %llu %llu\n", test, ret / 2, ret / 2 - 1);
        }
    }
    return 0;
}