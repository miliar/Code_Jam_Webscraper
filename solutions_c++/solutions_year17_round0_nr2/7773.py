#include<bits/stdc++.h>
using namespace std;
int main(){
    freopen("B-large.in", "r", stdin);
    freopen("output2.txt", "w", stdout);
    int tst,c=1;
    scanf("%d",&tst);
    string s;
    while(tst--){
        cin>>s;
        int i,j,l,f;
        l=s.length();
        printf("Case #%d: ",c);
        c++;
        if(l==1)
            cout<<s<<endl;
        else{
          f=0;
          for(i=0;i<l-1;i++){
            if(s[i]>s[i+1]){
                f=1;break;
            }
          }
        if(f==1){
            while(i>=1){
            if(s[i]>s[i-1])
                break;
            i--;
            }
            s[i]--;
            i++;
            for(;i<l;i++)
                s[i]='0'+9;
        }
         i=0;
        if(s[0]=='0'){
        s=s.substr(1,l-1);
        }
         cout<<s<<endl;
     }
    }
    return 0;
}
