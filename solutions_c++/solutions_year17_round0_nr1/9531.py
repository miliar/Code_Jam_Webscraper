#include<iostream>
#include <cstring>
using namespace std;
int main()
{
    int t;
    cin>>t;
    for(int l=1;l<=t;l++){
        char cake[1001];
        int count=0,flag=1,k;
        int count1=0 ,count2=0;
        cin>>cake;
        cin>>k;
        int len=strlen(cake);
        for(int i=0;i<=len-k ;i++)
         {
            if(cake[i]=='-'){
                count++;
                for(int j=i;j<=i+k-1 ;j++){
                if(cake[j]=='+') cake[j]='-';
                else cake[j]='+';
                }
            }

        }

        for(int i=len-k+1;i<=len-1 ;i++){
          if(cake[i] == '-'){
            flag = 0;
            break;
          }
       }
        if(flag)
            cout<<"Case #"<<l<<":"<<" "<<count<<endl;
        else
            cout<<"Case #"<<l<<":"<<" "<<"IMPOSSIBLE"<<endl;
    }
return 0;
}
