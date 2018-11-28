#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
using namespace std;
int arr[2] = {0};
unsigned int powOf2[65];

unsigned int pow2(int k) {
	if(powOf2[k] != 0) return powOf2[k];
	
	powOf2[k] = pow2(k/2) * pow2(k/2) ;
	if(k % 2) 
		powOf2[k] *= 2;

	return powOf2[k];
	 
} 
int prev[200] = {0};
int cur[200] = {0};
void fun(unsigned int N, unsigned int K) 
{
	if(N == 0 || N == 1) {
	
		arr[0] = 0;
		arr[1] = 0;
		return;
	}
	if (K == 1) 
	{
		
		arr[0] = (N - 1) / 2;
		arr[1] = N / 2;
		return;
	}
	unsigned int q = ceil(log2(K + 1) - 1);
	// cout << q << "q\n";
	unsigned int result = N / pow2(q);
	unsigned int table[3][2] = {0}, prevTable[3][2] = {0};
	table[0][0] = N, table[0][1] = 1;
	prevTable[0][0] = N, prevTable[0][1] = 1;
	unsigned int a = N , b = N;
	for (int i = 1; i <= q; i++) {

		int temp = prevTable[0][0];
		table[0][0] = temp / 2;
		table[1][0] = temp / 2 - 1;
		table[0][1] = 0, table[1][1] = 0;
		if(temp % 2)
			table[0][1] = prevTable[0][1] * 2;
		else {
			table[0][1] = prevTable[0][1];
			table[1][1] = prevTable[0][1];
		}
		// if(i == 1)
		// 	continue;
		temp = prevTable[1][0];
		if(temp % 2 ) {
			if(table[0][0] == temp / 2) 
				table[0][1] += prevTable[1][1] * 2;
			else
				table[1][1] += prevTable[1][1] * 2;
		} else {
			table[0][1] += prevTable[1][1];
			table[1][1] += prevTable[1][1];
		}
		// cout << table[0][0] << ":" << table[0][1] << endl;
		// cout << table[1][0] << ":" << table[1][1] << endl;
		// cout << "------------------" << endl;
		for(int i = 0; i < 2; i++)
			for(int j = 0; j < 2; j++)
				prevTable[i][j] = table[i][j];
	}

	
	int seri = K - pow2(q) + 1;
	// cout << seri << ")";
	// cout << table[1][1] << "," << table[0][1] << "(";
	if(table[0][1] >= seri) {
		fun(table[0][0], 1);
	}
	else {
		// cout << table[1][0] << "r";
		fun(table[1][0] , 1);
	}
	


}
int main() {
	powOf2[0] = 1;
	powOf2[1] = 2;

	int T;
	scanf("%d", &T);
	unsigned int N, K;
	for(int time = 1; time <= T; time++) {
		scanf("%d %d", &N, &K);
		// cout << "/------------------/" << endl;
		fun(N, K);
		cout << "Case #" << time << ": " 
		// << N << "," << K << ":"  
		<< arr[1] << " " << arr[0] << endl;
		// cout << endl;

	}
}