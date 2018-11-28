#include<bits/stdc++.h>
using namespace std;
int Check(string s,int k){
int count=0;
for(int i=0;i<s.length()-k+1;i++){
if(s[i]=='-'){
for(int j=i;j<i+k;j++){
if(s[j]=='+')
s[j]='-';
else
s[j]='+';
}
count++;
}
}
for(int i=0;i<s.length();i++){
if(s[i]=='-')
return -1;
}

return count;
}
int main(){
freopen("inp1l.in","r",stdin);
freopen("outp1l.out","w",stdout);
int n,k;
string s;
cin>>n;
int l=1;
while(n--){
cin>>s;
cin>>k;
int ans=Check(s,k);
cout<<"Case #"<<l<<": ";
if(ans!=-1)
cout<<ans<<endl;
else
cout<<"IMPOSSIBLE"<<endl;
l++;
}
}
