#include <bits/stdc++.h>
#define DEBUG(x) cout << #x << " :" << x << endl;
using namespace std;

char n[20];
int cnt;

void print(){
	int i = 0;
	while(n[i] == '0') ++i;
	cout << "Case #" << cnt << ": " << (n + i) << endl;
}


void sol(){
	bool tidy = false;
	int j = strlen(n);

	//finding first idx where tidyness is violated
	while(tidy == false){
		tidy = true;
		int i = 1;

		while(n[i] && n[i] >= n[i - 1]) ++i;

		if (i < j && n[i])	tidy = false;
		else break;

		j = i;
		--i;

		int diff = n[i] - '0' - 1 + 10;
		n[i] = '0' + (diff % 10);
	}

	while(n[j]){
		n[j++] = '9';
	}

	print();
}

int main(){
	int T;	
	cnt = 0;
	cin >> T;

	while(T--){
		cin >> n;
		++cnt;
		sol();
	}

	return 0;
}