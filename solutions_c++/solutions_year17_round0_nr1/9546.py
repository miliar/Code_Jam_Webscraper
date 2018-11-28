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


int main() {
    int T;
    cin >> T;
    
    for (int rnd = 1; rnd <= T; rnd++) {
        string S;
        int K;
        cin >> S >> K;
        
        int cnt = 0;
        for (int i = 0; i <= S.size() - K; i++) {
            if (S[i] == '+') {
                continue;
            }
            for (int j = i; j < i + K; j++) {
                if (S[j] == '+') {
                    S[j] = '-';
                } else {
                    S[j] = '+';
                }
            }
            cnt++;
        }
        int flag = 1;
        for (int i = S.size() - K + 1; i < S.size(); i++) {
            if (S[i] == '-') {
                flag = 0;
                break;
            }
        }
        if (flag) {
            cout << "Case #" << rnd << ": " << cnt << endl;
        } else {
            cout << "Case #" << rnd << ": IMPOSSIBLE" << endl;
        }
    }
    
    return 0;
}
