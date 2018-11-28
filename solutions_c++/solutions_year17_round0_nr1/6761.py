#include<iostream>
#include<vector>
#include<cstring>
#include<cstdio>
#include<algorithm>
using namespace std;
int main(){
    int t,i,j,z=1,k,f,count,l;
    cin>>t;
    while(z<=t){
        f=1;count=0;
        char s[1005];
        scanf("%s",s);
        cin>>k;
        l=strlen(s);
        for(i=0;i<l;i++){
            if(s[i]=='-'){
                if(i+k-1>=l){
                    f=0;
                    break;
                }
            else{
                for(j=i;j<=i+k-1;j++){
                    if(s[j]=='+')
                    s[j]='-';
                    else
                    s[j]='+';
                }
                count++;
            }
            }
        }
        printf("Case #%d: ",z);
        if(f==0)
        cout<<"IMPOSSIBLE\n";
        else
        cout<<count<<endl;
        z++;
    }
    return 0;
}