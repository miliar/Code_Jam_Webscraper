#include <algorithm>
#include <bitset>
#include <ctime>
#include <cstdlib>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>
using namespace std;

int main() {
    int NC;
    cin >> NC;
    for (int nc = 1; nc <= NC; nc++) {
        int ans = 0;
        string str;
        int s;
        cin >> str >> s;
        for (int i = 0; i < str.size() - s + 1; i++) {
            if (str[i] == '-') {
                ans++;
                for (int j = i; j < i + s; j++) {
                    if (str[j] == '-') str[j] = '+';
                    else str[j] = '-';
                }
            }
        }
        for (int i = 0; i < str.size(); i++) {
            if (str[i] == '-') {
                ans = -1;
            }
        }
        cout << "Case #" << nc << ": ";
        if (ans == -1) cout << "IMPOSSIBLE";
        else cout << ans;
        cout << endl;
    }
}
