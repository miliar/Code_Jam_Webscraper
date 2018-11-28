#include <bits/stdc++.h>

using namespace std;

bool check(int s){
    int prev=0,curr=0;
    curr = s%10;
    s = s/10;
    while(s!=0){
        prev = curr;
        curr = s%10;
        s = s/ 10;
        if(prev < curr){
            return false;
        }
        
    }
    return true;
}

int main()
{
  int test;
  cin>>test;
  int p=test;
  while(test--){
      int x;
      cin>>x;
      int ans;
      for(int i=x;i>0;i--){
          if(check(i)){
              ans = i;
              break;
      }
      
  }
  cout<<"Case #"<<p-test<<": "<<ans<<endl;
  }
   return 0;
}

