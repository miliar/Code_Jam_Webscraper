#include <bits/stdc++.h>

using namespace std;


int main()
{
//
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    for(int tc=1;tc<=t;tc++){
        string s;
        cin>>s;
        bool check=0;
        for(int i=1;i<s.length();i++){
            if(check){
                s[i]='9';
                continue;
            }
            if(s[i]<s[i-1]){
                s[i]='9';
                for(int j=i-1;j>=0;j--){
                    if(j==0){
                        s[j]--;
                        break;
                    }
                    if(s[j]==s[j-1]){
                        s[j]='9';
                    }else{
                        s[j]--;
                        break;
                    }
                }
                check=1;
            }
        }
        printf("Case #%d: ",tc);
        for(int i=0;i<s.length();i++){
            if(i==0 && s[i]=='0') continue;
            printf("%c",s[i]);
        }
        printf("\n");
    }



}
