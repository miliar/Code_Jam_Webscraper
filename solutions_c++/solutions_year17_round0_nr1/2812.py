#include<bits/stdc++.h>
using namespace std;
int main(){
int t;
scanf("%d",&t);
int x=t;
while(t--){
    int i,j,k,s=1,flip=0;
    string str;
    cin>>str;
    cin>>k;
    int l=str.length();
    for(i=0;i<l;i++){
        if(str[i]=='-'){
            for(j=0;j<k&&i+j<l;j++){
                if(str[i+j]=='+')
                    str[i+j]='-';
                else
                    str[i+j]='+';
            }
           if(j!=k){
            printf("Case #%d: IMPOSSIBLE\n",x-t);
            s=0;
            break;
           }
           else
            flip=flip+1;
        }
    }
    if(s==1)
        printf("Case #%d: %d\n",x-t,flip);
}
return 0;
}
