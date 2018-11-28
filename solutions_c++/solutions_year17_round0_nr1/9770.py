#include <iostream>
using namespace std;

int main() {
    int n, k, counti = 0;
    bool printed = false;
    cin >> n;
    string str;
    for(int t = 1; t<=n; t++) {
        counti = 0;
        cin >> str >> k;
        for(int i=0; i<str.length(); i++)
            if(str[i] == '-')
                counti++;
        if(counti == 0)
            cout << "Case #" << t << ": " << 0 << endl;
        else {
            printed = false;
            counti = 0;
            for ( int i=0; i<= str.length()-k; i++){
                if(str[i] == '-'){
                    counti++;
                    for(int u = 0; u<k; u++)
                        str[i + u] = (str[i + u] == '+') ? '-' : '+';
                }
            }
            for(int j=0; j<str.length(); j++)
                if(str[j] == '-'){
                    cout << "Case #" << t << ": " << "IMPOSSIBLE" << endl;
                    printed = true;
                    break;
                }
            if(!printed)
                cout << "Case #" << t << ": " << counti << endl;
        }
    }
    return 0;
}