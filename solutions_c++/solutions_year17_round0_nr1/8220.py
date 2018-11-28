#include <bits/stdc++.h>

using namespace std;

int main(){
   ofstream myfile;
   myfile.open ("goo1.txt");
   int t;
   cin>>t;
   string s;
   int k;
   for(int q=0;q<t;q++){
      cin>>s>>k;
      int count=0;
      int len=s.length();
      vector<int> a(len+1);
      if(s[0]=='-'){
         a[0]++;
         a[k]--;
         count++;
      } 
      for(int i=1;i<=len-k;i++){
         a[i]+=a[i-1];
         if((a[i]%2==0 && s[i]=='-') || (a[i]%2!=0 && s[i]=='+')){
            a[i]++;
            a[i+k]--;
            count++;
         }
      }
      int flag=0;
      for(int i=len-k+1;i<len;i++){
         a[i]+=a[i-1];
         if((a[i]%2==0 && s[i]=='-') || (a[i]%2!=0 && s[i]=='+')){
            flag=1;
            break;
         }
      }
      if(flag==0) myfile <<"Case #"<<q+1<<": "<<count<<endl;
      else myfile <<"Case #"<<q+1<<": "<<"IMPOSSIBLE"<<endl;
   }
   myfile.close();
}