#include <bits/stdc++.h>


using namespace std;
#define FOR(i, n) for (int i=0; i<(n); i++)
#define ll long long

void vyres(void)
{
	char buf[20];
	scanf("%s", buf);
	int n = strlen(buf);
	int last = -1;
	char c = '\0';
	int fl = n;
	buf[n] = '9' + 1;
	FOR(i, n){
		if (buf[i] != c)
			last = i, c = buf[i];

		if (buf[i] > buf[i + 1]){
			fl = last;
			break;
		}
	}

	assert(fl >= 0);
	buf[n] = '\0';
	if (fl < n)
		buf[fl]--;

	for (int i=fl + 1; i<n; i++)
		buf[i] = '9';
	
	char *b = buf;
	if (*b == '0')
		b++;

	printf("%s\n", b);
}

int main(void)
{
	int t;
	scanf("%d", &t);
	FOR(i, t){
		printf("Case #%d: ", i + 1);
		vyres();
	}
}
