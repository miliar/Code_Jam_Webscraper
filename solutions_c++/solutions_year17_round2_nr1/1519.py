#include <bits/stdc++.h>

using namespace std;
 

int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    cout.precision(20);
    for (int o = 1; o <= T; o++){
        cout << "Case #" << o << ": ";
        double n, d;
        cin >> d >> n;
        vector <double> k(n), s(n);
        double m = 0;
        for (int i = 0; i < n; i++){
            cin >> k[i] >> s[i];
            if (m < ((d - k[i])/s[i])){
                m = (d - k[i])/s[i];
            }
        }
        cout << d/m << endl;
    }   
    return 0;
}
