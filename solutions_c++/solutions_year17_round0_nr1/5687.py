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

bool check(const string& ss) {
    for (int i = 0; i< ss.size(); ++i) {
        if (ss[i] == '-') return false;
    }
    return true;
}

void convert(string& s, int start, int k) {
    for (int i = start; i< start +k; ++i) {
        if (s[i] == '-') {
            s[i] = '+';
        } else {
            s[i] = '-';
        }
    }
}

int solve(const string& str, int k) {
    string ss = str;
    int count = 0;
    for (int i = 0; i <= str.size() - k; ++i) {
        if (ss[i] == '-') {
            convert(ss, i, k);
            count++;
        }
    }
    if (check(ss)) return count;
    
    return -1;   
}

int solve() {
    string str;
    cin >> str;
    
    int k;
    cin >> k;
    
    int res1 =solve(str, k);
    
    reverse(str.begin(), str.end());
    int res2 =solve(str, k);
    
    if (res1 != -1 && res2 != -1) {
        return min(res1, res2);
    } else if (res1 != -1) {
        return res1;
    }
    
    return res2;
}

int main() {
    std::cout.precision(15);
    std::ios_base::sync_with_stdio(false);
    
    int t;
    cin >> t;
    for (int i = 1; i <=t ; ++i) {
        int res = solve();
        cout << "Case #" << i << ": ";
        if (res == -1) {
            cout << "IMPOSSIBLE";
        } else {
            cout << res;
        }
        cout << endl;
    }
    
    
    return 0;
}

