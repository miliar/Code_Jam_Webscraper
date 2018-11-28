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
#include <algorithm>¡
#include <unordered_map>
#include <unordered_set>

using namespace std;

int main() {
    ifstream cin("in.in");
    ofstream cout("out.in");

    int T;
    cin>>T;
    for (int t = 1; t<=T; t++) {
        int ans = 0;
        string s;
        int i, j, k;

        cin>>s>>k;

        for (i=0; i+k<=s.length(); i++) {
            if (s[i] == '-') {
                ans++;
                for (j=i; j<i+k; j++) {
                    if (s[j] == '+') s[j] = '-';
                    else s[j] = '+';
                }
            }
        }
        bool done = true;
        for (;i<s.length();i++) {
            if (s[i] == '-') done = false;
        }

        cout<<"Case #"<<t<<": ";
        if (done) cout<<ans<<endl;
        else cout<<"IMPOSSIBLE\n";
    }
}