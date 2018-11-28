#include <iostream>
#include <math.h>
using namespace std;

void helper(int total, int k, int& maxx, int& minn){
	int level = (int)(log(k)/log(2));
	//cout<<"level "<<level<<endl;
	int order = k - (pow(2, level)-1);
	int base = (total - (pow(2, level) - 1))/pow(2, level);
	//cout<<"base "<<base<<endl;
	int num_big = total - (pow(2, level) - 1) - base*pow(2, level);
	//cout<<"order "<<order<<" num_big "<<num_big<<endl;
	if(order<=num_big){
		minn = (base+1-1)/2;
		maxx = base+1-1-minn;
	}
	else{
		minn = (base-1)/2;
		maxx = base-1-minn;
	}
}

int main(){
	int n;
	cin>>n;
	int total=0, k=0;
	for(int i = 0; i<n; i++){
		cin>>total>>k;
		int maxx=0, minn=0;
		helper(total, k, maxx, minn);
		cout<<"Case #"<<i+1<<": "<<maxx<<" "<<minn<<endl;
	}
	return 0;
}