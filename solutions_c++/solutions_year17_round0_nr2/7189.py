#include <bits/stdc++.h>
using namespace std;


string getStringNine(int k){
    string temp="";
    for(int i=0;i<k;i++) temp+="9";
    return temp;
}
int main()
{
    int Test;
    cin>>Test;
    while(Test--){
    string str;
    cin>>str;
    int N=str.size();
    
    string temp="";
    string nine="9";
    
            int d=(int)str[N-1];
            int e=(int)str[N-2];
            int i;
            if(d < e){
            temp=(char)(e-1)+nine+temp;
                i=N-3;
            }
            else{
                temp+=str[N-1];
                i=N-2;
            }
        
        while(i>=0){
             e=(int)str[i];
             d=(int)temp[0];
             
            if(d < e){
                temp=getStringNine(temp.size());
                temp=(char)(e-1)+temp;
            }
            else{
                temp=str[i]+temp;
            }
            i--;
        }
        int n=temp.size();
   
    if(temp[0]=='0') temp=temp.substr(1,n-1);
    cout<<temp<<endl;
    }
}

