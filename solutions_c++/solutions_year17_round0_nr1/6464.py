#include <iostream>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	freopen("A-large.in", "r", stdin);
    freopen("large-output.out", "w", stdout);
	long t, k;
	string s;
	cin >> t;
	for (long is=1;is<=t;is++) {
		cout << "Case #" << is << ": ";
		cin >> s >> k;
		long ans = 0;
		long l = s.length();
		for (long i=0;i<l;i++) {
			if (s[i] == '-') {
				if (i+k <= l) {
					for (long j=i;j<i+k;j++) {
						s[j] = (s[j]=='+')?'-':'+';
					}
					ans++;
				}
				else {
					ans = -1;
					break;
				}
			}
		}
		if (ans==-1) cout << "IMPOSSIBLE"<< endl;
		else cout << ans << endl;
	}
	return 0;
}