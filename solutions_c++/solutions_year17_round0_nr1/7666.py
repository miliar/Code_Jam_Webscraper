/*
 * OversizedPancakeFlipper2017.cpp
 *
 *  Created on: Apr 8, 2017
 *      Author: Mostafa
 */

#include<bits/stdc++.h>

using namespace std;

int main() {
	freopen("A-large.in", "rt", stdin);
	freopen("outputLarge.txt", "wt", stdout);
	ios::sync_with_stdio(false);
	int t, tc = 1;
	cin >> t;
	while (t--) {
		string s;
		int k;
		cin >> s >> k;
		int sz = s.size(), res = 0;
		int frq[1010] = { 0 };
		for (int i = 0; i < sz - k + 1; i++) {
			frq[i+1]+=frq[i];
			if(((frq[i+1]%2==0) && s[i]=='-') || ((frq[i+1]%2==1) && s[i]=='+')) {
				res++;
				frq[i+1]++;
				frq[i+1+k]-=1;
			}
		}
		for(int i=sz-k+2;i<=sz;i++)
			frq[i]+=frq[i-1];
		for(int i=0;i<sz;i++) {
			if((frq[i+1]%2==0 && s[i]=='-') || (frq[i+1]%2 && s[i]=='+')) {
				res=-1;
				break;
			}
		}
		printf("Case #%d: ",tc++);
		if(res==-1)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n",res);
	}

	return 0;
}
