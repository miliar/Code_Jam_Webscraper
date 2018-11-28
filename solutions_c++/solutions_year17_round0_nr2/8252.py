#include <bits/stdc++.h>

using namespace std;

int main(){
   ofstream myfile;
   myfile.open ("goo2.txt");
   int t;
   cin>>t;
   string s;
   for(int q=0;q<t;q++){
      string s;
      cin>>s;
      int len=s.length();
      int flag=-1;
      int count=0;
      for(int i=0;i<len-1;i++){
         if(s[i]>s[i+1]){
            flag=i;
            break;
         }
         else if(s[i]==s[i+1]){
            count++;
         }
         else count=0;
      }
      if(flag==-1){
         myfile <<"Case #"<<q+1<<": ";
         for(int i=0;i<len;i++){
            int kw=s[i]-48;
            myfile<<kw;
         }
         myfile<<endl;
      } 
      else{
         myfile <<"Case #"<<q+1<<": ";
         int k=flag-count;
         if(k==0 && s[k]=='1'){
            for(int i=0;i<len-1;i++){
               myfile<<9;
            }
         }
         else{
            for(int i=0;i<k;i++){
               myfile<<s[i]-48;
            }
            s[k]-=49;
            myfile<<(int)s[k];
            for(int i=k+1;i<len;i++){
               myfile<<9;
            }
         }
         myfile<<endl;
      } 
   }
   myfile.close();
}
