#include<bits/stdc++.h>
#define ll long long int

int val(char c){
    return c-48;
}

int main(){
    int t; scanf("%d",&t);
    ll n,tidy=0,fl;
    for(int j=1;j<=t;j++){
        tidy=0; fl=0; ll dec=0;
        std::string s; std::cin>>s;
        int valS=val(s.at(0));
        for(int i=1;i<s.length();i++){
            if(valS<=val(s.at(i)) && fl==0){
                tidy=tidy*10+valS;  valS=val(s.at(i));
            }
            else if(fl==1) tidy=tidy*10+9;
            else {fl=1; if(tidy%10<=(valS-1)){ } else{ dec=tidy*10;}tidy=tidy*10+(valS-1); valS=9;}
        }
        printf("Case #%d: %lld\n",j,tidy*10+valS-dec);
    }
}
