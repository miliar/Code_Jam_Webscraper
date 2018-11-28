#include <stdio.h>
#include <string.h>
#define MAX 3
void save_arr(int s[], int given){
	int tmp=given;
	for(int i=0; i<=MAX; i++){
		s[i] = tmp%10;
		tmp = tmp/10;
	}
}

int cmp_arr(int s[]){
	int i=0;
	int result=0;
	while(i<MAX){
		if(s[i]<s[i+1])
		{
			result = -1;
			break;
		}
		else result = 1;
		
		i++;
	}
	return result;
}

int main(void){

	int n=0, given=0;
	int s[20];
	

	FILE *in = fopen("B-small-attempt0.in", "r");
	FILE *out = fopen("result.txt", "w");

	fscanf(in, "%d", &n);
	for(int i=0; i<n; i++){
		fscanf(in, "%d", &given);
		
		save_arr(s, given);
		while(cmp_arr(s)==-1){
			for(int x=0; x<20; x++){
			s[x]='\0';
		}
			save_arr(s, --given);
		}

		fprintf(out, "Case #%d: %d\n", i+1, given);

		
	}
	fclose(in);
	fclose(out);
}