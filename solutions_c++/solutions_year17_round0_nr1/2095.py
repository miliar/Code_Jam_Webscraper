#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <queue>
#include <cassert>
#include <unordered_map>
#include <fstream>
#define ll long long
#define F first
#define S second
#define MOD 1000000007
#define MAX 200001
#define BUGGY 0
using namespace std;
int main(){
    ifstream cin("/Users/shikhar.s/Downloads/A-large.in");
    //ifstream cin("/Users/shikhar.s/Desktop/Competitive/Competitive/a.txt");
    ofstream cout("/Users/shikhar.s/Desktop/Competitive/Competitive/b.txt");
    int t;
    cin >> t;
    int T = 1;
    while (t--) {
        string s;
        int k;
        cin >> s >> k;
        int ans = 0;
        int l = s.length();
        for (int i = 0;i < l; ++i) {
            if (s[i] == '-') {
                if ((i + k) > l) {
                    ans = -1;
                    break;
                } else {
                    for (int j = i;j < (i + k); ++j)
                        s[j] = (s[j] == '-') ? '+' : '-';
                    ++ans;
                }
            }
        }
        cout << "Case #" << T++ << ": ";
        if (ans == -1) cout << "IMPOSSIBLE\n";
        else cout << ans << "\n";
    }
    return 0;
}

