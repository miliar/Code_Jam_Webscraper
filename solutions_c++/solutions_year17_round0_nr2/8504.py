#include<cstdio>
#include<cstring>
#include<cstdlib>
using namespace std;

int main(){
	FILE *f, *f2;
	f = fopen("a.txt", "w");
	f2 = fopen("a.in", "r");
	int t;
	fscanf(f2, "%d", &t);
	for(int i = 1; i <= t; i++){
		char str[32];
		unsigned long long ret = 0;
		fscanf(f2, "%s", str);
		int size = strlen(str);
		fprintf(f, "Case #%d: ", i);
		int cut = -1;
		for(int j = 0; j < size-1; j++){
			if(str[j] > str[j+1]){
				cut = j;
				str[j] -= 1;
				break;
			}
		}
		if(cut >= 0){
			for(int j = cut+1; j < size; j++) str[j] = '9';
			for(int j = cut; j > 0; j--){
				if(str[j] < str[j-1]){
					str[j-1] = str[j];
					str[j] = '9';
				}
			}
		}
		for(int j = 0; j < size; j++){
			if(j == 0 && str[j] == '0') continue;
			else fprintf(f, "%c", str[j]);
		}
		fprintf(f, "\n");
		printf("%s\n", str);

	}
	fclose(f);
	fclose(f2);
}
