#include<iostream>
using namespace std;
#define ll long long int
int main(){
    ll T,T1=0;
    cin>>T;
    while(T--){
        string S,s1;
        int flg=2;
        ll K,countn=0,i;
        cin>>S>>K;
        s1="";
        for(ll i=0;i<S.size();i++){
            s1+='+';
        }
        if(S.compare(s1)==0){
            flg=1;
        }
        else{
                for(i=0;i<S.size();i++){
                    if(S[i]=='+'){continue;}
                    else if(S[i]=='-' && (i+K-1)<S.size()){
                        for(ll j=i;j<=(i+K-1);j++){
                            if(S[j]=='-'){S[j]='+';}
                            else{S[j]='-';}
                        }
                        ++countn;
                    }
                    else{flg=3;break;}
                }
        if(S.compare(s1)!=0){flg=3;}
        }
        cout<<"Case #"<<++T1<<": ";
        if(flg==1){cout<<0;}
        else if(flg==2){cout<<countn;}
        else{cout<<"IMPOSSIBLE";}
        cout<<endl;
    }
return 0;
}
