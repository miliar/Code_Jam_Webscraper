#include<bits/stdc++.h>
using namespace std;

int t;

bool good(long long x){
    int t = 10;
    while(x > 0){
        if(t < x % 10)
            return false;
        t = min(t, (int)(x % 10));
        x /= 10;
    }
    return true;
}

long long toLong(string s){
    long long ans = 0;
    for(int i = 0;i < s.length();i++)
        ans = ans * 10 + s[i] - '0';
    return ans;
}

long long solve(string s){
    string ans = "";
    while(s.length() < 19)
        s = "0" + s;
    bool onpref = true;
    ans = s;
    for(int i = 0;i < s.length();i++){
        if(onpref){
            char mn = '9';
            for(int j = i;j < s.length();j++){
                mn = min(mn, s[j]);
            }
            ans[i] = mn;
            if(ans[i] != s[i]){
                onpref = false;
            }
        }else{
            ans[i] = '9';
        }
    }
    return toLong(ans);
}

int solve(int x){
    while(!good(x))
        x--;
    return x;
}

int main(int argc, char **argv) {
    cin >> t;
    for(int i = 0;i < t;i++){
        int f;
        cin >> f;
        cout << "Case #" << i + 1 << ": ";
        cout << solve(f);
        cout << endl;
    }
}