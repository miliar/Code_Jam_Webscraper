#include<bits/stdc++.h>
using namespace std;

int bt(int x){
    int ans = 0;
    while(x > 0)
        ans += x & 1, x >>= 1;
    return ans;
}

int main(int argc, char **argv) {
    int t;
    cin >> t;
    for(int i = 0;i < t;i++){
        string s;
        int k;
        cin >> s >> k;
        int ans = 1000;
        for(int m = 0;m < (1 << (s.length() - k + 1));m++){
            string nw = s;
            for(int j = 0;j < s.length() - k + 1;j++){
                if((m & (1 << j)) != 0){
                    for(int f = 0;f < k;f++){
                        nw[j + f] = (nw[j + f] == '+' ? '-' : '+');
                    }
                }
            }
            //cout << nw << endl;
            bool ok = true;
            for(int j = 0;j < nw.length();j++)
                if(nw[j] == '-')
                    ok = false;
            if(ok)
                ans = min(ans, bt(m));
        }
        if(ans != 1000)
            cout << "Case #" << i + 1 << ": " << ans << endl;
        else
            cout << "Case #" << i + 1 << ": " << "IMPOSSIBLE" << endl;
    }
}