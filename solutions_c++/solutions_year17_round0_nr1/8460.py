#include <bits/stdc++.h>
using namespace std;

int check_first_minus(string s){
    int i = 0;
    while (s[i] =='+' && i < s.length()){
        i++;
    }
    return i;
}

string flip(string s, int begin, int length){
    for (int i = 0; i < length; i++){
        s[begin+i] = s[begin+i] == '-' ? '+' : '-';
    }
    return s;
}

int count_min_flip(string &s, const &length){
    int ans = 0, flip_begin = check_first_minus(s);
    while (flip_begin <= s.length() - length) {
        s = flip(s, flip_begin, length);
        flip_begin = check_first_minus(s);
        ans++;
    }
    if (flip_begin == s.length()){
        return ans;
    }
    else {
        return -1;
    }
}

int main() {
    int T, k, ans;
    long long N;
    string s;
    scanf("%d", &T);
    for (int i=1;i<=T;i++){
        cin >> s >> k;
        ans = count_min_flip(s, k);
        if (ans >= 0){
            printf("Case #%d: %d\n", i, ans);
        } else{
            printf("Case #%d: IMPOSSIBLE\n", i);
        }
    }
}
