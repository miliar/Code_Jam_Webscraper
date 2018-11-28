#include <bits/stdc++.h>
using namespace std;

string solve(string inp) {
    for (int i=inp.size()-2;i>=0;--i) {
        if (inp[i] > inp[i+1]) {
            inp[i]--;
            for (int j=i+1;j<inp.size();++j) inp[j]='9';
        }
    }
    if (inp[0]=='0') {
        inp.erase(inp.begin());
    }
    return inp;
}

int main() {
    int ntest;
    scanf("%d",&ntest);
    for (int test=1;test<=ntest;++test){
        string tmp;
        cin >> tmp;
        cout << "Case #" << test << ": " << solve(tmp) << endl;
    }
    return 0;
}
