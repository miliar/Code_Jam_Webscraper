#include <bits/stdc++.h>

using namespace std;

int main(){
    int n, k = 1;
    string s;

    cin >> n;

    while(n--){
        // getchar();
        getline(cin >> ws, s);

        // cout << s;
        // cout << s.length()-1 << "\n";

        for(int i = s.length()-1;i>=1;i--){
            if ((int)s[i-1] > (int)s[i]) {
                // cout << s[i-1];
                for(int j=i; j < s.length();j++){
                    s[j] = '9';
                }
                s[i-1] = s[i-1] - 1;
            }
        }
        if(s[0] == '0') s.erase(0,1);

        cout << "Case #" << k << ": " << s << endl;
        k++;
        s.clear();
    }


    return 0;
}
