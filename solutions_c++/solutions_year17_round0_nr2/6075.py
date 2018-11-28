#include<iostream>

using namespace std;

bool isTidy(long long n) {
	bool flag = true;
	int d = n % 10;
	n /= 10;
	while(n) {
		int e = n % 10;
		n /= 10;
		if(e > d) {
			flag = false;
			break;
		}
		d = e;
	}
	return flag;
}

int main() {
	int t;
	cin>>t;
	for(int i=1;i<=t;i++) {
		long long n;
		cin>>n;
		long long toMinus = 10, toAdd = 9;
		while(!isTidy(n)) {
			n = n / toMinus * toMinus - toMinus + toAdd;

			toMinus *= 10;
			toAdd = toMinus - 1;
		}
		cout<<"Case #"<<i<<": "<<n<<endl;
	}
	return 0;
}
