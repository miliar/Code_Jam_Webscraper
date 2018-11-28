#include <iostream>
#include <vector>
using namespace std;

unsigned long long helper(unsigned long long maxx){
	unsigned long long temp = maxx;
	unsigned long long result = 0;
	unsigned long long base = 10;
	vector<int> bits;
	while(temp%base||temp/base){
		bits.push_back(temp%base);
		temp/=10;
	}
	int remain = bits.size()-1;
	while(remain&&remain<bits.size()){
		if(bits[remain]<=bits[remain-1]){remain--; continue;}
		bits[remain]--;
		if(remain==bits.size()-1||bits[remain+1]<=bits[remain]) break;
		remain++;
	}
	base = 1;
	for(int i = 0; i<bits.size(); i++){
		if(i<remain){
			result+=base*9;
		}
		else{
			result+=base*bits[i];
		}
		base*=10;
	}
	return result;
}

int main(){
	int n;
	cin>>n;
	unsigned long long maxx;
	for(int i = 0; i<n; i++){
		cin>>maxx;
		cout<<"Case #"<<i+1<<": "<<helper(maxx)<<endl;
	}
	return 0;
}