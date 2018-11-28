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
#include <iomanip>
#include <cstdio>

using namespace std;


bool isIncrease(long long n) {
    string s = to_string(n);
    
    for(int i = 1; i < s.size(); i++) {
        if(s[i] < s[i - 1]) {
            return false;
        }
    }
    
    return true;
}

int main() {
    int T;
    cin >> T;
    
    for (int rnd = 1; rnd <= T; rnd++) {
        long long N;
        cin >> N;
        
        while (N >= 0) {
            if (isIncrease(N)) {
                break;
            }
            N--;
        }
        
        cout << "Case #" << rnd << ": " << N << endl;
    }
    
    return 0;
}
