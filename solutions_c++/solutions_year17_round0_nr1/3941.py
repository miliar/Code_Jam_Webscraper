#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#define pb push_back

using namespace std;
typedef long long ll;

int main() {
	int t,k;
	string line;
	scanf("%d",&t);
	for (int ctr=1;ctr<=t;ctr++) {
		cin >> line;
		cin >> k;
		ll acc = 0;
		bool toggle = true;
		for (int i=0;i<line.size();i++) {
			if (line[i]=='-') {
				if (i+k-1<line.size()) {
					for (int j=i;j<=i+k-1;j++) {
						if (line[j]=='-') line[j] = '+';
						else if (line[j]=='+') line[j] = '-';
					}
					acc++;
				}
				else {
					toggle = false;
					break;
				}
			}
			else continue;
		}
		if (toggle) {
			printf("Case #%d: %lld\n",ctr,acc);
		}
		else printf("Case #%d: IMPOSSIBLE\n",ctr);
	}
	return 0;
}