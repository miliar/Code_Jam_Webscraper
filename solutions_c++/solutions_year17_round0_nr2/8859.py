#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool judge(int n) {
	vector<int> v;
	while(n) {
		v.push_back(n%10);
		n /= 10;
	}
	int last = 10;
	for(int i = 0; i < v.size(); i++) {
		if(v[i] > last) return false;
		last = min(last, v[i]);
	}
	return true;
}

int main()
{
	int n, T;
	freopen("B-small-attempt0.in","r",stdin);
	freopen("Boutput_small.txt","w",stdout);
	int ncase = 0;
	cin >> T;
	while(T--) {
		ncase++;
		cin >> n;
		while(judge(n) == 0)
			n--;
		printf("Case #%d: %d\n",ncase,n);
	}
	return 0;
}