#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
using namespace std;

#define LL long long

void run() {
	LL x;
	cin >> x;
	vector<int> A;
	LL z = x;
	while(z > 0) {
		A.push_back(z % 10);
		z /= 10;
	}
	reverse(A.begin(), A.end());
	// check orig
	int pos = -1;
	for(int i=1;i<A.size();++i)
		if (A[i]<A[i-1]) {pos = i; break;}
	if (pos < 0) {
		cout << x << endl;
		return ;
	}
	int t = A[pos-1];
	for(int i=pos-1;i>=0;--i)
		if(A[i] == t) {
			A[i] --;
			A[i + 1] = 9;
		}
		else break;
	for(int i=pos;i<A.size();++i)
		A[i] = 9;
	bool start = true;
	for(int i=0;i<A.size();++i) {
		if (A[i] == 0 && start) 
			continue;
		else
			start = false;
		cout << A[i];
	}
	cout << endl;
}

int main() {
	freopen("B-large.in","r",stdin);
	freopen("B.out","w",stdout);
	int T;
	cin >>T;
	for (int i=1;i<=T;++i) {
		printf("Case #%d: ", i);
		run();
	}
}
