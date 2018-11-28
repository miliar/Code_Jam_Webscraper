# include <iostream>
# include<string>

using namespace std;


void solve(string &s,int l, int k){
      for(int i=l; i<=l+k-1;i++){
        if(s[i]=='-'){
            s[i]='+';
        }
        else{
            s[i]='-';
        }}

}

int main(){
int t,k;
int count=0;
string s;
cin>>t;
for(int j=1;j<=t;j++){
    cin>>s>>k;
    count=0;
    for (int i=0;i<s.length()-k+1;i++){
        if(s[i]=='-'){
        solve(s,i,k);
        count++;
}
}
    int f=0;
    for(int i=0;i<s.length();i++){
        if(s[i]=='-'){
            f=0;
            break;}
        else{
            f=1;
            }}
    if(f==0){
        cout<<"Case #"<<j<<": IMPOSSIBLE"<<endl;
}
    else{
        cout<<"Case #"<<j<<": "<<count<<endl;

}}
return 0;
}
