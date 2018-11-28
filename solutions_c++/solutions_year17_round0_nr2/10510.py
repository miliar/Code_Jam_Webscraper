#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>

using namespace std;

int t, n;

bool istidy(int n){
	char buff[1007];
	itoa(n, buff, 10);
	// cout << buff << endl;
	int l = strlen(buff);
	for(int j = 1; j < l; j++){
		if(buff[j] < buff[j-1])
			return false;
	}
	return true;
}


int main(){
	cin >> t;
	for(int i=1; i<=t; i++){
		cin >> n;
		while(!istidy(n)){
			n--;
		}
		printf("Case #%d: %d\n", i, n);
	}
	return 0;
}