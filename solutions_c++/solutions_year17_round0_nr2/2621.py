#include <iostream>
#include <string>

using namespace std;

int main() {
    int T;

    ios_base::sync_with_stdio(false);
    cin>>T;

    for (int testCase=1; testCase<=T; ++testCase) {
        string s; cin>>s;

        for (int i=s.size()-2; i>=0; --i) {
            if (s[i]<=s[i+1]) continue;

            s[i] = s[i]-1;
            for (int j=i+1; j<s.size(); ++j) s[j]='9';
        }

        while (s[0]=='0' && s.size()!=1)
            s.erase(s.begin());
        cout<<"Case #"<<testCase<<": "<<s<<endl;
    }

    return 0;
}
