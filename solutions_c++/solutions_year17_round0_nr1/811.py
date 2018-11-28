#include <iostream>
#include <cstdio>
#include <string>

#define MAX_S 1000

using namespace std;

string cake;
int K;
int fliptime;

int solve() {
	//printf("%s | %d\n", cake.c_str(), K);
	int i = 0;
	int count = 0;
	while (cake[i+K-1] != '\0') {
		if (cake[i]=='-') {
			for (int j=0; j<K; ++j){
				cake[i+j] = (cake[i+j] == '-') ? '+': '-';
			}
			++count;
			//printf("%s\n", cake.c_str());
		}
		++i;
	}
	while (cake[i] != '\0') {
		if(cake[i] == '-')
			return -1;
		++i;
	}

	return count;
}


int main() {

	freopen("A-large.in", "r", stdin);

	int T;
	cin >> T;

	for (int i = 0; i < T; ++i) {
		cin >> cake >> K;
		int res = solve();
		if (res != -1) printf("Case #%d: %d\n", i+1, res);
		else printf("Case #%d: IMPOSSIBLE\n", i+1);
	}

	return 0;
}
