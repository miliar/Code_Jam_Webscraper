#include <bits/stdc++.h>

using namespace std;

int main(){
  int t,i,p;
  cin>>t;
  for(int k=1;k<=t;k++){
   string s;
   cin>>s;
 p=0;
 int c=0;
   for( i=1;i<s.size();i++){
     if(s[i]<s[i-1]){
        s[i-1];
        p=i-1;
        break;
        }
        }
        if(i==s.size()){
            cout<<"Case #"<<k<<":"<<" ";
            for(int i=0;i<s.size();i++)
             cout<<s[i];
             cout<<endl;
             continue;
        }

for(i=p-1;i>=0;i--){
    if(s[i]==s[i+1])
        s[i+1]='9';
        else
            break;

}i++;

s[i]--;

   for(i=p+1;i<s.size();i++)
       s[i]='9';

cout<<"Case #"<<k<<":"<<" ";

   if(s[0]!='0')
       cout<<s[0];
   for(int i=1;i<s.size();i++)
         cout<<s[i];
         cout<<endl;


  }
    return 0;
}
