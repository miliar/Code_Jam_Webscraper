#include<bits/stdc++.h>
using namespace std;


int main() {
 int n,t,a,b,c;
 cin>>t;


 for(int i=1;i<=t;i++){
        cin>>n;
        a=n/100;
        b=(n/10)%10;
        c=n%10;

        if((a<b)&&(b<c)&&(a<c)){

        }
       else if((a>=b)&&(b>=c)&&a>c){
            a--;
            b=9;
            c=9;
       }
       else if((a<b)&&(b>c)){
        b--;
        c=9;
       }
       else if((a>b)&&(b<=c)&&(a<=c)){
        a--;
        b=9;
        c=9;
       }
       else if((a>b)&&(b<c)&&(a>c)){
        a--;b=9;c=9;
       }
        if((a==0)&&(b==0)){
            cout<<"Case #"<<i<<": "<<c<<endl;

        }
        else if((a==0)&&b!=0){
            cout<<"Case #"<<i<<": "<<b<<c<<endl;
        }
        else

       cout<<"Case #"<<i<<": "<<a<<b<<c<<endl;

 }
 return 0;
}
