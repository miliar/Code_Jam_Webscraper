#include<iostream>
#include<stdio.h>
//check with single digit number
using namespace std;

int val(char ch){
    return (ch-48);
}

int isTidy(string str){

   if(str.size()==1) return 1;

   for(int i=str.size()-1 ; i>=1; i--)
        if(str[i]<str[i-1]) return 0;

    return 1;
}

int main(){

int T;
string str;

//freopen("B-large.in","r",stdin);
//freopen("B.out","w",stdout);

cin>>T;

for(int t=1; t<=T; t++){

cin>>str;

if(isTidy(str)==1){
    cout<<"Case #"<<t<<": ";
    cout<<str<<endl;
    continue;
}


bool first=true;

for(int i=str.size()-1; i>=1; i--){
    /*
    if(first){
        if( (val(str[i]) - 1 ) >= val(str[i-1]) ){
            //str[i] = (val(str[i]) - 1 ) + 48 ;
            //break;
            continue;
            }
         first = false;
         str[i] = '9';
         //cout<<"before: "<<str[i-1]<<endl;
         str[i-1] = ( val(str[i-1]) - 1 ) + 48;
         //cout<<"after: "<<str[i-1]<<endl;
    }
    else{*/
        if( (val(str[i]) - 0 ) >= val(str[i-1]) ){
            //str[i] = (val(str[i]) - 1 ) + 48 ;
            //break;
            continue;
            }
         //str[i] = '9';
         int ind = i;
         while(ind<str.size()){ str[ind] = '9'; ind++;}
         str[i-1] = ( val(str[i-1]) - 1 ) + 48;
    //}
}

cout<<"Case #"<<t<<": ";

int beg=0;

if(str[0]=='0') beg=1;

for(int i=beg; i<str.size();i++) cout<<str[i];

cout<<endl;

}

return 0;
}
