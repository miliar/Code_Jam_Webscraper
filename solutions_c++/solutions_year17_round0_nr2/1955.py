#include<iostream>
#include<string>
using namespace std;
int main()
{
    int t;
    cin >> t;
    for (int cs = 1; cs <= t; cs++) {
        string s;
        cin >> s;
        int l = s.length();
        for (int i = l - 1; i >= 1; i--) {
            bool tt = (s[i] < s[i - 1]);
            if (tt) {
                s[i - 1]--;
                for (int j = i; j < l; j++) {
                    s[j] = '9';
                }
            }
        }

        if (s[0] == '0') {
            s = s.substr(1, l - 1);
        }
        cout << "Case #" << cs << ": " << s << endl;
    }

    return 0;
}
