#include<iostream>

using namespace std;

int main(void)
{
    int T;
    cin >> T;
    for (int i=0; i<T; i++) {
        string s;
        cin >> s;
        for (int i=s.length()-1; i>0; i--) {
            if (s[i-1] <= s[i]) continue;
            s[i-1] = s[i-1]-1;
            for (int j=i; j<s.length(); j++)
                s[j] = '9';
            if (s[i-1] == '0' && i == 1) {
                s = s.substr(1);
                break;
            }
        }
        cout << "Case #" << i+1 << ": " << s << endl;
    }
    return 0;
}
