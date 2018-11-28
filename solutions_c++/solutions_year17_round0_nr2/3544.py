#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
    int testcase;
    cin >> testcase;
    for(int tc=1;tc<=testcase;++tc) {
        string s;
        vector<int> ans;
        cin >> s;
        bool used = false;
        for(int i=0;i<s.length();++i) {
            int cur = s[i] - '0';
            ans.push_back(cur);
            int j = ans.size() - 1;
            if( ans[j-1] > ans[j] ) {
                if(!used) {
                    used = true;
                    for(;j>0;--j) {
                        if(ans[j-1] > ans[j]) {
                            ans[j-1]--;
                            ans[j] = 9;
                        }
                    }
                } else ans[j] = 9;
            }
        }
        cout << "Case #" << tc << ": ";
        bool sw = false;
        for(const auto& e : ans) { 
            if (e>0) sw = true;
            if (sw) cout << e;
        }
        cout << endl;
    }
    return 0;
}
