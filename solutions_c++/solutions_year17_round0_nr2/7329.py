#include<bits/stdc++.h>
using namespace std;

main(){
freopen("in.txt","r",stdin);
freopen("out.txt","w",stdout);
    long long int t,n,j;
    string s;
    bool flg;
    scanf("%d",&t);
    for(int i=1;i<=t;i++){
        cin>>n;
        stringstream ss;
        ss<<n;
        string str = ss.str();

        for(int k=str.length()-1;k>0;k--){
            if(str[k]<str[k-1]){
                str[k]='9';
                str[k-1]=str[k-1]-1;
            }

        }
        printf("Case #%d: ",i);
        if(str[0]=='0')j=1;
        else j=0;
        for(int k=j;k<str.length()-1;k++){
            if(str[k]>str[k+1]){
                str[k+1]='9';
            }
        }
        for(int k=j;k<str.length();k++){
            printf("%c",str[k]);
        }
        printf("\n");
    }

return 0;}
