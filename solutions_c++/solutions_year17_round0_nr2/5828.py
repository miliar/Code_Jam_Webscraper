#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int tc, count = 1;
    cin>>tc;
    while (tc--) {
        string s;
        cin>>s;
        string realans = "";
        string ans;
        for (int q=0;q<20;q++) {
            ans=s;
            for (int i=0;i<s.length()-1;i++) {
                if (ans[i] <= ans[i+1]) continue;
                else {
                    ans[i]--;
                    for (int j=i+1;j<ans.length();j++)
                        ans[j] = '9';
                    break;
                }
            }
            if (ans == s) break;
            s = ans;
        }

        for (int i=0;i<ans.length();i++) {
            if (ans[i] == '0') continue;
            else realans+=ans[i];
        }
        cout<<"Case #"<<count++<<": "<<realans<<endl;

    }
    return 0;
}