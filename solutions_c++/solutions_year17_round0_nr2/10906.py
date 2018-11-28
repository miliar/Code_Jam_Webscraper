#include<iostream>
#include<algorithm>
#include<string>
#include<fstream>
#include<vector>
using namespace std;

int check(long long int n){
	vector<int> first;
	int val = 0;
	first.clear();
	while(n != 0){
		int x = n%10;
		first.push_back(x);
		n/=10;
	}
//	std::reverse(myvector.begin(),myvector.end());
	for(int i=0; i<first.size()-1; i++){
		if(first[i] < first[i+1]){
			return -1;
		}
	}
	return val;
}

int main()
{
	int t;
	cin>>t;
	ofstream output("cj17.dat");
	for(int k=1; k<=t; k++){
		long long int cnt=0, l, n, ans=0;
		cin >> n;
		while(check(n) != 0){
			n-=1;
		}
		ans = n;
		output << "Case #"<<k<<": "<<ans<<"\n";
	}
}
