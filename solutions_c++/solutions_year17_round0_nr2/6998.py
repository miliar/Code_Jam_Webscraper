#include<iostream>
#include<stdio.h>
#include<cstring>

using namespace std;

long long int toint(char);

int main(){
    string str;
    int T;
    cin>>T;
    for(long long int x=0;x<T;x++){

    cin>>str;
    for(long long int i=str.length()-1;i>0;i--){
        if (toint(str[i])<toint(str[i-1])){
        for(long long int j=i;j<str.length();j++){
            str[j]='9';
        }
            str[i]='9';
            long long int digit;
            if(toint(str[i])){
                digit=toint(str[i-1])-1;
            }else{
                digit=9;
            }
            if(digit==0)
                str[i-1]='0';
            else if(digit==1)
                str[i-1]='1';
            else if(digit==2)
                str[i-1]='2';
            else if(digit==3)
                str[i-1]='3';
            else if(digit==4)
                str[i-1]='4';
            else if(digit==5)
                str[i-1]='5';
            else if(digit==6)
                str[i-1]='6';
            else if(digit==7)
                str[i-1]='7';
            else if(digit==8)
                str[i-1]='8';
            else if(digit==9)
                str[i-1]='9';
        }
    }
    if(toint(str[0])!=0){
        cout<<"Case #"<<x+1<<": "<<str<<endl;
    }
    else{
        str.erase(0,1);
        cout<<"Case #"<<x+1<<": "<<str<<endl;
    }
    }
    return 0;
}

long long int toint(char a){
    return a-'0';
}
