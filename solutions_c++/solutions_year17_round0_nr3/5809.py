#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

string compute(const intmax_t n, intmax_t k)
{
    intmax_t max_ls_rs = -1;
    intmax_t min_ls_rs = -1;
    
    const intmax_t size = n + 2;
    vector<bool> stalls(size, false);
    stalls[0] = true;
    stalls[size - 1] = true;
    
    vector<intmax_t> occupied;
    occupied.push_back(0);
    occupied.push_back(size - 1);
    
    intmax_t last_max_ls_rs = -1;
    intmax_t last_min_ls_rs = -1;
    
    // for each person
    for (intmax_t p = 0; p < k; ++p)
    {
        intmax_t maximal_min_ls_rs = -1;
        
        map<intmax_t, pair<intmax_t, intmax_t>> sets;
        // for each stall
        for (intmax_t s = 1; s < size - 1; ++s)
        {
            if (find(begin(occupied), end(occupied), s) != end(occupied)) {
                continue; // stall is already occupied, skip it
            }
            intmax_t ls = INTMAX_MAX;
            intmax_t rs = INTMAX_MAX;
            for (auto o : occupied) {
                if (o < s) {
                    auto ls_o = abs(o - s) - 1; // nb of empty stalls
                    if (ls_o < ls) ls = ls_o;
                } else if (o > s) {
                    auto rs_o = abs(o - s) - 1; // nb of empty stalls
                    if (rs_o < rs) rs = rs_o;
                }
//                cout << "occupied " << o << ": " << ls << ", " << rs << endl;
            }
//            cout << "stall " << s << ": " << ls << ", " << rs << endl;
            
            intmax_t min_ls_rs = min(ls, rs);
            if (min_ls_rs > maximal_min_ls_rs ) {
                sets.clear();
                maximal_min_ls_rs = min_ls_rs;
                sets[s] = {ls, rs};
//                cout << "    reset and add " << ls << ", " << rs << "  " << sets.size() << endl;
            } else if (min_ls_rs == maximal_min_ls_rs ) {
                sets[s] = {ls, rs};
//                cout << "    add " << ls << ", " << rs << "  " << sets.size() << endl;
            }
            
        }
        if (sets.size() == 1) {
            occupied.push_back((*sets.begin()).first); // one candidate, use it
            intmax_t ls = (*sets.begin()).second.first;
            intmax_t rs = (*sets.begin()).second.second;
//            cout << "ls " << ls << ", rs " << rs << endl;
            last_min_ls_rs = min( ls, rs );
            last_max_ls_rs = max( ls, rs );
            continue;
        }
        
        intmax_t maximal_max_ls_rs = -1;
        map<intmax_t, pair<intmax_t, intmax_t>> sets2;
        
        for (auto set : sets) {
            intmax_t s = set.first;
            intmax_t ls = set.second.first;
            intmax_t rs = set.second.second;
//            cout << "candidate: " << set.second.first << ", " << set.second.second << endl;
            intmax_t max_ls_rs = max(ls, rs);
            if (max_ls_rs > maximal_max_ls_rs ) {
                sets2.clear();
                maximal_max_ls_rs = max_ls_rs;
                sets2[s] = {ls, rs};
//                cout << "    reset and add " << ls << ", " << rs << "  " << sets2.size() << endl;
            } else if (max_ls_rs == maximal_max_ls_rs ) {
                sets2[s] = {ls, rs};
//                cout << "    add " << ls << ", " << rs << "  " << sets2.size() << endl;
            }
        }
        
        occupied.push_back((*sets2.begin()).first); // one candidate, use it
        intmax_t ls = (*sets2.begin()).second.first;
        intmax_t rs = (*sets2.begin()).second.second;
        last_min_ls_rs = min( ls, rs );
        last_max_ls_rs = max( ls, rs );
    }
    
    return to_string(last_max_ls_rs) + " " + to_string(last_min_ls_rs);
}

int main() {
    int t;
    cin >> t;  // read T
    for (int i = 1; i <= t; ++i) {
        intmax_t n, k;
        cin >> n; // read N
        cin >> k; // read K
        cout << "Case #" << i << ": " << compute(n, k) << endl;
    }
}
