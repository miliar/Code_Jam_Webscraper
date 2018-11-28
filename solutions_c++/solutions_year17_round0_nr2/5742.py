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

using namespace std;

int main()
{
    int T;
    string n;
    cin >> T;
    for(int caso=1; caso<=T; caso++) {
        cin >> n;
        int len = n.size();
        string res = "";
        bool done = false;

        if(n[0] == '1') {
            for(int i=0; i<len; i++) {
                if(n[i] == '0') {
                    for(int i=0; i<len-1; i++) res += '9';
                    done = true;
                    break;
                }
                if(n[i] > '1') break;
            }
        }

        if(!done) {
            for(int i=0; i<len; i++) {
                bool ok = true;
                for(int j=i+1; j<len; j++) {
                    if(n[j] < n[i]) ok = false;
                    if(!ok || n[j] > n[i]) break;
                }
                if(ok) {
                    res += n[i];
                } else {
                    res += n[i]-1;
                    for(int j = i+1; j<len; j++) res += '9';
                    break;
                }
            }
            done = true;
        }

        cout << "Case #" << caso << ": " << res << endl;
    }
}
