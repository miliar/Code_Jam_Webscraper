#include <iostream>

using namespace std;

long long last(long long n){
	return n%10;
}

long long head(long long n){
	return n/10;
}

bool tidy(long long n){
	return n < 10 || (tidy(head(n)) && last(n) >= last(head(n)));
}

long long maketidy(long long n){
	return tidy(n) ? n : maketidy(head(n)-1)*10 + 9;
}

int main(){

	int t;
	cin>>t;

	for(int test = 1; test <= t; test++){
		long long n;
		cin>>n;

		cout<<"Case #"<<test<<": "<<maketidy(n)<<endl;
	}

	return 0;
}