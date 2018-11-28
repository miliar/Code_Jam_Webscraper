
#include <iostream>
#include <vector>
#include <string>
#include <math.h>
#include <set>
#include <unordered_set>
#include <queue>
#include <cstdio>
#include <queue>
#include <stack>
#include <unordered_map>
#include <sstream>

using namespace std;


// fliper method
int fliper(vector<bool>& vec, int k) {
    if (k > vec.size()) return -1;
    
    int i = 0, res = 0;
    while (i+k-1 < vec.size()) {
        while (i+k-1 < vec.size() && vec[i]) ++i;
        if (i+k-1 >= vec.size()) break;
        
//    TODO: deal with flip and find new location for i
        int temp = i+k;
        for (int j = i+k-1; j >= i; --j) {
            if (vec[j]) temp = j;
            vec[j] = !vec[j];
        }
        i = temp;
        res++;
        
    }
    
//check i to end of vec, if all == true;
    while (i < vec.size()) {
        if (!vec[i]) return -1;
        ++i;
    }
    
    return res;
}


int main(){
    
    int num; cin >> num;
    
    string s;
    int k;
    for (int i = 0; i < num; ++i) {
        cin >> s; cin >> k;
        
        vector<bool> vec;
        // construct vec<bool>
        for (char c : s) {
            if (c == '+') vec.push_back(true);
            else vec.push_back(false);
        }

        int res = fliper(vec, k);
        
        string res_s = to_string(res);
        if (res_s == "-1") res_s = "IMPOSSIBLE";
        
        cout << "Case #" << (i+1) << ": " + res_s << endl;
        
    }
    
    return 0;
}
