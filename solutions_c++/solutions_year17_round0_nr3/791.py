#include<iostream>
#include<cstdio> 
#include<cstring>
#include<string>
#include<cmath>
using namespace std;
const int INF = 1000000;

int T;
long long N, K;

void solve(long long & m, long long & n){
	int k = 0;
	long long res_B, d, tmp_k = K + 1; 
	long long used_B = 1, res_N; 
	while(tmp_k > 1){
		used_B *= 2;
		tmp_k /= 2; 
	}
	used_B -= 1;
	res_B = K - used_B; 
	d = (N + 1)/ (used_B + 1) - 1;
	res_N = N + 1- (used_B + 1) * (d + 1);
	if (res_B == 0){
		m = d; 
		n = d; 
		if(res_N > 0 && res_N >= (used_B + 1)/2 )
			m+=1;
		return ;
	}
	if(res_B <= res_N){
		m = (d + 1) / 2;
		n = d - m;
	}
	else{
		m = d / 2; 
		n = d - 1 - m;
	}
}


int main(){
	cin >> T; 
	int ans; 
	long long m = 0, n = 0;	
	for(int i = 0; i < T; i++){
		cin >> N >> K;
		solve(m, n);
		cout << "Case #"<< (i+1) << ": " << m << " " << n << endl; 
	}
	
	return 0;
}
