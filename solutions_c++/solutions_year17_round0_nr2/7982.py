#include <bits/stdc++.h>

using namespace std;


int main() {
    int T;
    cin >> T;
    int t = T;

    while(t--) {
        string num;
        cin >> num;

        for(int i = num.size()-1; i > 0; i--) {
            if(num[i] < num[i-1]) {
                num[i-1]--;
                for(int j = i; j < num.size(); j++) {
                    num[j] = '9';
                }
            }
        }

        cout << "Case #" << T-t << ": "; 
        for(int i = 0; i < num.size(); i++) {
            if(num[i] > '0')
                cout << num[i];
        }
        cout << endl;
    }
}