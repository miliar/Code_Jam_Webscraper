#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<vector>
#include<queue>
#include<map>
#include<stdio.h>
#include<string.h>
#include<string>
#include<set>
#include<stdlib.h>
#include<bitset>
using namespace std;
#define ll long long
vector<int>v;
int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif // !ONLINE_JUDGE
	int t;
	scanf("%d", &t);
	long long int n;
	for(int i=1;i<=t;++i) {
		scanf("%lld", &n);
		while (n > 0) {
			v.push_back(n % 10);
			n /= 10;
		}
		reverse(v.begin(), v.end());
		for (int k = 0; k < 30; ++k) {
			bool change = false;
			for (int j = 0; j < v.size() - 1; ++j) {
				if (v[j] > v[j + 1]) {
					v[j]--;
					for (int d = j + 1; d < v.size(); ++d)
						v[d] = 9;
					change = true;
					break;
				}
			}
			if (!change)
				break;
		}
		printf("Case #%d: ",i);
		bool start = false;
		for (int i = 0; i < v.size(); ++i) {
			if (v[i] > 0)
				start = true;
			if (start)
				printf("%d", v[i]);
		}
		printf("\n");
		v.clear();
	}
}