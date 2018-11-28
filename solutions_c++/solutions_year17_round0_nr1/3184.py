#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <string>
#include <map>

using namespace std;

int main(){
	int n, k;
	char f[1001];
	FILE *fin = fopen("a.in","r");
	FILE *fout = fopen("a.res","w");
	fscanf(fin, "%d", &n);
	for(int loop=1;loop<=n;loop++){
		fscanf(fin, "%s %d", f, &k);
		fprintf(fout, "Case #%d: ", loop);
		int len = strlen(f);
		int ans = 0;
		for(int i=0;i<len;i++)
			if(f[i] == '-') f[i] = 0; else f[i]=1;
		for(int i=0;i+k<=len;i++){
			if(f[i] == 0){
				ans++;
				for(int j=i; j<i+k; j++) f[j] = !f[j];
			}
		}
		bool ok = true;
		//for(int i=0;i<len;i++) printf("%d", f[i]);
		for(int i=0;i<len;i++)
			if(f[i] == 0) {
				ok = false;
				break;
			}
		if(ok) fprintf(fout, "%d\n", ans);
		else fprintf(fout, "IMPOSSIBLE\n");
	}
	fclose(fin);
	fclose(fout);
	return 0;
}
