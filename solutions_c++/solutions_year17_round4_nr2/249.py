#include <cstdio>
#include <iostream>
#include <ctime>
#include <iomanip>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cstring>
using namespace std;
int N, C, M;
int P[1001], B[1001];



void mainfunc(){
	cin >> N >> C >> M;
	for(int i = 1; i <= N; i++){
		P[i] = 0;
	}
	for(int i = 1; i <= C; i++){
		B[i] = 0;
	}
	for(int i = 0; i < M; i++){
		int p, b;
		cin >> p >> b;
		P[p] ++;
		B[b] ++;
	}
	int y = 0;
	for(int i = 1; i <= C; i++){
		if(y < B[i]) y = B[i];
	}
	int sum = 0;
	for(int i = 1; i <= N; i++){
		sum += P[i];
		int a = (sum + i - 1)/i;
		if(a > y) y = a;
	}

	int z = 0;
	for(int i = 1; i <= N; i++){
		if(P[i] > y) z += P[i] - y;
	}
	printf("%d %d\n" , y , z);
}


int main() {
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		printf("Case #%d: " , i);
		mainfunc();
	}
}