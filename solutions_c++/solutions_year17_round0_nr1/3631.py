#include <bits/stdc++.h>
using namespace std;

int t, s, k;
bool arr[1005]; // 0 -> happy, 1 -> sad
string a;

int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> t;

    for(int caseno = 1; caseno <= t; caseno ++) {
        cin >> a >> k;
        int c = 0;
        int flip = 0;
        for (char ch : a) {
            arr[c] = ch == '-';
            c++;
        }

        int l = a.length();

        for(int i=0; i+k <= l; i++) {
            if(arr[i] == 0) continue;
            for(int j=0; j<k; j++) {
                arr[i + j] = !arr[i + j];
            }
            flip ++;
        }

        bool flag = false;

        for(int i=0; i<l; i++) {
            // cout << arr[i] << ' ';
            if(arr[i]) flag = true;
        }

        cout << "Case #" << caseno << ": ";
        if(flag) cout << "IMPOSSIBLE";
        else cout << flip;
        cout << '\n';
    }

}
