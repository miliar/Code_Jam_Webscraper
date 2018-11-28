#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

bool isFlipped(string s){
    return (s == string(s.size(), '+'));
}

// Flip all chars from x to x+k
string flip(string s, int x, int k){
    string flipped = "";
    for (int i = x; i < x+k; i++){
        flipped = flipped + (s[i] == '+' ? '-' : '+');
    }
    return s.substr(0, x) + flipped + s.substr(x+k, (s.size() - (x+k)));
}

string ans(string s, int k){
    string cpy = s;
    int num_happy = 0;
    for (int i = 0; i < s.size(); i++){
        if (s[i] == '+') num_happy++;
    }
    int num_sad = s.size() - num_happy;
    if (num_happy == s.size()) return "0";
    else {
        int cnt = 0;
        for (int i = 0; i < s.size() - k + 1; i++){
            if (s[i] == '-'){
                s = flip(s, i, k);
                cnt++;
            }
            if (isFlipped(s)) return to_string(cnt);
        }
        return "IMPOSSIBLE";
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    int t, k;
    string s;
    cin >> t;
    for (int i = 1; i <= t; i++){
        cin >> s >> k;
        cout << "Case #" + to_string(i) + ": " + ans(s, k) << endl;
    }
    return 0;
}
