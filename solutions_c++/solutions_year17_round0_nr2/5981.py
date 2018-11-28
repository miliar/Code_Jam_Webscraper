#include <iostream>
#include <map>
#include <cstring>
#include <climits>
#include <fstream>
#include <string>
#include <cmath>
#include <sstream>

using namespace std;

int T;
long long N, ans;

bool judge(long long nn) {
    string number;
    stringstream strstream;
    strstream << nn;
    strstream >> number;
    // cout << number << endl;
    if (number.size() == 1) {
        return true;
    }
    for (int i = 0; i < number.size() - 1; i++) {
        if (number[i] > number[i+1]) {
            return false;
        }
    }
    return true;
}

void solve() {
    long long nn = N;
    while (nn) {
        if (judge(nn)) {
            ans = nn;
            return;
        }
        nn--;
    }
    return;
}

int main() {
    ifstream cin("B-small-attempt0.in");
    ofstream cout("output.txt");
    cin >> T;
    for (int i=1; i<=T; i++) {
        cin >> N;
        ans = -1;
        solve();
        cout << "Case #" << i << ": " << ans << endl;
    }
    return 0;
}