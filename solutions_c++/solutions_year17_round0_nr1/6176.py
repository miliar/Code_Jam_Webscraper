#include<bits/stdc++.h>
using namespace std;

#define inst freopen("in.txt", "r", stdin)
#define oust freopen("out.txt", "w", stdout)

int main() {
    inst;oust;
    int t, cs = 1, k;
    string str;
    cin >> t;
    //getchar();
    while(t--) {
        cin >> str >> k;
        //cout<< str << endl;
        int len = str.size();
        int ans = 0;
        for(int i = 0; i < len; i++) {
            if(str[i] == '-') {
                if(len - i < k) {
                    ans = -1;
                    break;
                }
                ans++;
                for(int j = 0; j < k; j++){
                    if(str[i + j] =='-') str[i + j] = '+';
                    else str[i + j] = '-';
                }
            }
            // cout<< i <<" "<< ans << " "<<" "<<str<<endl;
        }
        if(ans == -1) {
            printf("Case #%d: IMPOSSIBLE\n", cs++);
        }
        else {
            printf("Case #%d: %d\n", cs++, ans);
        }
    }
    return 0;
}
