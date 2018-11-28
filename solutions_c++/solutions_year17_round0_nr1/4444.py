#include<iostream>
using namespace std;


int eval(string s, int k) {
    int res = 0;
    bool is_good = true;
    for(int i=0;i<s.size();i++) {
        if(s[i] == '+') continue;
        int j = i;
        for(int t=0;j<s.size()&&t<k;j++,t++) 
            s[j] = s[j] == '-' ? '+' : '-';
        if(j-i != k) { is_good = false; break; }
        res ++;
    }
    if(is_good) return res;
    return -1;
}

int main(int argc, char const* argv[]) {
    int t;
    cin >> t;
    for(int i=1;i<=t;i++) {
        string s;
        int k;
        cin >> s >> k;
        int res = eval(s,k);
        cout << "Case #" << i << ": ";
        if(res == -1) cout << "IMPOSSIBLE";
        else cout << res;
        cout << endl;
    }
    return 0;
}
