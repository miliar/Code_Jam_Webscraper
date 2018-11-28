#include<bits/stdc++.h>
using namespace std;
string Check(string n){
    if(n.length()==1)
        return n;
int flag=0;
string str;
for(int i=0;i<n.length()-1;i++){
   //     cout<<"i:"<<n[i]<<endl;
if(n[i+1]<n[i]){
n[i]--;

for(int j=i+1;j<n.length();j++ )
n[j]='9';
if(n[0]!='0'){
     str=Check(n);
flag=1;
}
}
}
if(flag==0)
return n;
else
    return str;

}
int main(){
freopen("inp.in","r",stdin);
freopen("outp.out","w",stdout);
int t;
string n;
cin>>t;
int l=1;
while(t--){

cin>>n;
string ans=Check(n);
//cout<<"Ans"<<ans<<endl;
int i=0;
while(ans[i]=='0'){

    i++;
}
cout<<"Case #"<<l<<": "<<ans.substr(i)<<endl;
l++;
}
return 0;
}
