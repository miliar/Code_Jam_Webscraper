#include <iostream>
#include <algorithm>
#include <queue>
#include <stack>
#include <vector>
#include <climits>
#include <map>
#include <set>
#include <cassert>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <deque>
#include <string> 
#include <sstream>
#include <cstdlib>
#include <unordered_set>
#include <unordered_map>

using namespace std;

queue<long long> q;
set<long long> vis;
vector<long long> v;
int main(){
    ios::sync_with_stdio(false); cin.tie(0);
    q.push(0);
    while(!q.empty()){
        long long u = q.front();
        q.pop();
        if(log10(u)+1 > 18) break;
        long long last = u%10;
        for (int i = last; i < 10; ++i){
            long long p = u*10LL+i;
            if(!vis.count(p)){
                vis.insert(p);
                v.push_back(p);
                q.push(p);
            }
        }
    }
    int t; cin >>t;
    for (int i = 1; i <= t; ++i){
        long long x; cin >> x;
        int pos = lower_bound(v.begin(),v.end(),x)-v.begin();
        if(v[pos] > x) pos--;
        cout<< "Case #" << i << ": " << v[pos] << "\n";
    }
    return 0;
}

