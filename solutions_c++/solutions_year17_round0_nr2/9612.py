#include<iostream>
using namespace std;
#define ll long long int
inline bool checkTidy(ll N){
    ll a=N%10,b=0;
    N/=10;
    while(N!=0){
        b=N%10;
        if(b>a){return false;}
        a=b;
        N/=10;
    }
    return true;
}
int main(){
    ll T,T1=0;
    cin>>T;
    while(T--){
        ll N,num=0;
        cin>>N;
        if(N<10){
            num=N;
        }
        else{
                if(checkTidy(N)){
                    num=N;
                }
                else{
                    for(ll i=N-1;i>=0;i--){
                        if(checkTidy(i)){
                            num=i;
                            break;
                        }
                    }
                }
        }
        cout<<"Case #"<<++T1<<": "<<num<<endl;
    }
return 0;
}
