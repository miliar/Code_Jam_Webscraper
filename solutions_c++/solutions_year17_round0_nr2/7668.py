/*
 * TidyNumbers2017.cpp
 *
 *  Created on: Apr 8, 2017
 *      Author: Mostafa
 */

#include<bits/stdc++.h>

using namespace std;

int main() {
	freopen("B-large.in", "rt", stdin);
	freopen("outputLarge.txt", "wt", stdout);
	int t, tc = 1;
	scanf("%d", &t);
	while (t--) {
		string n;
		cin >> n;
		int sz = n.size(),ind=0;
		while(n[ind+1]>=n[ind])
			ind++;
		if(ind!=sz-1)
			n[ind]-=1;
		for(int i=ind+1;i<sz;i++)
			n[i]='9';
		for (int i = sz - 1; i > 0; i--) {
			if (n[i] < n[i - 1]) {
				n[i] = '9';
				n[i - 1] -= 1;
			}
			if (n[i] == '0') {
				n[i] = '9';
			}
		}
		stringstream ss;
		ss << n;
		long long res;
		ss >> res;
		printf("Case #%d: %lld\n",tc++,res);
	}
	return 0;
}
