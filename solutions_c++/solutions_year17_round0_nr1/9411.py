#include <iostream>
#include<string>
#include<vector>

using namespace std;

int main(){
    int test;
    cin >> test;

    for (int t=1; t<=test; t++) {
        string str;
        int k;
        bool success;
        int cnt;
        cin >> str >> k;

        vector<bool> ps;   // is the i. pancake happy side up

        for (int i=0; i<str.size(); i++) {
            ps.push_back(str[i] == '+');
        }

        cnt = 0;
        success = true;
        for (int i=0; i<=ps.size()-k; i++) {
            if (!ps[i]) {   // the pancake isn't the happy side up
                cnt++;
                for (int j=i; j<i+k; j++) {    // flip pancakes  [i, i+k)
                    bool w = true;
                    w ^= ps[j];
                    ps[j] = w;
                }
            }
        }
        for (int i=ps.size()-k+1; i<ps.size(); i++) {
            success &= ps[i];
        }

        if (success) {
            cout << "Case #" << t << ": " << cnt << endl;
        } else {
            cout << "Case #" << t << ": " << "IMPOSSIBLE" << endl;
        }
    }

    return 0;
}
