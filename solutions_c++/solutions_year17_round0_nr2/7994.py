#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <queue>
#include <vector>
using namespace std;
typedef long long int lli;
typedef pair<lli, lli> ii;
const int MAXN = 10010, MAXL = 1000010;

char s[64];

bool ok();
void decrement();
int leadingZeroes();

int main() {
	// freopen("B-large.in", "r", stdin);
	// freopen("output-large.txt", "w", stdout); 

	int t;
	scanf("%d", &t);

	for(int test=1; test<=t; test++) {
		printf("Case #%d: ", test);

		scanf("%s", s);

		while(!ok()) {
			decrement();
		}

		printf("%s\n", s+leadingZeroes());
	}
}

bool ok() {
	for(int i=strlen(s)-2; i>=0; i--) {
		if(s[i] > s[i+1]) {
			return false;
		}
	}
	return true;
}

void decrement() {
	for(int i=strlen(s)-2; i>=0; i--) {
		if(s[i] > s[i+1]) {
			s[i]--;
			for(int j=i+1; j<strlen(s); j++) {
				s[j] = '9';
			}
			return;
		}
	}
}

int leadingZeroes() {
	for(int i=0; i<strlen(s); i++) {
		if(s[i] != '0') {
			return i;
		}
	}
	return 0;
}
