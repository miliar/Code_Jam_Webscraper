#include <iostream>
#include <bitset>
#include <sstream>
#include <memory>
#include <limits>
#include <list>
#include <stack>
#include <set>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <string>
#include <vector>
#include <algorithm>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <queue>


using namespace std;

void recalc(vector<bool>& people, vector<int>& ls, vector<int>& rs) {
    for (int i = 0; i < ls.size(); ++i) {
        if (people[i]) continue;
        for (int j = i-1; j >=0; --j) {
            if (people[j]) {
                ls[i] = i-j;
                break;
            }
        }
        for (int j = i+1; j < ls.size(); ++j) {
            if (people[j]) {
                rs[i] = j-i;
                break;
            }
        }
    }
    
}

pair<int,int> solve() {
    int n,k;
    cin >> n >> k;
    
    vector<bool> people(n+2, false);
    vector<int> people_idx(n+2, -1);
    
    people[0] = true;
    people.back() = true;
    
    
    vector<int> ls(n+2, 0);
    vector<int> rs(n+2, 0);
    recalc(people, ls, rs);
    
    for (int i = 0; i < k; ++i) {
        int best_idx = -1;
        int max_min_l_r = -1;
        int max_max_l_r = -1;
        
        for (int j = 0; j < ls.size(); ++j) {
            if (people[j]) continue;
            
            if (min(ls[j], rs[j]) > max_min_l_r) {
                max_min_l_r = min(ls[j], rs[j]);
                max_max_l_r = max(ls[j], rs[j]);
                best_idx = j;
            } else if ((min(ls[j], rs[j]) == max_min_l_r) && (max(ls[j], rs[j]) > max_max_l_r)) {
                max_min_l_r = min(ls[j], rs[j]);
                max_max_l_r = max(ls[j], rs[j]);
                best_idx = j;
            }
        }
        
        if (i == k-1) {
            people_idx[best_idx] = i;
            /*
            for (int jj = 0; jj < people_idx.size(); ++jj) {
                cout <<people_idx[jj] << " ";
            }*/
            
            return {max_max_l_r, max_min_l_r};
        }
        people[best_idx] = true;
        people_idx[best_idx] = i;
        recalc(people, ls, rs);
    }
    
    return {-1,-1};
}

int main() {
    std::cout.precision(15);
    std::ios_base::sync_with_stdio(false);
    
    int t;
    cin >> t;
    for (int i = 1; i <=t ; ++i) {
        cout << "Case #" << i << ": ";
        pair<int,int> p = solve();
        
        cout << p.first-1 << " " << p.second-1;
        cout << endl;
    }
    
    
    return 0;
}

