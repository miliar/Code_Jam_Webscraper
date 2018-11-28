#include<bits/stdc++.h>
using namespace std;

int main() {
ios_base::sync_with_stdio(false);
cin.tie(NULL);
int t;
cin>>t;
for(int f=1;f<=t;f++){
string s;
int k;
cin>>s>>k;
int cnt=0;
int i;
for( i=0;i+k-1<s.size();i++){
if(s[i]=='-'){
	cnt++;
for(int j=0;j<k;j++){
if(s[i+j]=='-') s[i+j]='+';
	else s[i+j]='-';

}

}

}
for(;i<s.size();i++){
if(s[i]=='-') cnt=INT_MAX;
}
if(cnt==INT_MAX) cout<<"case #"<<f<<": IMPOSSIBLE\n";
	else cout<<"case #"<<f<<": "<<cnt<<"\n";

}

}