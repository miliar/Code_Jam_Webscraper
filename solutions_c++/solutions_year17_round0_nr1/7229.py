#include <bits/stdc++.h>

using namespace std;

int main(){
    int t, k;
    string s;
    cin >> t;

    for(int x=1;x<=t;x++){
        int counter = 0;
        cin >> s >> k;
    
        int cm = 0;
        for(auto c : s) cm += (c == '-');

        for(int i=0;i<=(s.size() - k);i++){
            if(s[i] == '-'){
                for(int j=0;j<k;j++){
                    s[i+j] = s[i+j] == '+' ? '-' : '+';
                    cm = cm + (s[i+j] == '+' ? -1 : 1);
                }
                counter++;
            }
            if(!cm) break;
        }

        printf("Case #%d: ", x);
        if(cm) printf("IMPOSSIBLE\n");
        else printf("%d\n", counter);
    }

    return 0;
}
