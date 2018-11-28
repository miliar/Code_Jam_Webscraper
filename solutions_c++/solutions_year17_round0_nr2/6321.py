#include <iostream>
#include <string>

#define N 1000

#define ll unsigned long long 


using namespace std;

int main() {

    int t;
    cin >> t;

    int n;
    for (int l = 0; l < t; l++) {
        cin >> n;
        
        string s;
        int m;
        for (int i = n; i >= 0; i--) {
            s = to_string(i);            
            char c = s.at(0);
            int current = c - '0';            
            bool found = true;
            m = i;
            for (int j = 1; j < s.length(); j++) {                                
                int c1 = s.at(j);                
                if (current > c1 - '0') {
                    found = false;
                    break;
                }
                current = c1 - '0';
            }
            if (found) break;
        }

        cout << "Case #" << (l+1) << ": " << m << endl;

    }

    return 0;
}