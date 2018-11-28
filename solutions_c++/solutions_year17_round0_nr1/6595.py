#include <cstdio>

using namespace std;


int main() {
	FILE *in = fopen("input.txt", "r");
	FILE *out = fopen("output.txt", "w");
	int t,n;
	char st[1005];
	fscanf(in,"%d", &t);
	for(int i=0; i<t; i++) {
		fscanf(in,"%s",st);
		int count = 0;
		fscanf(in,"%d", &n);
		int j;
		for(j=0; st[j+n]!='\0'; j++) {
			if(st[j] == '-') {
				count++;
				for(int k=j; k<j+n; k++)
					if(st[k] == '+')
						st[k] = '-';
					else
						st[k] = '+';
			}
		}
		if(st[j] == '-') {
				count++;
				for(int k=j; k<j+n; k++)
					if(st[k] == '+')
						st[k] = '-';
					else
						st[k] = '+';
			}
		bool flag = true;
		for(; st[j]!='\0' && flag; j++) {
			if(st[j] == '-')
				flag = false;
		}
		fprintf(out,"Case #%d: ",i+1);
		if(!flag)
			fprintf(out,"IMPOSSIBLE\n");
		else
			fprintf(out,"%d\n",count);
	}
	return 0;
}
