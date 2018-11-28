#include <bits/stdc++.h>
using namespace std;

int main() {
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	
	int tt;
	scanf("%d", &tt);
	for (int qq = 1; qq <= tt; qq++) {
    printf("Case #%d: ", qq);
		string n;
		cin >> n;
		int i;
		for (i = 0; i < n.size()-1 && n[i] <= n[i+1]; i++)
			;
		if (i == n.size()-1) {
			cout << n << endl;
			continue;
		}
		for (i = 0; i < n.size()-1 && n[i] < n[i+1]; i++)
			;
		if(i == n.size()-1) {
			cout << n << endl;
			continue;
		}
		n[i] -= 1;
		for (int j=i+1; j < n.size(); j++)
			n[j] = '9';
		string rez;
		int pom  = 0;
		while(n[pom] == '0')
			pom++;
		for (int j=pom; j<n.size(); j++)
			rez += n[j];
		cout << rez << endl;
		
		fprintf(stderr, "test case %d solved\n", qq);
    fflush(stderr);
	}
	return 0;
}

