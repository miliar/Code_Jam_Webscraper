/*---+-++-
12333321
++++-++-
01233321
++++---+
01233210

-+-+-
12221
+-++-
01110
*/

#include<bits/stdc++.h>

using namespace std;

int main() {
    int t;
    cin >> t;
    int cas = 1;
    while(t--) {
        string s;
        int k;
        cin >> s >> k;
        
        int a[s.size()];
        int len = s.size();
/*        for(int i = 0; i < len; i++) {
            int start = max(0,i-k+1);
            int end = min(len,i+k);
            a[i] = end-start+1-k;
            cout << a[i];
        }
        cout << "\n";
*/
        int left = 0;
        int right = len-1;
        while(s[left] == '+') left++;
        while(s[right] == '+') right--;

        int flips = 0;
        while(left < right) {
            flips++;
            if(flips % 2) {
                if(left+k > len) break;
                for(int i = left; i < min(len,left+k); i++) {
                    s[i] = s[i] == '+' ? '-' : '+';
                }
//                left++;
            } else {
                if(right-k < -1) break;
                for(int i = right; i > max(0,right-k); i--) {
                    s[i] = s[i] == '+' ? '-' : '+';
                }
//                right--;
            }
            while(s[left] == '+') left++;
            while(s[right] == '+') right--;
//            cout << s << " " << left << " " << right << "\n";
        }
        int done = 1;
        for(int i = 0; i < len; i++) if(s[i] == '-') { done = 0; break; }
        if(done) {
            cout << "Case #" << cas++ << ": " << flips << "\n";
        } else {
            cout << "Case #" << cas++ << ": IMPOSSIBLE\n";
        }
    }
    return 0;
}
