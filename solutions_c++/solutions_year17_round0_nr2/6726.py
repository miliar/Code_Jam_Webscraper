#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

int main(){
int T;
cin>>T;
for(int t=1;t<=T;t++){
string n;
bool f=0;
int k=0;
cin>>n;
for(int q=0;q<(n.length()-1);q++){
f=0;
for(int i=0;i<(n.length()-1);i++){
	if(f){
		n[i+1]='9';
		}
	else if(n[i]>n[i+1]){
		n[i]=n[i]-1;
		n[i+1]='9';
		f=1;
		}
	
	}
k=0;
if(n[0]=='0'){
	k=1;
	}
}	
		
cout<<"Case #"<<t<<": "<<n.substr(k)<<endl;

}
}
