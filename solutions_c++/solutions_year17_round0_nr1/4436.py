#include <iostream>
#include <vector>
#include "unordered_map"
#include <cmath>
#include <climits>
#include "queue"
#include "tuple"
#include <algorithm>

using ll=long long;
using ull=unsigned long long;
using namespace std;

int main() {
    freopen("../input.txt","r",stdin);
    freopen("../output.txt","w",stdout);
    int n;
    cin >> n;
    for(int i = 1; i <= n; ++i) {
        string s;
        cin >> s;
        int fl;
        cin >> fl;
        int count = 0;
        int sCount = s.size();
        string result;
        for(int j = 0; j <= sCount - fl; ++j) {
            char cs = s[j];
            if(cs == '-') {
                for(int k = 0; k < fl; ++k) {
                    s[j + k] = s[j + k] == '-' ? '+' : '-';
                }
                ++count;
            }
        }
        result = to_string(count);
        for(int j = sCount - fl + 1; j < sCount; ++j) {
            if(s[j] == '-') {
                result = "IMPOSSIBLE";
                break;
            }
        }
        cout << "Case #" << i << ": " << result << endl;
    }
}
