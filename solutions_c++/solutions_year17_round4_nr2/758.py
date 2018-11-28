//
//  b.cpp
//  
//
//  Created by Lucca Siaudzionis on 2017-05-13.
//
//

#include <map>
#include <set>
#include <tuple>
#include <cstdio>
#include <vector>
#include <string>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

//-----------------------------
#define MAXN 1010

int n, c, m;
vector<int> ticket[MAXN];
set<int> available[MAXN];

int best[MAXN];
bool used[MAXN];
vector<int> justUsed;
//-----------------------------

bool Try(int r){
    
    for(int i = 1;i <= r;i++){
        used[i] = 0;
        //available[i].clear();
        for(int j = 0;j <= n;j++) available[i].insert(j);
    }

    best[r] = 0;
    for(int p = 1;p <= c;p++){
        
        for(auto v : justUsed) used[v] = 0;
        justUsed.clear();

        for(int t : ticket[p]){
            
            int big = 0;
            int id = -1;

            for(int i = 1;i <= r;i++){
                
                if(used[i]) continue;

                set<int>::iterator it = available[i].upper_bound(t);
                it--;

                if( (*it) > big ){
                    big = *it;
                    id = i;
                }
            }

            if(!big){
                best[r] = -1;
                return false;
            }

            if(big < t) best[r]++;
            justUsed.push_back(id);
            available[id].erase(big);
        }
    }

    return true;
}

int main(){
    
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int nCases;
    cin >> nCases;

    for(int nc = 1;nc <= nCases;nc++){

        cin >> n >> c >> m;

        for(int i = 0;i < MAXN;i++) ticket[i].clear();

        for(int i = 1;i <= m;i++){
            
            int p, b;
            cin >> p >> b;
            ticket[b].push_back(p);
        }
        
        for(int i = 1;i <= c;i++) sort(ticket[i].begin(), ticket[i].end());

        memset(best, -1, sizeof best);

        int beg = 0, end = m;
        for(int i = 1;i <= c;i++) beg = max(beg, (int)ticket[i].size() - 1);

        while(beg < end-1){
            
            int mid = (beg+end)/2;

            if(Try(mid)) end = mid;
            else beg = mid;
        }

        Try(end);
        cout << "Case #" << nc << ": " << end << " " << best[end] << endl;
    }

    return 0;
}
