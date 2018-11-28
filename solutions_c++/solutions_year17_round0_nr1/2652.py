#include <iostream>
#include <string>

using namespace std;

//O(n^2)

int main() {
    int T;

    ios_base::sync_with_stdio(false);
    cin>>T;

    for (int testCase=1; testCase<=T; ++testCase) {
        string s; cin>>s;
        int len; cin>>len;
        int ans=0;

        for (int i=0; i<s.size(); ++i) {
            if (s[i]=='+') continue;
            if (i+len>s.size()) {ans=-1; break;}

            ++ans;
            for (int j=i; j<i+len; ++j) s[j]=(s[j]=='+')?'-':'+';
        }

        if (ans!=-1) cout<<"Case #"<<testCase<<": "<<ans<<endl;
        else cout<<"Case #"<<testCase<<": IMPOSSIBLE\n";
    }

    return 0;
}
