#include<iostream>
#include<cstdlib>
#include<algorithm>
using namespace std;

int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t;
    cin >> t;
    for(int c=1;c<=t;c++){
        string s;
        cin >> s;
        int flag;
        for(int i=0;i<s.length()-1;i++){
            if(s[i]<=s[i+1])
                continue;
            else{
                s[i]--;
                for(int j=i+1;j<s.length();j++){
                    s[j]='9';
                }
                for(int j=i-1;j>=0;j--){
                    if(s[j]<=s[j+1]){
                        flag=1;
                        break;
                    }
                    else{
                        s[j]--;
                        s[j+1]='9';
                    }
                }
            }
            if(flag==1)
                break;
        }
        int f=1;
        cout << "Case #" << c << ": ";
        for(int i=0;i<s.length();i++){
            if(s[i]=='0' && f==1){
                continue;
            }
            else{
                cout << s[i];
                f=0;
            }
        }
        cout << endl;
    }
}
