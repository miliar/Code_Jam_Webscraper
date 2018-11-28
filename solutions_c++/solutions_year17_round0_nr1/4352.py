#include<bits/stdc++.h>
using namespace std;




int main(){
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T,K;
    string s;

    cin >> T;


    for(int k = 0; k < T; k++){
        cin >> s >> K;
        int st = 50000,cnt = 0;
        for(int l = 0; l < s.size(); l++){
            if(s[l] == '+')continue;

            if((l+K-1) >= s.size()){
                //cout << k << endl;
                break;
            }

            for(int m = l; m < (l+K); m++){
                if(s[m] == '+'){
                    s[m] = '-';
                    st = min(st,l);
                }
                else if(s[m] == '-')s[m] = '+';
                cnt++;
            }
            //cout << s << endl;
            if(st != 50000)l = st;
            st = 50000;
        }

        int f = 0;

        for(int l = 0; l < s.size(); l++){
            if(s[l] == '-')f = 1;
        }

        cout << "Case #" << k+1 << ": ";

        if(f)cout << "IMPOSSIBLE" << endl;
        else cout << cnt/K << endl;

    }

}
