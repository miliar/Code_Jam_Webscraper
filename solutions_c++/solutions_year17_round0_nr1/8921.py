#include <iostream>
#include <cmath>
#include <cstdio>
using namespace std;
int main(){
    int T;
    cin >> T;
    for(int n=0;n<T;n++)
    {
        string s;
        int k;
        cin>>s>>k;
        int i,j,tn=0,size=s.size();
        for(i=0;i<=(size-k);i++)
            {if(s[i]=='-')
                {
                for(j=i;j<(i+k);j++)
                    {
                    	s[j]= (s[j]=='-') ? s[j]='+':s[j]='-';
                   }tn++;}}
        int flag=0;
        for(i=0;i<size;i++)
            {if(s[i]!='+')
            {flag=1;
            break;}}
        if(flag==0){
            cout<< "Case #"<<(n+1);
            cout<< ": "<<tn<<endl;
        }
        else{
            cout<<"Case #"<<(n+1);
            cout<<": "<<"IMPOSSIBLE"<<endl;
    }}
    return 0;
}