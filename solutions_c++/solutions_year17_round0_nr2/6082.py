#include<iostream>
#include<cstdio>

using namespace std;

typedef unsigned long long ull;

int T;
ull N;

bool isok() {
	ull m=1;
	while(N/m>0) {
		if( N%(100*m)/(10*m) > N%(10*m)/m ) return false;
		m*=10;
	}
	return true;
}

int main() {
	cin >> T;
	for(int numc=1; numc<=T; numc++) {
		cin >> N;
		ull mult=1;
		while(!isok()) {
			while( N%(10*mult)/mult != 9) {
				N-=mult;
			}
			mult*=10;
		}
		cout << "Case #" << numc << ": " << N << endl;
	}
	
	return 0;
}
