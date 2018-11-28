
#include <iostream>
using namespace std;

int main() {
    freopen("A-large.in", "r", stdin);
    	freopen("ans.txt", "w", stdout);
    
    int t;
    cin >> t;
    string s;
    int k;
    for (int it = 1; it <= t; ++it) {
        cout<<"Case #"<<it<<": ";
        cin>>s>>k;
        int n = s.length();
        //cout << s << ", " << k << endl;
        int cnt = 0;
        for(int i = 0; i < n ; i++){
            if (cnt == -1) break;
            if (s[i] == '-'){
                cnt++;
                for(int j = i; j <i+k; j++){
                    if (j >= n)
                        cnt = -1;
                        
                    
                    if (s[j] == '+') s[j] = '-';
                    else s[j] = '+';
                }
            }
        }
        if (cnt == -1) cout << "IMPOSSIBLE\n";
        else cout << cnt << "\n";
    }

    return 0;
}
