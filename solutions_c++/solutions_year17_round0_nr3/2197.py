#include<iostream>
#include<cmath>
#define ull unsigned long long

using namespace std;

ull N,k;
ull min_,max_;
ull cur;

void print(ull n) {
	cout<<(n/2)<<" "<<max( (n-1)/2, (ull)0)<<endl;
}

void solve(ull min_c, ull max_c) {
	//cout<<"---------min "<<min_<<" "<<min_c<<endl;
	//cout<<"---------max "<<max_<<" "<<max_c<<endl;
	if(cur+max_c >= k) {
		print(max_);
		return;
	}
	cur += max_c;
	if(cur+min_c >= k) {
		print(min_);
		return;
	}
	cur += min_c;
	if( (min_ == max_)){
		if(min_ % 2 == 0) {
			max_ = min_/2;
			min_ = (min_ - 1)/2;
			solve(min_c+max_c, min_c+max_c);
		}else{
			max_ = min_/2;
			min_ = min_/2;
			solve(min_c+max_c, min_c+max_c);
		}
	} else{

		if(min_ % 2 == 0){
			max_ = min_/2;
			min_ = (min_ - 1)/2;
			solve(min_c,  min_c + 2*max_c);
		}else if(max_ % 2 == 0){
			min_ = (max_ - 1)/2;
			max_ = max_/2;
			solve(2*min_c + max_c, max_c);
		}
	}
}


void solve_() {
	if(k==1) {
		print(N);
	} else {
		min_ = (N-1)/2;
		max_ = N/2;
		cur = 1;
		solve(1,1);
	}
}

int main(){
	int T;
	cin>>T;
	for(int t=1;t<=T;t++){
	cin>>N>>k;
	cout<<"Case #"<<t<<": ";
	solve_();
	}
	return 0;
}
