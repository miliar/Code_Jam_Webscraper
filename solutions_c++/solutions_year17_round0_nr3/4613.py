#include <iostream>
#include <fstream>
#include <algorithm>
//#include <list>
//#include <stack>
//#include <vector>
#include <string>
#include <cstring>
#include <cstdio>
//#include <unordered_map>
//#include <map>
#include <queue>

using namespace std;

typedef unsigned long long L;

int main(int ac, char **av)
{
	int T;
	cin >> T;
	L Ls, Rs;
	for (int i = 1 ; i <= T; i++) {
		L N, K;
		priority_queue<L> Q;

		cin >> N >> K;
		Q.push(N);

		for (int k = 0; k < K; k++) {
			L t = Q.top();
			Q.pop();
			Ls = (t-1)/2;
			Rs = (t-1-Ls);
			//printf("L=%d Ls=%d Rs=%d\n", l, Ls, Rs);
			Q.push(Ls);
			Q.push(Rs);
		}
		cout << "Case #" << i << ": " <<  max(Ls, Rs) << " "<< min(Ls,Rs) << endl;
	}
	return 0;
}

