#include <bits/stdc++.h>
using namespace std;
#define ll long long

int main(){
	int t;
	cin>>t;
	for(int i=1;i<=t;i++){
		string num;
		cin>>num;
		int n = num.size();
		for(int j=n-1;j>0;j--){
			if(num[j] < num[j-1]){
				for(int k=j;k<n;k++)
					num[k]='9';
				num[j-1]-=1;
			}
		}
		cout<<"Case #"<<i<<": ";
		for(int k=0;k<n;k++){
			if(num[k]=='0')
				continue;
			else
				cout<<num[k];
		}
		cout<<"\n";
}
}