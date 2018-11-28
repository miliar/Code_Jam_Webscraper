#include<stdio.h>
#include<string>
#include<stdlib.h>
using namespace std;
int T;
string s;
char z[20];
bool check(void);
int main(void) {
	FILE * fp = fopen("B-small-attempt1.in", "rb");
	//FILE * fp = fopen("text.txt", "r");
	FILE * fp2 = fopen("result.txt", "w");
	fscanf(fp, "%d", &T);
	fgetc(fp);
	for (int i = 0; i < T; i++) {
		long long num;
		fscanf(fp, "%lld", &num);
		fprintf(fp2, "Case #%d: ", i + 1);
		if (num < 10)
			fprintf(fp2, "%lld\n", num);
		else {
			while (1) {
				s = to_string(num);
				bool chk = check();
				if (!chk) {
					fprintf(fp2, "%lld\n", num);
					break;
				}
				else {
					num--;
				}
			}
		}
	}
	return 0;
}
bool check(){
	for (long long j = 0; j < s.size() - 1; j++) {
		if (s[j] > s[j + 1]) {
			return true;
		}
	}
	return false;
}