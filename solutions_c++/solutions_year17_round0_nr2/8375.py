#include <cstdio>
#include <queue>
#include <string>
#include <cstring>
#include <cmath>
#include <set>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef pair<int, int> P;

//int dir[] = { 0, -1, 0, 1, 0 };

int T = 0;
string curr;

bool needDecrease(const string& curr, int start) {
    char minchar = curr[start];
    for (int i = start + 1; i < curr.length(); i++) {
        if (curr[i] < curr[i-1]) {
            return true;
        }
        else if (curr[i] > curr[i-1]) {
            return false;
        }
    }
    return false;
}

string lastTidy() {
    int len = (int)curr.length();
    
    string res = curr;
    bool isSmaller = true;
    for (int i = 0; i < len; i++) {
        if (!isSmaller) {
            res[i] = '9';
        }
        else if (needDecrease(curr, i)) {
            res[i] = curr[i] - 1;
            isSmaller = false;
        }
        else {
            res[i] = curr[i];
        }
    }
    
    if (res[0] == '0') {
        return string(res, 1, len - 1);
    }
    return res;
}

int main() {
    freopen("1B_small.in", "r", stdin);
    
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cin >> curr;
        
        printf("Case #%d: ", t);
        cout << lastTidy() << endl;
    }
    
    return 0;
}
