#include <iostream>
#include <utility>
#include <limits.h>
#include <fstream>
#include <string>
#include <string.h>
#include <queue>
#include <stdio.h>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <stack>
#include <cmath>
#include <functional>

using namespace std;
char inn[33];
int len;
int erasezero() {
	int ret = 0;
	for (int i = 0; i < len; i++) {
		if (inn[i] == '0') ret = i + 1;
		else break;
	}
	return ret;
}

int main()
{
	int T;
	scanf("%d", &T);
	
	for (int t = 1; t <= T; t++)
	{
		scanf("%s", inn);
		len = strlen(inn);
		int last = 0;
		for (int i = 0; i < len; i++) {
			if (inn[i] > inn[last]) last = i;
			else if (inn[i] < inn[last]) {
				inn[last]--;
				last++;
				for (int j = last; j < len; j++) {
					inn[j] = '9';
				}
				break;
			}
		}
		int ei = erasezero();
		printf("Case #%d: %s\n", t, &inn[ei]);
	}
	return 0;
}