#include <iostream>

using namespace std;

int main() {
	int T;

	cin >> T;

	for(int i = 1; i <=T; i++) {
        string s;
        int k;
        cin >> s >> k;

        int len;
        len = s.length();

        int bit[len], t[len], total = 0, ans = 0;
        bool isImpossible = false;

        for(int j = 0; j < len; j++) {
            t[j] = 0;
            if(s[j] == '+') bit[j] = 1;
            else bit[j] = 0;
        }

        for(int j = 0; j < len; j++) {
            t[j] = (bit[j] + total)%2 != 1;
            total += t[j] - (j >= k-1? t[j-k+1]:0);
            ans += t[j];
            if(j > len-k and t[j] != 0) {
                isImpossible = true;
            }
        }

        if(isImpossible) {
            cout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
            continue;
        }

        cout << "Case #" << i << ": " << ans << endl;

    }

}
