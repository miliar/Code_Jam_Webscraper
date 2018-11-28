#include <bits/stdc++.h>

using namespace std;
bool verif(string s){
for(int i=0;i<s.size();i++){
    if(s[i]=='-') return false;
}
return true;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large-O.txt","w",stdout);
   int t;
   int ca=0;
   int k;
   string s;
   cin>>t;
   while(t--){
        ca++;
        int ans=0;
    cin>>s>>k;
    for(int i=s.size()-1;i>=0;i--){
        if(s[i]=='-'){
         if(i-k+1>=0){
            ans++;
            for(int j=i-k+1;j<=i;j++){
                if(s[j]=='-') s[j]='+';
                else s[j]='-';
            }
         }
        }
    }
    cout<<"Case #"<<ca<<": ";
    if(verif(s)){
   cout<<ans<<endl;
    }
    else cout<<"IMPOSSIBLE"<<endl;

   }
    return 0;
}
