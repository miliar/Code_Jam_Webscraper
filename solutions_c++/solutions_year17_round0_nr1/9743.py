#include <bits/stdc++.h>
using namespace std;

string s;
int k;

bool smjesko() {
	for (int ii = 0; ii < s.size(); ii++) 
		if (s[ii] == '-')
			return false;
	return true;
}
		
int main() {
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	
	int tt;
	scanf("%d", &tt);
	for (int qq = 1; qq <= tt; qq++) {
    printf("Case #%d: ", qq);
		cin >> s;
		vector <string> bash;
		scanf ("%d", &k);
		int pom;
		int sol = 0;
		if(smjesko()) {
			cout << sol << endl;
			continue;
		}
		pom = 0;
		petlja:
		for (; pom<s.size() && s[pom]=='+' && pom + k < s.size(); pom++)
			;
		for (int uu = pom; uu < s.size() && uu < pom + k; uu++)
			if(s[uu] == '-')
				s[uu] = '+';
			else
				s[uu] = '-';
		if(!smjesko()) {
			sol ++;
			if (find(bash.begin(), bash.end(), s) != bash.end()) {
				cout << "IMPOSSIBLE" << endl;
				continue;
			}	
			else
				bash.push_back(s);
			goto petlja;
		}
		else cout << sol+1 << endl;
		fprintf(stderr, "test case %d solved\n", qq);
    fflush(stderr);
	}
	return 0;
}
