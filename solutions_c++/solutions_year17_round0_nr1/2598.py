#include<iostream>
#include <string>
using namespace std;

void doatest(){
	string str;
	cin>>str;
	int k;
	cin>>k;
	int sum=0;
	int len=str.length();
	int i;
	for(i=0;i<len-k+1;i++){
		if(str[i]=='+')continue;
		sum++;
		for(int j=0;j<k;j++)
			if(str[i+j]=='+')
				str[i+j]='-';
			else
				str[i+j]='+';
	}
	for(;i<len;i++)
		if(str[i]=='-'){
			cout<<"IMPOSSIBLE"<<endl;
			return;
		}
	cout<<sum<<endl;
}

int main(){
	int n;
	cin>>n;
	for(int i=1;i<=n;i++){
		cout<<"Case #"<<i<<": ";
		doatest();
	}
	return 0;
}