#include<bits/stdc++.h>
#include<string>
using namespace std;

int main(){
freopen("input.in","r",stdin);
freopen("output.out","w",stdout);
int t;
cin >>t;
for(int x=1;x<=t;x++){

   string str;
   cin >> str;
   int j;
   int flag=0,tmp=0;
   char c;
   for(j=0;j<str.size()-1;j++){
        if(flag){
            str[j]='9';
        }
      else if(str[j+1]<str[j]){
            tmp=j;
            c=str[j];
          str[j]=str[j]-1;
          flag=1;
          tmp=j;
      }
   }

   if(tmp!=0 && (str[tmp-1]==str[tmp-1]))
     str[tmp]='9';
   for(j=tmp-1;j>=0;j--){
         if(str[j]==c){
            str[j]=(j!=0 ?'9':str[j]-1);
         }
         else{
            str[j+1]=(c-1);
            break;
         }

   }
   if(flag)
      str[str.size()-1]='9';

   for(int i=0;i<str.size();i++){
      if(str[i]=='0')
        str=str.substr(1,str.size()-1);
   }
   cout<<"Case #"<<x<<": "<<str<<endl;
}
}
