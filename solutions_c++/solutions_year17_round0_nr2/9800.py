#include <iostream>
#include <cstring>
#include <cstdio>
#include <queue>
using namespace std;

int main(){
    int t;
    //freopen("B-small-attempt1.in","r",stdin);
    cin >> t;
    int tt=t;
    while(t--){
        string s;
        cin >> s;
        //cout << "stirng "<< s<< endl;
        for(int i=s.size()-1;i>0;i--){
            if(s[i]-'0'!=0){
                if(s[i-1]!='0'){
                    if((s[i-1]-'0')-(s[i]-'0')>0){
                        s[i] = '9';
                        for(int j=i+1;j<s.size();j++){
                            s[j]='9';
                        }
                        s[i-1] = '0'+((s[i-1]-'0')-1);
                        //cout << "s " << i-1 << " is " << s[i-1] << endl;
                    }
                }
                else {
                    s[i]='9';
                }
            }
            else {
                s[i] = '9';
                if(s[i-1]!='0')
                    s[i-1] = '0'+((s[i-1]-'0')-1);
            }
        }
        if(s.size()>1&&((s[0]-'0')-(s[1]-'0')>0)){
            s[0] = '0'+((s[0]-'0')-1);
        }

        cout << "Case #"<<tt-t<<": ";
        for(int i=0;i<s.size();i++){
            if(s[i]!='0')
                cout << s[i];
        }
        cout << endl;
    }
    return 0;
}
