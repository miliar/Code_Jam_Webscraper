#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<utility>
using namespace std;

int T,N,R,O,Y,G,B,V;

void solve(){
    char c;
    char r;
    if(R>=Y && R>=B){
        if(R>Y+B){
            cout<<"IMPOSSIBLE";
            return;
        }
        c='R';
        R--;
    }
    else if(Y>=R && Y>=B){
        if(Y>R+B){
            cout<<"IMPOSSIBLE";
            return;
        }
        c='Y';
        Y--;
    }
    else if(B>=Y && B>=R){
        if(B>Y+R){
            cout<<"IMPOSSIBLE";
            return;
        }
        c='B';
        B--;
    }
    r=c;
    cout<<c;
    for(int i=1;i<N;i++){
        if(c=='R'){
            if(Y>B || (Y==B && r=='Y')){
                c='Y';
                Y--;
            }
            else{
                c='B';
                B--;
            }
            //cout<<"R to "<<c<<endl;
        }
        else if(c=='Y'){
            if(R>B ||(R==B && r=='R')){
                c='R';
                R--;
            }
            else{
                c='B';
                B--;
            }
        }
        else if(c=='B'){
            if(R>Y ||(R==Y && r=='R')){
                c='R';
                R--;
            }
            else{
                c='Y';
                Y--;
            }
        }
        cout<<c;
    }

}

int main(){
    cin>>T;
    for(int _c=1;_c<=T ; _c++){
        //Input
        cin>>N>>R>>O>>Y>>G>>B>>V;
        cout<<"Case #"<<_c<<": ";
        solve();
        cout<<endl;

    }
}
