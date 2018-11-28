#include<bits/stdc++.h>
using namespace std;

int main() {
ios_base::sync_with_stdio(false);
cin.tie(NULL);
int t;
cin>>t;
for(int f=1;f<=t;f++){
string s;
cin>>s;
int mark=s.size();
for(int i=s.size()-2;i>=0;i--){
if(s[i]>s[i+1]) s[i]--,mark=i;
}
for(int i=mark+1;i<s.size();i++)
s[i]='9';
cout<<"Case #"<<f<<": ";
if(s[0]=='0')
	cout<<s.substr(1)<<"\n";
	else
cout<<s<<"\n";
}

}