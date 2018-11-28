#include <bits/stdc++.h>

using namespace std;

string flip(string s, long long i, long long k){
    if(i + k > s.size()) return "IMPOSSIBLE";
    for(int j = i; j < k + i; j++){
        if(s[j] == '+') s[j] = '-'; else s[j] = '+';
    }
    return s;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    long long t, k;
    string s;
    cin >> t;
    for(int z = 0; z < t; z++){
        cin >> s >> k;
        long long ans = 0;
        for(int i = 0; i < s.size(); i++){
            //cout << i << " " << s << endl;
            if(s[i] == '-') s = flip(s, i, k), ans++;
        }
        cout << "Case #" << z + 1 << ": ";
        if(s == "IMPOSSIBLE") cout << s << endl;
        else cout << ans << endl;
    }
    return 0;
}
