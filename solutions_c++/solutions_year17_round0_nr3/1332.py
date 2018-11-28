#include <iostream>
#include <stdio.h>
#include <string>
#include <math.h>
#include <vector>
#include <stdlib.h>

using namespace std;

int compare (const void * a, const void * b)
{
	return ( *(int*)a - *(int*)b );
}


int logo(long long number){
	long long aux = 1;
	int ans = -1;
	while (number >= aux) {
		ans++;
		aux = (long long) 2*aux;
	}
	return ans;
}


long long poo(int expo){
	int i;
	long long ans = 1;
	for (i = 0; i < expo; i++) {
		ans = (long long) 2*ans;
	}
	return ans;
}


void * solve(){
	void * ans;
	long long nr, kei, pw, mai, gap, aux;
	int logk;
	cin >> nr >> kei;
	
	logk = logo(kei);
	pw = poo(logk);
	mai = (long long) ((long long) nr + 1)%pw;
	
	gap = (long long) ((long long) nr + 1 - mai)/pw;
	
	if(mai <=  (kei - pw)){
		gap = (long long) gap - 1;
	}
	
	aux = (long long) gap - 1;
	if (aux%2 == 0) {
		cout << (long long) aux/2 << " " << (long long) aux/2;
	}
	else {
		cout << (long long) ((long long) aux + 1)/2 << " " << (long long) ((long long) aux - 1)/2;
	}

	return ans;
}




int main (int argc, char * const argv[]) {
    int ncases, cases;
	scanf("%d\n", &ncases);
	for (cases = 0; cases < ncases; cases++) {
		cout << "Case #" << cases + 1 << ": ";
		solve();
		cout << endl;
	}
    return 0;
}