#include <stdio.h>
#include <vector>
#include <algorithm>
#include <iostream>
#include <cmath>

using namespace std;

bool shouldFlip(char c, int flips) {
	if (c=='-' && flips%2==0) {
		return true;
	}
	if (c=='+' && flips%2==1) {
		return true;
	}
	
	return false;
}

int main(int argc, char **argv)
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	
	int T=0;
	int k;
	string s;
	vector<int> flips;
	int activeFlip = 0;
	bool exit = false;
	
	cin >> T;
	
	for (int t=1;t<=T;t++) {
		exit = false;
		cin >> s >> k;
		
		for (int i=0;i<s.length();i++) {
			if (shouldFlip(s[i],flips.size()-activeFlip)) {
				flips.push_back(i);
				if (i+k-1>=s.size()) {
					printf("Case #%d: IMPOSSIBLE\n",t);
					flips.clear();
					activeFlip = 0;
					exit = true;
					break;
				}
			}
			for (int j=activeFlip;j<flips.size()&&flips[j]+k-1<=i;j++) {
				activeFlip++;
			}
		}
		
		if (!exit) {
			printf("Case #%d: %d\n",t,flips.size());
			flips.clear();
			activeFlip = 0;
		}
	}
}