#include <iostream>
#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#define ll long long
using namespace std;
ll T;
bool is_tidy(ll n) {
    string s = to_string(n);
    for(ll i = s.size()-1; i >= 1; i--) {
        if(s[i] < s[i-1]) return false;
    }
    return true;
}
int main(int argc, const char * argv[]) {
    cin >> T;
    for(int t = 1; t <= T; t++) {
        string N;
        cin >> N;
        for(ll i = stoll(N); i >= 1; i--) {
            if( N == "111111111111111110") cout << i << endl;
            if(is_tidy(i)) {
                cout << "Case #" << t << ": " << i << endl;
                break;
            }
        }
    }
}

