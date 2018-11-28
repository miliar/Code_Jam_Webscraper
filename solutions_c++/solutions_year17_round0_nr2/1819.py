#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>
#include <string.h>
#include <climits>

using namespace std;

int main() {
    int ite;
    cin >> ite;
    for(int tt = 1; tt <= ite; tt ++ ) {
        string s;
        cin >> s;

        for(int i=0; i<s.length() - 1; i++ ) {
            if(s[i] > s[i+1]) {
                int j = i - 1;
                while(j >= 0 && s[i] == s[j]) {
                    j -= 1;
                }
                j += 1;
                s[j] -= 1;
                for(int k=j+1; k<s.length(); k++) {
                    s[k] = '9';
                }
                break;
            }
        }
        bool st = false;
        cout << "Case #" << tt <<": ";
        for(int i=0; i<s.length(); i++ ) {
            if(!st && s[i] == '0') continue;
            st = true;
            cout << s[i];
        }
        cout << endl;
    }
    return 0;
}

