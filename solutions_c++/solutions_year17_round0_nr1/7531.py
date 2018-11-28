#include<iostream>
#include<String.h>
using namespace std;
int main(){
int t;
cin>>t;
for(int h=1;h<=t;++h){
string s;
int k;
cin>>s>>k;
int l = s.length(), i=0, flag=0, count=0;
while(i<l){
	if(s[i]=='-') {
		if(i+k>l) 
		{flag=1;break;}
		for(int h=i;h<i+k;++h)
			if(s[h]=='-') 
			s[h]='+'; 
			else 
			s[h]='-';
		count++;
//		cout<<s<<endl;
	}
	else i++;	
}
if(flag) cout<<"Case #"<<h<<": IMPOSSIBLE"<<endl;
else cout<<"Case #"<<h<<": "<<count<<endl;
}		
return 0;
}
