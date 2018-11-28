#include<iostream>
#include<vector>
#include<fstream>
using namespace std;

long long int T;

bool istidy(long long int N){
	long long int prev=N%10;
	N=N/10;
	while(N>0){
		long long int r=N%10;
		if(prev<r)
			return false;
		prev=r;
		N=N/10;
	}
	return true;
}

long long int process(long long int N){
	vector<int>rev;
	while(N>0){
		rev.push_back(N%10);
		N=N/10;
	}
	
	vector<int>O;
	for(int i=rev.size()-1;i>=0;i--){
		O.push_back(rev[i]);
	}
	
	for(int i=O.size()-2;i>=0;i--){
		if(O[i]>O[i+1]){
			O[i]--;
			for(int j=i+1;j<O.size();j++){
				O[j]=9;
			}
		}
	}
	
	long long int n=0;
	for(int i=0;i<O.size();i++){
		n=n*10+O[i];
	}
	
	return n;
}

/*int main(){
	cout<<process(111111111111111110);
}*/

int main(){
	ifstream ifs("B-large (2).in");
	ifs>>T;
	vector<long long int>N;
	
	for(long long int i=0;i<T;i++){
		long long int n;
		ifs>>n;
		N.push_back(n);
	}
	
	vector<long long int>O;
	for(long long int i=0;i<T;i++){
		O.push_back(process(N[i]));
	}
	
	ofstream ofs("outputBLarge.txt");
	for(long long int i=0;i<T;i++){
		ofs<<"Case #"<<i+1<<": "<<O[i]<<"\n";
	}
}
