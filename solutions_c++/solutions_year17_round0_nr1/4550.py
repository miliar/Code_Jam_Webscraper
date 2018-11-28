#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int main(){
    int t,x,k,i,n,j;
    string s;
    cin>>t;
    for(x=1;x<=t;x++){
        cin>>s>>k;
        n=s.length();
        cout<<"Case #"<<x<<": ";
        int st=0,ans=0;
        while(true){
            for(i=st;i<n;i++){
                if(s[i]=='-')break;
            }
            if(i==n)break;
            st=i,ans++;
            for(j=0;j<k;j++){
                if(i+j>=n)break;
                if(s[i+j]=='+'){
                    s[i+j]='-';
                }else{
                    s[i+j]='+';
                }
            }
            if(j!=k)break;
        }
        if(i==n){
            cout<<ans<<endl;
        }else{
            cout<<"IMPOSSIBLE\n";
        }
    }
    return 0;
}
