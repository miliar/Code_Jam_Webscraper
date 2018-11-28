#include <bits/stdc++.h>
using namespace std;

int main() {
	int t, k, n, i, j, count;
	string a;
	cin >> t;
	for(int z=1;z<=t;z++) {
		cin >> a >> k;
		n = a.length();
		count = 0;
		for(i=0;i<=n-k;i++) {
			if(a[i] == '-') {
				count++;
				for(j=i;j<i+k;j++) {
					if(a[j] == '-')
						a[j] = '+';
					else
						a[j] = '-';
				}
			}
		}
		bool flag = true;
		for(i=n-k+1;i<n;i++) {
			if(a[i] == '-') {
				cout << "Case #" << z << ": " << "IMPOSSIBLE" << endl;
				flag = false;
				break;
			}
		}
		if(flag)
			cout << "Case #" << z << ": " << count << endl;
	}
	return 0;
}