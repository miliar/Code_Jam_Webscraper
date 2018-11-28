#include<bits/stdc++.h>
using namespace std;

//3  -> 1, 1
//4  -> 1, 3 -> 1, 1, 1
//5  -> 2, 2 
//6  -> 2, 3 -> 2, 1, 1
//7  -> 3, 3 -> 3, 1, 1 -> 1, 1, 1, 1
//8  -> 3, 4 -> 3, 2, 1 -> 1, 1, 2, 1
//9  -> 4, 4 -> 2, 1, 4 -> 2, 1, 2, 1
//10 -> 4, 5 -> 2, 2, 4 -> 2, 2, 2, 1
//11 -> 5, 5 -> 2, 2, 5 -> 2, 2, 2, 2 ->
//
//2(1) ->  4(3) -> 8(7) -> 16(15) -> 32(31) ->


void solve(){
	long long N, K;
	cin >> N >> K;

	long long people = 0;
	while(2*people + 1 < K){
		people = 2 * people + 1;
	}
	long long seg = people + 1;
	long long rest = N - people;
	
	long long small = rest/seg;
	long long big = rest/seg + 1;

 	long long smallnum;
	long long bignum;
	bignum = rest % seg;
	smallnum = seg - bignum;

	/*
	cout << endl;
	cout << "people " << people << endl;
	cout << "rest " << rest << endl;
	cout << "big " << big << " num " << bignum << endl;
	cout << "small " << small << " smallnum " << smallnum << endl;
	cout << endl;
	*/

	if(K - people <= bignum){
		if(big%2 == 1){
			cout << big/2 << " " << big/2 << endl;
		}else{
			cout << big/2 << " " << big/2 - 1<< endl;
		}
	}else{
		if(small%2 == 1){
			cout << small/2 << " " << small/2 << endl;
		}else{
			cout << small/2 << " " << small/2 - 1<< endl;
		}
	}
}

int main(){
	long long T;
	cin >> T;
	for(int i = 0; i < T; i++){
		cout << "Case #" << i + 1 << ":" << " ";
		solve();
	}
}

