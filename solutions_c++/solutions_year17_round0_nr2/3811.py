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

bool ok(string s) {
    for(int i=1;i<s.size();i++) {
        if(s[i-1] > s[i])
            return false;
    }
    return true;
}

void solve() {
    string s;
    cin >> s;
    if(ok(s)) {
        cout << s << endl;
        return;
    }

    for(int i=1;i<s.size();i++) {
        if(s[i-1] > s[i]) {
            int it = i;
            while(it > 0 && s[it-1] > s[it]) {
                it--;
                s[it]--;
            }
            for(int j=it+1;j<s.size();j++)
                s[j] = '9';
            for(int j=0;j<s.size();j++) {
                if(s[j] != '0') {
                    s = s.substr(j);
                    break;
                }
            }
            cout << s << endl;
            return ;
        }
    }
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