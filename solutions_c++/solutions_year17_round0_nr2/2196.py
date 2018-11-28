#include <bits/stdc++.h>

using namespace std;

string get (int n){
    string s;
    for (int i = 0; i < n; i++)
        s += '9';
    return s;
}

string solve (string s){
    vector <string> ans;
    s.insert(s.begin(), '0');
    for (int i = 1; i < s.size(); i++){
        if (s[i] < s[i - 1]) break;
        if (s[i] - 1 >= s[i-1]){
            string aux = s.substr(0, i + 1);
            aux.back()--;
            aux += get(s.size() - i - 1);
            ans.push_back(aux);
        }
        if (i == s.size() - 1) ans.push_back(s);
    }
    sort (ans.begin(), ans.end());
    string ret = ans.back();
    while (ret[0] == '0') ret.erase(ret.begin());

    return ret;
}

int main(){

    int t;
    scanf ("%d", &t);
    for (int cc = 1; cc <= t; cc++){
        string s;
        cin >> s;
        printf ("Case #%d: %s\n", cc, solve(s).c_str());
    }

    return 0;
}
