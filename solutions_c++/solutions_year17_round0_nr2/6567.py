#include <cstdio>
#include <cstring>

using namespace std;


int main() {
	FILE *in = fopen("input.txt", "r");
	FILE *out = fopen("output.txt", "w");
	int t;
	char st[20];
	fscanf(in,"%d", &t);
	for(int i=0; i<t; i++) {
		fscanf(in,"%s",st);
		int l = strlen(st);
		int p = l;
		for(int i=l-2; i>=0; i--) {
			if(st[i]>st[i+1]) {
				st[i]--;
				p = i+1;
			}
		}
		fprintf(out, "Case #%d: ", i+1);
		for(int i=0; i<l; i++) {
			if(i>=p)
				fprintf(out, "9");
			else if(st[i]>'0' || i>0)
				fprintf(out, "%c", st[i]);
		}
		fprintf(out, "\n");
	}
	return 0;
}
