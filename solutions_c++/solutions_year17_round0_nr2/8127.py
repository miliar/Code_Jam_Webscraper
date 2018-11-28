#include <bits/stdc++.h>
using namespace std;
void print(string & 	n){
	int f=0;
	for(char i:n){
		if(i!='0'||f!=0)
			cout<<i;
		if(i!=0)
			f=1;
	}
}
int main(){
	int T,i;
	cin>>T;
	for(int t=1;t<=T;t++){
		string n;
		cin>>n;
		//cout<<n<<endl;
		for(i=1;i<n.size();i++){
			if(n[i]<n[i-1])
				break;
		}
		if(i==n.size()){
			cout<<"Case #"<<t<<": "<<n<<endl;
			continue;
		}
		i--;
		while(i!=0&&n[i]==n[i-1]) i--;
		n[i]-=1;
		i++;
		while(i!=n.size()) n[i++]='9';
		cout<<"Case #"<<t<<": ";print(n);cout<<endl;
	}
}