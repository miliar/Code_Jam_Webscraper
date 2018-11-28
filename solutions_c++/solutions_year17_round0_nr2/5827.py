#include <stdio.h>
#include <iostream>
#include <string>
using namespace std;
string solve(string num) {
    bool finished = false;
    string ans = "";
    bool keep = true;
    for (int i = 0; i<num.length()-1; i++) {
        char ch = num.at(i);
        if (keep && ch <= num.at(i+1)) {
            ans+=ch;
        } else if (keep) {
            keep = false;
            if (ans.length() != 0 || ch > '1') {
                ans += (ch-1);
                return solve(ans) + string(num.length()-i-1,'9');
            }
        } else {
            ans+='9';
        }
    }
    ans+= (keep ? (num.at(num.length()-1)) : '9');
    return ans;
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int N;
    cin>>N;
    for (int aa=0;aa<N;aa++) {
        string num;
        cin>>num;
        printf("Case #%d: %s\n", aa+1, solve(num).c_str());
    }
    fclose(stdin);
    fclose(stdout);
}
