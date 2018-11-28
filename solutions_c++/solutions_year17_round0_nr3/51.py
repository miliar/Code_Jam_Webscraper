#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<map>
using namespace std;

#define LL long long

void run() {
	LL N, K;
	cin >> N >> K;
	map<LL,LL> H;
	H[N] = 1;
	while(H.size() > 0) {
		auto iter = H.rbegin();
		auto x = iter->first;  // len
		auto y = iter->second;  // amount
		LL a = (x - 1) / 2;
		LL b = (x - 1) - a;
		if (y >= K) {
			cout << b << " " << a << endl;
			return ;
		}
		H.erase(x);
		K -= y;
		if (a > 0) H[a] += y;
		if (b > 0) H[b] += y;
	}
	cout << "0 0"<<endl;
}

int main() {
	freopen("C-large.in","r",stdin);
	freopen("C.out","w",stdout);
	int T;
	cin >>T;
	for (int i=1;i<=T;++i) {
		printf("Case #%d: ", i);
		run();
	}
}
