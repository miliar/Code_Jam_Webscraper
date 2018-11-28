#include<bits/stdc++.h>
using namespace std;

main(){
freopen("in.txt","r",stdin);
freopen("out.txt","w",stdout);
    int t,K;
    string s;
    scanf("%d",&t);
    for(int i=1;i<=t;i++){
        cin>>s>>K;
        int result=0;
        for(int j=0;j<=s.length()-K;j++){
            if(s[j]=='-'){
                for(int k=0;k<K;k++){
                    if(s[j+k]=='-')s[j+k]='+';
                    else s[j+k]='-';
                    //result++;
                    //cout<<j+k<<" "<<s[j+k]<<endl;
                }
                result++;
            }

        }
        bool flg=false;
        for(int j=0;j<s.length();j++)if(s[j]=='-')flg=true;
        if(flg)printf("Case #%d: IMPOSSIBLE\n",i);
        else printf("Case #%d: %d\n",i,result);
    }

return 0;}
