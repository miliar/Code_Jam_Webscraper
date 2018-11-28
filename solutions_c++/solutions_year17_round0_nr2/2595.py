/*
*	Author: Suparshva Mehta 	Username: suparsh14
*	College: DA-IICT, India
*	GCJ Qualification Round
*	Q-B
*/

#include<bits/stdc++.h>

using namespace std;

long long brute(long long n){		//O(N)

		long long ans=1;

		for(long long i=1;i<=n;i++){

			vector<int> v;

			long long temp=i;

			while(temp){
				v.push_back(temp%10);
				temp/=10;
			}

			bool flag=1;

			for(int j=1;j<v.size();j++){
				if(v[j]>v[j-1]){
					flag=0;
					break;
				}
			}

			if(flag)ans=i;

	}

	return ans;
}

long long smart(long long n){	//O(log10(N)^2)

	long long temp=n;
	vector<int> v;

	while(temp){
			v.push_back(temp%10);				
			temp/=10;
		}

	reverse(v.begin(),v.end());

	for(int i=(int)v.size()-1;i>=0;i--){

		bool flag=0;

		for(int j=i+1;j<v.size();j++){
			if(v[j]<v[j-1]){
				v[j]=9;
				flag=1;
			}
		}
		if(flag)v[i]--;
	}

	long long ans=0;

	for(int i=0;i<v.size();i++){
		ans*=10;
		ans+=v[i];
	}

	return ans;
}


int main(){

	int T;
	cin>>T;

	for(int ca=1;ca<=T;ca++)
	{
		cout<<"Case #"<<ca<<": ";

		//logic starts here

		long long n;
		cin>>n;

		//cout<<brute(n)<<endl;
		cout<<smart(n)<<endl;
	}

	return 0;
}