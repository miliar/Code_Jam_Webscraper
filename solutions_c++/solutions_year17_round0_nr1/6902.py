#include <bits/stdc++.h>

using namespace std;


int main(){
    int t;
    cin>>t;
    for(int p=1;p<=t;p++){
        int k,cnt=0;
        string s;
        cin>>s>>k;
        int i=0;
        while(i<s.size()-k+1){
            if(s[i]=='-'){
                for(int j=i;j<i+k;j++)
                {
                 if(s[j]=='+') s[j]='-';
                    else s[j] = '+';
                }
                cnt++;
            }
            i++;
        }
        bool flag = 1;
        for(int i=s.size()-k;i<s.size();i++){
            if(s[i]=='-'){
                flag=0;
                break;
            }
        }
        if(flag)
            printf("Case #%d: %d\n",p,cnt);
        else
            printf("Case #%d: IMPOSSIBLE\n",p);
    }
    return 0;
}

