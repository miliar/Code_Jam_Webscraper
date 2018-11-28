#include<bits/stdc++.h>
using namespace std;
ifstream fin("C:\\Users\\Vamseedhar\\Downloads\\A-large.in");
ofstream fout("C:\\Users\\Vamseedhar\\Downloads\\counting sheep1.txt");
int pos(string s){
int l=s.length();
for(int i=0;i<l;i++){
    if(s[i]=='-'){
        return i;
    }
}
}
int check(string s){
int l=s.length();
for(int i=0;i<l;i++){
    if(s[i]=='-'){
        return 0;
        break;
    }
}
return 1;
}
int main(){
int t;
fin>>t;
for(int j=1;j<=t;j++){
    string s;
    int n,ans=0;
    fin>>s>>n;
    int l=s.length();
    int k=pos(s),p=0;
    if(check(s)==1){
       fout<<"Case #"<<j<<": "<<ans<<endl;
       p++;
    }
    else{
    while(k+n<=l){
            //cout<<k<<endl;
        for(int i=k;i<(k+n);i++){
            if(s[i]=='+'){
                s[i]='-';
            }
            else{
                s[i]='+';
            }
        }
        ans++;
        //cout<<"vamsee<<endl"<<endl;
        if(check(s)==1){
            fout<<"Case #"<<j<<": "<<ans<<endl;
            p++;
            break;
        }
        else{
            k=pos(s);
        }
    }
}
if(p==0)
fout<<"Case #"<<j<<": "<<"IMPOSSIBLE"<<endl;
}
}
