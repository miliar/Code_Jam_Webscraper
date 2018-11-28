#include<bits/stdc++.h>
using namespace std;
int main(){
    int t,k,cont,ban;
    string s;
    scanf("%d",&t);
    for(int l=1;l<=t;l++){
        cin>>s>>k;
        cont=0;
        for(int i=0;i<=s.size()-k;i++){
            if(s[i]=='-'){
                cont++;
                for(int j=i;j<i+k;j++){
                    if(s[j]=='-')
                        s[j]='+';
                    else
                        s[j]='-';
                }
            }
        }
        for(int i=0;i<s.size();i++){
            if(s[i]=='-'){
                ban=0;
                break;
            }
            else
                ban=1;
        }
        if(ban==0)
            printf("Case #%d: IMPOSSIBLE\n",l);
        else
            printf("Case #%d: %d\n",l,cont);
    }
    return 0;
}

