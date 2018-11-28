#include <iostream>
#include <string>
#include <queue>
#include <list>
#include <tuple>

using namespace std;

int main()
{
    int t;
    cin >> t;
    
    for (int i=1; i<=t; ++i) {
        bool impossible = false;
        string s;
        int k, w=0;
        
        cin >> s >> k;
        
        vector<bool> a(s.size());
        for (int j=0; j<s.size(); j++) {
            if (s[j] == '+') {
                a[j] = true;
            }
        }
        
        for (int j=0; j<=a.size()-k; j++) {
            if (!a[j]) {
                w++;
                for (int l=j; l<j+k; l++) {
                    a[l] = !a[l];
                }
            }
        }
        
        cout << "Case #" << i << ": ";
        
        for (int j=a.size()-k; j<a.size(); j++) {
            if (!a[j]) {
                cout << "IMPOSSIBLE" << endl;
                impossible = true;
                break;
            }
        }
        
        if (!impossible) {
            cout << w << endl;
        }
    }

    return 0;
}
