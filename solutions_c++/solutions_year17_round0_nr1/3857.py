#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <algorithm>
#include <cmath>
#include <map>
#include <queue>
#include <ctime>
#include <unordered_map>
using namespace std;

clock_t begin_time, end_time;
void printtime() {
    end_time = clock();
    double elapsed_secs = double(end_time - begin_time) / CLOCKS_PER_SEC;
    cerr << "\nTime elapsed: " << elapsed_secs << endl;
}

void solve() {
    string s;
    int k;
    cin >> s >> k;
    int res = 0;
    for(int i=0;i<s.size()-k+1;i++) {
        if(s[i] == '-') {
            res ++;
            for(int j=i;j<i+k;j++) {
                if(s[j] == '+')
                    s[j] = '-';
                else
                    s[j] = '+';
            }
        }
    }
    bool ok = true;
    for(auto c: s) {
        if(c == '-')
            ok = false;
    }
    if(!ok)
        cout << "IMPOSSIBLE\n";
    else
        cout << res << endl;
}

int main() {
    begin_time = clock();

    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int tests;
    scanf("%d", &tests);
    for(int i=0;i<tests;i++) {
        printf("Case #%d: ", i + 1);
        solve();
    }

    printtime();
    return 0;
}