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
    int t, k;
    string s;
    cin >> t;
    for(int caso=1; caso<=t; caso++) {
        cin >> s >> k;
        int eof[1001] = {0};
        int ret = 0;
        int flips = 0;
        int n = s.size();
        for(int i=0; i<n; i++) {
            int curr = (s[i]=='+')?1:0;
            flips -= eof[i];
            curr = (curr+flips)%2;
            if(!curr) {
                if(i > n-k) {
                    ret = -1;
                    break;
                }
                flips++;
                ret++;
                eof[i+k] = 1;
            }
        }
        cout << "Case #" << caso << ": ";
        if(ret < 0) cout << "IMPOSSIBLE\n";
        else cout << ret << endl;
    }
}
