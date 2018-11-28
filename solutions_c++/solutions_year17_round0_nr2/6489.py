#include<iostream>
using namespace std;

// void print(string value, int t) {
//
// }

int main()
{
    ios::sync_with_stdio(false);
    int T;
    cin >> T;
    for(int t=0; t<T; t++) {
        string s;
        cin >> s;
        int i=1;
        for(; i<(int)s.size(); i++)
            if( s[i] < s[i-1] )
                break;
        if( i != (int)s.size() ) {
            i--;
            for(int j=i+1; j<(int)s.size(); j++)
                s[j] = '9';
            for(int j=i; j>=0; j--) {
                s[j]--;
                if( j == 0 || s[j] >= s[j-1] )
                    break;
                s[j] = '9';
            }
        }
        for(i=0; i<(int)s.size(); i++)
            if( s[i] != '0' )
                break;
        cout << "Case #" << t+1 << ": " << s.substr(i) << endl;
    }
    return 0;
}
