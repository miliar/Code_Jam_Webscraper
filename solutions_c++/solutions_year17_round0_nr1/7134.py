#include<iostream>
#include<string>
using namespace std;

int main(){
    int ch,caseno;
    int slen,k;
    string s;
    cin >> ch ;
    int flag,cnt;
    for (caseno = 1; caseno < ch+1 ; caseno++){
        cin >> s >> k;
        cnt=0;flag=1;
        slen = s.length();
        for(int i=0; i<= slen-k ; i++){
            if(s[i] == '-'){
                for(int j=0;j<k;j++){
                    s[i+j] = (s[i+j] == '-') ? '+' : '-';
                }
            cnt++;
            //cout << s << endl;
            }
        }

        for(int m=slen-k+1;m<slen;m++){
            if(s[m]=='-'){
                flag = 0;
            }
        }
        if(flag == 1){
            cout << "Case #" << caseno << ": "<< cnt << endl;
        }
        if (flag ==0){
            cout << "Case #" << caseno << ": "<< "IMPOSSIBLE" << endl;

        }

    }
    return 0;
}
