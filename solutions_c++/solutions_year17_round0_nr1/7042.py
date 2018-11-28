#include <iostream>
#include <cstdio>
using namespace std;

int count_segment(int start, int k, string pancake) {
	int end = start + k - 1;
	int count = 0;
	for (int i=start; i<=end; i++) {
		if (pancake[i]=='+') {
			count++;
		}
	}
	return count;
}

void flip(int start, int k, string &pancake) {
	int end = start + k - 1;
	for (int i=start; i<=end; i++) {
		if (pancake[i]=='+') {
			pancake[i] = '-';
		}
		else if (pancake[i]=='-') {
			pancake[i] = '+';
		}
	}
}

bool is_all_happy(string str) {
	bool not_happy = false;
	for (int j=0; j<str.length() && !not_happy; j++) {
		if (str[j]!='+')
			not_happy = true;
	}
	return !not_happy;
}

int main() {
	int t;
	scanf("%d",&t);
	string str;
	int k;
	for (int i=0; i<t; i++) {
		cin >> str >> k;
		if (!is_all_happy(str)) {
			bool breaked = false;
			int flip_count = 0;
			for (int j=0; j<=str.length()-k && !breaked; j++) {
				if (str[j]=='-') {
					flip(j, k, str);
					flip_count ++;
				}
			}
			if (is_all_happy(str)) {
				printf("Case #%d: %d\n", i+1, flip_count);
			}
			else {
				printf("Case #%d: IMPOSSIBLE\n", i+1);
			}
		}
		else {
			printf("Case #%d: 0\n", i+1);
		}
	}
	return 0;
}