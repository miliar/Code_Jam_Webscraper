#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

int main(){
	string x;
	int t;
	cin>>t;
	int cse=1;
	while(t--){
		cout<<"Case #"<<cse++<<": ";
		cin>>x;
		for(int i=x.size()-1;i>0;i--){
			if((int)x[i]<(int)x[i-1]){
				x[i-1]--;
				for(int j=i;j<x.size();j++)x[j]='9';
			}
		}
		if(x[0]!='0')cout<<x[0];
		for(int i=1;i<x.size();i++){
			cout<<x[i];
		}
		cout<<"\n";
	}
	return 0;
}
