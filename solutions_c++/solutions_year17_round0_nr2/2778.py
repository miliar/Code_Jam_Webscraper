#include<bits/stdc++.h>
using namespace std;
int tidyno(string str,int l){
int i;
for(i=0;i<l-1;i++){
    if(str[i+1]<str[i])
        break;
}
if(i==l-1)
    return 1;
else
    return 0;
}
int main(){
    int t;
    scanf("%d",&t);
    int x=t;
    while(t--){
        string str;
        int i,j;
        cin>>str;
        int l=str.length();
       while(!tidyno(str,l)){
        for(i=0;i<l-1;i++){
            if(str[i]>str[i+1])
                break;
        }
        str[i]=str[i]-1;
        for(j=i+1;j<l;j++)
            str[j]='9';
       }
       int f=1;
       printf("case #%d: ",x-t);
       for(i=0;i<l;i++){
        if(str[i]=='0'&&f==1)
            continue;
        else{
            f=0;
            cout<<str[i];
        }
       }
       cout<<endl;
    }
    return 0;
}
