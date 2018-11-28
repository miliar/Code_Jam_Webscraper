#include <cstdio>
#include <cstring>
using namespace std;

char a[21];
char b[21];

bool fill(long long int curr1, long long curr2, long long int prev, int ind) {
	if(!a[ind]) return true;
	for(long long int j=9;j >= prev; j--) {
		long long val2 = curr2 * 10 + j;
		long long val1 = curr1 * 10 +  a[ind] - '0';
		if(val2 <= val1) {
			b[ind] = j + '0';
			if(fill(val1, val2 , j, ind + 1 ))
				return true;
		}
	}
	return false;
}

int main() {
	int i,j,t,Case = 1;
	long long int n;
	scanf("%d",&t);
	while(t--) {
		scanf("%s",a);
		strcpy(b,a);
		fill(0,0,0,0);	
		printf("Case #%d: ", Case++ );
		for(i=0;b[i];i++) if(b[i]!='0') break;
		for(;b[i];i++) printf("%c",b[i]);
		printf("\n");
	}
	return 0;
}
