#include <bits/stdc++.h>
using namespace std;

int t;
char n[1234];

int main()
{
scanf("%d\n", &t);
for(int q=1; q<=t; q++) {
	scanf("%s\n", n+1);
	n[0]='0';
	int last=0;
	for(int i=1; n[i]; i++) {
		if(n[i]>n[i-1]) last=i;
		else if(n[i]<n[i-1]) {
			n[last]--;
			for(int j=last+1; n[j]; j++) n[j]='9';
			break;
		}
	}
	int from=0;
	while(n[from]=='0') from++;
	printf("Case #%d: ", q);
	for(int i=from; n[i]; i++) printf("%c", n[i]);
	printf("\n");
}

	return 0;
}
