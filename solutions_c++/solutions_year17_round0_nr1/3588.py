#include <iostream>

using namespace std;

int main()
{
    int testcase;
    cin >> testcase;
    for(int tc=1;tc<=testcase;tc++) {
        string s;
        int k;
        bool ans = true;
        int ans_c = 0;
        cin >> s >> k;
        for(int i=0;i<=s.length()-k;++i) {
            if (s[i] == '-') {
                ans_c++;
                for(int j=i;j<i+k;++j) {
                    s[j] = (s[j]=='-'?'+':'-');
                }
            }
        }
        for(int i=s.length()-k+1; i<s.length(); ++i) {
            if(s[i] != '+') {
                ans = false;
                break;
            }
        }
        cout << "Case #" << tc << ": ";
        if(ans) cout << ans_c << endl;
        else cout << "IMPOSSIBLE" << endl;
    }
    return 0;
}
