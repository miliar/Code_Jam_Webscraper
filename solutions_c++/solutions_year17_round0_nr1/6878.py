#include <bits/stdc++.h>

using namespace std;

void flip(string &s,int i){
    if(s[i]=='+') s[i]='-';
    else s[i] = '+';
}

int main(){
    int z;
    cin>>z;
    for(int t=1;t<=z;t++){
        int k,count=0;
        string s;
        cin>>s>>k;
        int i=0;
        while(i<s.size()-k+1){
            if(s[i]=='-'){
                for(int j=i;j<i+k;j++) flip(s,j);
                count++;
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
        if(flag) printf("Case #%d: %d\n",t,count);
        else printf("Case #%d: IMPOSSIBLE\n",t);
    }
    return 0;
}
