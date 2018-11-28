#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

bool checkIfSorted(string s){
    if (s.size() == 1) return true;
    for (int i = 1; i < s.size(); i++){
        if (s[i-1] > s[i]) return false;
    }
    return true;
}

string recurse(string s){
    string ans = "";
    if (checkIfSorted(s)){
        return s;
    } else {
        for (int i = s.size() - 1; i >= 1; i--){
            for (int j = i-1; j >= 0; j--){
                if (s[i] < s[j]){
                    // The range j to END is unsorted, so sort the range
                    ans = string((s.size() - 1 - j), '9') + ans;
                    if (j != 0 || s[0] != '1') {
                        s[j] = ((s[j] - '0') - 1) + '0';
                        return recurse(s.substr(0, j+1)) + ans;
                    } else {
                        return ans;
                    }
                }
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++){
        string s;
        cin >> s;
        cout << "Case #" + to_string(i) + ": " + recurse(s) << endl;
    }
    return 0;
}
