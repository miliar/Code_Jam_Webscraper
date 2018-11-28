#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fstream>

using namespace std;

fstream file("num.txt");

int checktidy(char *ch, int k)
{
	char c;
	c = ch[k -1];
	if ((k - 1) == 0) return 1;
	for (int i = k - 2; i >= 0; i--) {
		if ( ch[i] > c) return 0;
		c = ch[i];
	}
	return 1;
}
int main()
{
	int t;
	char ch[20];
	long int n;
	cin >> t;
	int m = 1;
	while (m != (t + 1)) {
		cin >> n;
		cout << "Case #" << m << ": ";
		for (long int i = n; i >= 0; i--) {
			sprintf(ch, "%ld",i);
			if (checktidy(ch, strlen(ch))) {
				cout << i << endl;
				break;
			}

		}
		m++;	

	}
	return 0;
}
