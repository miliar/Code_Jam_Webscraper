#include<iostream>
#include<vector>
using namespace std;
int main() {
	int t,k=0;
	cin>>t;
	while(t--){
		++k;
		long long int a;
		cin>>a;
		vector<int> num;
		while(a!=0){
			int k=a%10;
			num.push_back(k);
			a=a/10;
		}
		for(int i=1;i<num.size();i++){
			if(num[i]>num[i-1]){
				num[i]-=1;
				for(int k=0;k<i;k++)
				num[k]=9;
			}
		}
		bool start=false;
		cout<<"Case #"<<k<<": ";
		for(int i=num.size()-1;i>=0;i--){
			if(num[i]!=0) start=true;
			if(start)
			cout<<num[i];
		}
		cout<<endl;
	}
	return 0;
}
