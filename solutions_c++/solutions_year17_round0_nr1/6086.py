#include <stdio.h>
#include <vector>
#include <string.h>
using namespace std;
int main() {
	int t;
	int tt = 0;
	FILE* fp;
	FILE* fp2;
	fp2 = fopen("A-large.in", "r");
	fp = fopen("output.out", "w");
	fscanf(fp2,"%d", &t);
	while (t--) {
		tt++;
		int n;
		char arr[1001];
		vector<int>v;
		vector<int>ch;
		int num = 0, cnt = 0;
		fscanf(fp2,"%s", arr);
		fscanf(fp2,"%d", &n);
		int len = strlen(arr);
		v.resize(len + 1);
		ch.resize(len + 1);
		for (int i = 0; i < len; i++) {
			if (arr[i] == '-')
				v[i] = 0;
			else
				v[i] = 1;
		}
		for (int i = 0; i < len - n + 1; i++) {
			if (cnt % 2)
				v[i] = (v[i] + 1) % 2;
			if (ch[i])
				cnt--;
			if (!v[i]) {
				cnt++;
				num++;
				ch[i + n - 1] = 1;
				v[i] = (v[i] + 1) % 2;
			}
		}
		for (int i = len - n + 1; i < len; i++) {
			if (cnt % 2)
				v[i] = (v[i] + 1) % 2;
			if (ch[i])
				cnt--;
		}
		int check = 0;
		for (int i = 0; i < len; i++) {
			if (!v[i]) {
				check = 1;
				break;
			}
		}
		if (!check)
			fprintf(fp, "Case #%d: %d\n", tt, num);
		else
			fprintf(fp, "Case #%d: IMPOSSIBLE\n", tt);
	}
}