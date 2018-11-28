#include<iostream>
#include<string>
using namespace std;
int T,K;
string S;
void flip(string & s,int t){
    for(int i=0;i<K;i++){
        if(s[t+i] == '+')
            s[t+i] = '-';
        else
            s[t+i] = '+';
    }
}
int solve(string s,int k){
    int ret = 0;
    for(int i=0;i<s.size();i++){
        if(s[i] == '-'){
            if((s.size()-i)<K)
                return -1;
            ret ++;
            flip(s,i);
        }
    }
    return ret;
}
int main(){
    cin>>T;
    for (int _c=1; _c<=T;_c++){
       cin>>S>>K;
       int r = solve(S,K);
       cout<<"Case #"<<_c<<": ";
       if(r >= 0)
           cout<<r<<endl;
       else
           cout<<"IMPOSSIBLE"<<endl;
    }
    return 0;
}
