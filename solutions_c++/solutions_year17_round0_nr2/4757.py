#include <bits/stdc++.h>
using namespace std;

string s, t;
int k, n;

bool dq(int k, bool ok) {
	if (k == n) 
		return true;
	char gh;
	if (ok) 
		gh = '9';
	else 
		gh = s[k];
	for(char ch = gh; ch >= '0'; ch--) {
		t[k] = ch;
		if (k==0 || t[k-1] <= t[k])
			if (dq(k+1, ok || t[k] < s[k]))
				return true;
	}
	return false;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);;
	int test;
	scanf("%d\n", &test);
	for(int dem = 1; dem <= test; dem++) {
		getline(cin, s);
		n = s.length();
		t = "";
		for(int i=0; i<n; i++) 
			t = t + "@";
		dq(0, false);
		while (t.length()>1 && t[0] == '0')
			t.erase(t.begin());
		printf("Case #%d: ", dem);
		cout << t << endl;
	}
	fclose(stdin);
	fclose(stdout);
}