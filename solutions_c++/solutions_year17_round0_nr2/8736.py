#include <bits/stdc++.h>
using namespace std;

#define MAXN 1000

vector <int> tidy;

bool isTidy (int n) {
	string s = to_string(n); 

	int prev = s[0];
	bool flag = true;

	for (int i=1; i<s.length(); i++) {
		if (prev > s[i]) {
			flag = false;
			break;
		}
		prev = s[i];
	}

	return flag;
}

int main () {

	int t=0, n=0, i=0;

	for (i=1; i<=MAXN; i++) 
		if (isTidy(i))
			tidy.push_back(i);

	scanf("%d", &t);

	for(i=1; i<=t; i++) {
		scanf("%d", &n);
		int idx = lower_bound(tidy.begin(), tidy.end(), n) - tidy.begin();
		if (idx == tidy.size()) idx-=1;
		while (tidy[idx] > n) idx--;
		//printf("Case #%d: %d\n", i, tidy[idx]);
		cout << "Case " << (char)(35) << i << (char)(58) << " " << tidy[idx] << endl;
	}
	
	return 0;
}