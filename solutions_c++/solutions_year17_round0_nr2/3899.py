#include <bits/stdc++.h>
using namespace std;
typedef long long int LL;

int main(){

      freopen("B-large.in","r",stdin);
      freopen("o2small.txt","w",stdout);


    int t;
    scanf("%d",&t);


    for(int g=1;g<=t;g++){

            string s;
            cin>>s;
            int len = s.length();
            for(int i=len-1;i>=0;i--){
                if(s[i-1]>s[i]){
                    s[i-1]=s[i-1]-1;
                    for(int j=i;j<len;j++){
                        s[j]='9';
                    }
                }
            }
            int flg=0;
            cout<<"Case #"<<g<<": ";
            for(int i=0;i<len;i++){
                if(s[i]!='0'){
                    cout<<s[i];
                    flg=1;
                }else if(s[i]=='0' && flg==1){
                    cout<<s[i];
                }
            }
            cout<<endl;
        }

    return 0;
}
