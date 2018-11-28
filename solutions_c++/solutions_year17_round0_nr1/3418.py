#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <fstream>
using namespace std;  // since cin and cout are both in namespace std, this saves some text

string str[101];
int N[101];

int main() {
    int T;
    cin >> T;  // read t. cin knows that t is an int, so it reads it as such.
    int count = 0;
    
    for (int t = 1; t <= T; ++t) {
        cin >> str[t] >> N[t];
    }
    
    for (int t = 1; t <= T; ++t) {
        
        for (int i=0;i<=str[t].length()-N[t];i++) {
            if (str[t][i] == '-') {
                for (int j=0;j<N[t];j++) {
                    if (str[t][i+j] == '-') str[t][i+j] = '+';
                    else str[t][i+j] = '-';
                }
                count++;
            }
        }
        bool imp = true;
        //cout << str[t] << endl;
        for (int i=0;i<str[t].length();i++) {
            if (str[t][i] == '-') {
                imp = false;
                break;
            }
        }
        
        if (!imp) {
            cout <<"Case #" << t <<": IMPOSSIBLE" << endl;
        }
        else {
            cout <<"Case #" << t <<": " << count << endl;
        }
        
        count = 0;
    }
    
    return 0;
}
