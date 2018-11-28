#include <bits/stdc++.h>

using namespace std;

int main()
{
  int test;
  cin>>test;
  int p=test;
  while(test--){
      int x;
      string s;
      cin>>s>>x;
      string pl = "+";
      string mi = "-";
      int ans=0;
      for(int i=0;i<s.length();i++){
          if(s[i]=='-' && i+x-1<s.length()){
              for(int j=i;j<i+x;j++){
                  if(s[j]=='-'){
                     s.replace(j,1,"+");
                  }
                  else{
                     s.replace(j,1,"-");
                  }
              }
              ans++;
          }
      } 
      int temp=0;
      for(int i=0;i<s.length();i++){
         if(s[i]=='-'){
            
             temp++;
             break;
         }
      }
      if(temp!=0){
          cout<<"Case #"<<p-test<<": IMPOSSIBLE"<<endl;
      }
      else{
           cout<<"Case #"<<p-test<<": "<<ans<<endl;
      }
  }
   
   return 0;
}

