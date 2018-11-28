#include <iostream>
#include<string>
#include<cstdio>
#include<algorithm>
using namespace std;
int main()
{
    long long int i,cc,t,j,length,prev,curr,pprev;
    string strin;
    scanf("%d",&t);
    for(cc=1; cc<=t; cc++){
           cin >> strin;
           cout << "Case #"<<cc<<": ";
           length=strin.length();
           if(length==1)
                cout << strin << endl;
           else{
               prev=strin[0]-'0';
               for(i=1;i<length;i++){
                   if(i>1)
                        pprev=strin[i-2]-'0';
                   curr=strin[i]-'0';
                   if(prev>curr){
                        strin[i-1]=prev-1+'0';
                        prev=strin[i-1]-'0';
                        for(j=i;j<length;j++)
                            strin[j]='9';
                        break;
                   }
                   prev=curr;
               }
               if(length>2){
                   if(pprev>prev){
                       for(j=i-1;j>0;j--){
                           strin[j]='9';
                           strin[j-1]=strin[j-1]-1;
                       }
                   }
               }
          
    
               if(strin[0]=='0'){
                    strin=strin.substr(1);
                    cout << strin << endl;
               }
               else
                    cout << strin << endl;
           }
    }
    return 0;
}