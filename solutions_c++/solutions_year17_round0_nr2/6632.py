#include<bits/stdc++.h>
using namespace std;

string to_string(long long n){
    string s="";
    int rem=0;
while(n>0){
    rem=n%10;
    s=(char)(rem+'0')+s;
    n=n/10;
//cout<<
}
//cout<<s<<endl;
return s;
}

int main() {
    freopen("inpb.txt","r",stdin);
freopen("outtb.txt","w",stdout);
int T,u=1;
cin>>T;
while(T--){

long long N;
int i;
cin>>N;
string s = to_string(N);
cout<<"Case #"<<u<<": ";
			u+=1;
for(i=0;i<s.size()-1;i++){
if(s[i]>s[i+1]){
break;
}
}



if(i==s.size()-1){
cout<<s<<endl;
continue;
}

string ans="";
if(s[i]=='1'){

for(i=0;i<s.size()-1;i++){
ans+="9";
}
cout<<ans<<endl;
continue;
}
//cout<<s[i]<<endl;
while(i>=0){

if(s[i]!=s[i-1])
    break;
i--;
}
ans+=s.substr(0,i);
ans+=(char)(((int)s[i]) - 1);
for(int j=i+1;j<s.size();j++){
ans+="9";
}

cout<<ans<<endl;
}


return 0;
}
