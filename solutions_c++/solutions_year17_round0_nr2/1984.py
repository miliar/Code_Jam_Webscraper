
#include <iostream>

using namespace std;


typedef long long ll;
typedef pair<int,int> pii;



ll table[20][10];
ll T(int i, int j){
	if(i == 1) return 1;

	if(table[i][j] != -1) return table[i][j];

	ll res = 0;
	for(int k=j; k<10; k++){
		res += T(i-1,k);
	}

	table[i][j] = res;
	return res;
}

ll get_kth(ll k){
	ll res = 0;

	int num_digits = 1;
	ll num_before = 0;
	while(num_before + T(num_digits+1,1)< k){
		num_before += T(num_digits+1,1);
		num_digits++;
	}

	int r = 1;
	while(num_digits > 0){
		int d = r;
		while(num_before + T(num_digits,d) < k){
			num_before += T(num_digits,d);
			d++;
		}
		r = d;
		res *= 10;
		res += d;
		num_digits--;
	}

	return res;
}

bool is_inc(ll N){
	ll last = N % 10;
	N /= 10;
	while(N != 0){
		if(last < N%10) return false;
		last = N%10;
		N /= 10;
	}

	return true;
}

ll ans(ll N){
	ll i=1;
	ll j=1;
	while(get_kth(j) < N){
		j *= 2;
	}

	while(i != j){
		ll m = i+(j-i)/2;
		if(get_kth(m) <= N){
			i = m+1;
		}else{
			j = m;
		}
	}

	return get_kth(i-1);
}

int main(){
	for(int i=0; i<20; i++){
		for(int j=0; j<10; j++){
			table[i][j] = -1;
		}
	}
	for(int i=1; i<10; i++){
		table[1][i] = 1;
	}

	int T;
	cin >> T;

	for(int tsc=0; tsc<T; tsc++){
		ll N;
		cin >> N;
		if(is_inc(N)){
		cout << "Case #"<<tsc+1<<": "<<N<<endl;
		}else{
		cout << "Case #"<<tsc+1<<": "<<ans(N)<<endl;
		}
	}
}
