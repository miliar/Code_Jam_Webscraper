#include <bits/stdc++.h>

using namespace std;
int main(){
	int t;
	long int n;
	int i,j,k;
	int done;

	cin>>t;

	for(i=0;i<t;i++){
		cin>>n;
		string number = to_string(n);
		int length = number.length();
		done = length;
		for(j=length-1;j>0;j--){
			if(number[j]<number[j-1]){
				number[j-1]=number[j-1]-1;
				for(k=j;k<done;k++){
					number[k]='9';
				}
				done = k;
			}
		}
		if(number[0]=='0')
			cout<<"Case #"<<i+1<<": "<< stol(number,nullptr,10)<<endl;
		else
			cout<<"Case #"<<i+1<<": "<< number<<endl;

	}
}