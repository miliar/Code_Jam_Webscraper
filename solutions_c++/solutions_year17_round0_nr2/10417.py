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
	while(N>=1){
		if(istidy(N))
			return N;
		N--;
	}
}

int main(){
	ifstream ifs("B-small-attempt0.in");
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
	
	ofstream ofs("output.txt");
	for(long long int i=0;i<T;i++){
		ofs<<"Case #"<<i+1<<": "<<O[i]<<"\n";
	}
}
