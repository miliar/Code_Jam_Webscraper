#include <iostream>
#include <cmath>
#include <cstdio>
using namespace std;
int main(){
    int num;
    cin>>num;
    for(int n=0;n<num;n++)
    {
        string s;
        int a;
        cin>>s>>a;
        int i,j,m=0;
        int len=s.size();
        for(i=0;i<=(len-a);i++)
            {if(s[i]=='-')
                {
                for(j=i;j<(i+a);j++)
                    {
                    	s[j]= (s[j]=='-') ? s[j]='+':s[j]='-';
                   }m++;}}
        int flag=0;
        for(i=0;i<len;i++)
            {if(s[i]!='+')
            {
                flag=1;
            break;}
        }
        if(flag==0){
            cout<< "Case #"<<(n+1);
            cout<< ": "<<m<<endl;
        }
        else{
            cout<<"Case #"<<(n+1);
            cout<<": "<<"IMPOSSIBLE"<<endl;
    }}
    return 0;
}