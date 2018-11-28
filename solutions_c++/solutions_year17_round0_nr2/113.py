#include <bits/stdc++.h>
using namespace std;

int main()
{
    freopen("inB.txt", "r", stdin);
    freopen("outB.txt", "w", stdout);
    int T;cin >> T;
    for(int cas=1;cas<=T;++cas){
        cout << "Case #" << cas << ": ";
        string s;cin >> s;
        for(int i=(int)s.size()-1;i>0;--i) if(s[i]<s[i-1]){
            for(int j=i;j<s.size();++j) s[j]='9';
            --s[i-1];
        }
        if(s[0]=='0') s=s.substr(1, -1);
        cout << s;
        cerr << s << "\n";

        cout << "\n";
    }

    return 0;
}

