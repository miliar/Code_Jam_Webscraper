#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <stdio.h>
using namespace std;  // since cin and cout are both in namespace std, this saves some text
#define min(a,b) a>b ? b:a
#define INF 987654321
char n[20];
int l;
int k;
int minus_(int i){
	int ret = 0;
	if (i == k){
		if (n[i] == '1'){
			n[i] -= 1;
			return 1;
		}
		else{
			n[i] -= 1;
			return 0;
		}
	}
	else{
		if (n[i] == '0'){
			n[i] = '9';
			ret = minus_(i - 1);
		}
		else{
			n[i] -= 1;
		}
	}
	return ret;
}
void main() {
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	for (int test = 1; test <= t; ++test) {
		scanf("%s", &n);
		//printf("%s ", n);
		l = strlen(n);
		k = 0;
		for (int i = l - 1; i >= k; --i)
		{
			int next = n[i - 1] - '0';
			int now = n[i] - '0';

			if (next > now)
			{	
				for (int j = i; j < l; ++j){
					n[j] = '9';
				}
				k += minus_(i - 1);
				
			}
		}
		cout << "Case #" << test << ": ";
		for (int i = k; i < l; ++i){
				printf("%c", n[i]);
		}	
		printf("\n");

		// cout knows that n + m and n * m are ints, and prints them accordingly.
		// It also knows "Case #", ": ", and " " are strings and that endl ends the line.
	}
}