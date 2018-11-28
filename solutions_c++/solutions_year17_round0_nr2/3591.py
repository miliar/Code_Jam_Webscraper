#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool check(long long n){
	vector<long long> x;
	while(n>0){
		x.push_back(n%10);
		n=n/10;
	}
	int prev=9;
	for(int i=0;i<x.size();i++){
		if(x[i]>prev)return false;
		prev=x[i];
	}
	return true;
}

int main(){
	int t;
	cin>>t;
	for(int j=1;j<=t;j++){
		long long n;
		cin>>n;
		bool f=true;
		vector<long long> x;
		while(f){
			if(check(n)){
				x.push_back(n);
				f=false;
			}
			else{
				x.push_back(9);
				n=n/10;
				n--;
				// cout<<"dsg "<<n<<endl;;
			}
		}
		cout<<"Case #"<<j<<": ";
		for(int i=x.size()-1;i>=0;i--){
			if(x[i]!=0)
			cout<<x[i];
		}
		cout<<endl;
	}
}