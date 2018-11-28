#include<iostream>
#include<map>
#include<cstring>
#include<climits>
#include<fstream>
#include<string>
#include<cmath>

using namespace std;

int T, K, ans;
string S;

void dfs(string copys, int count) {
    // cout << copys << " " << count << endl;
    bool flag = false;
    for (int i = 0; i < copys.size(); i++) {
        if (copys[i] == '-' && i+K <= copys.size()) {
            flag = true;
            string _copys = copys;
            int j = 0;
            while (j <= K-1) {
                if (_copys[i+j] == '-') {
                    _copys[i+j] = '+';
                } else {
                    _copys[i+j] = '-';
                }
                j++;
            }
            dfs(_copys, count + 1);
            break;
        }
        if (copys[i] == '-' && i+K > copys.size()) {
            flag = true;
            break;
        }
    }
    if (!flag) {
        //cout << copys << endl;
        if (ans == -1) {
            ans = count;
        } else {
            ans = min(ans, count);
        }
    }
}

int main() {
    ifstream cin("A-large.in");
    ofstream cout("A-output.txt");
    cin >> T;
    for (int i=1; i<=T; i++) {
        cin >> S;
        cin >> K;
        ans = -1;
        dfs(S, 0);
        if (ans == -1) {
            cout << "Case #" << i << ": IMPOSSIBLE" << endl;
        } else {
            cout << "Case #" << i << ": " << ans << endl;
        }
    }
    return 0;
}