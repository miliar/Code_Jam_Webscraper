#include<bits/stdc++.h>
using namespace std;

string ntos(long long n){
        stringstream ss;
        ss<<n;
        string s;
        ss>>s;
        return s;
}

long long ston(string n){
        stringstream ss;
        ss<<n;
        long long  s;
        ss>>s;
        return s;
}

int pos(string s){
    for(int i=0;i<s.size()-1;++i){
        if(s[i+1]<s[i]){
           return i;
        }
    }
    return -1;
}

string llenar(string s, int pos){
    s[pos]=s[pos]-1;

    for(int i=pos+1;i<s.size();++i){
        s[i]='9';
    }
    return s;
}

int main(){
    freopen ("B-large.in","r",stdin);
    freopen ("Blargaoutput.out","w",stdout);
int T;
cin>>T;
long long n;
string s;
for(int t=1;t<=T;++t){
    cin>>n;
    s=ntos(n);
    int p=pos(s);
    string ans=s;
    while(p!=-1){
        ans=llenar(s,p);
        p=pos(ans);
    }
    long long a=ston(ans);
    cout<<"Case #"<<t<<": "<<a<<endl;
}
return 0;}
