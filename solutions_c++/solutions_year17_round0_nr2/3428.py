
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
string tidy(string str) {
    
    vector<int> s;
//implement s
    for (char c : str) s.push_back(c - '0');
    
    int loc = 0;
    int i = 1;
    for (; i < s.size(); ++i) {
        if (s[i] > s[loc]) {
            loc = i;
        }
        else if (s[i] < s[loc]) break;
    }
    
    if (i < s.size()) {
        if (loc == 0 && s[loc] == 1) {
//        TODO: fill this case
            s.erase(s.begin());
            for (int j = 0; j < s.size(); ++j) s[j] = 9;
        }
        else {
            s[loc] -= 1;
            for (int j = loc+1; j < s.size(); ++j) s[j] = 9;
        }
    }
    
    string res;
    for (int n : s) res.push_back(n + '0');
    
    return res;
}

int main(){
    
    int num; cin >> num;
    string temp;
    for (int i = 0; i < num; ++i) {
        cin >> temp;
        string res = tidy(temp);
        cout << "Case #" << (i+1) << ": " << res << endl;
    }
    
    
    return 0;
}
