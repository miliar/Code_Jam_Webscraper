#include<bits/stdc++.h>
using namespace std;



int main(){
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    string s;

    cin >> T;

    for(int k =0; k < T; k++){
        cin >> s;

        for(int l = s.size()-1; l >= 1; l--){
            int ff = s[l] - '0';
            int ss = s[l-1] - '0';

            if(ff < ss){
                ss--;
                for(int m = l; m < s.size(); m++){
                    s[m] = '9';
                }
                s[l-1] = (ss+'0');
            }

        }

        int pp = 0;

        string res = "";

        for(int l = 0; l < s.size(); l++){
            if(s[l] != '0'){
                pp = l;
                break;
            }
        }

        for(int m = pp; m < s.size(); m++){
            res+=s[m];
        }

        cout << "Case #" << k+1 << ": " << res << endl;

    }

}
