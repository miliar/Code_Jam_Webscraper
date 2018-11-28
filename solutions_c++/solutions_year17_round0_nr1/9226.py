#include <stdio.h>
#include <string.h>
int pancake(char s[], int k);
int main(void){
	int t=0, k=0, j=0;
	char s[1500];
	int result=0;
	FILE *in = fopen("A-large.in", "r");
	FILE *out = fopen("result.txt", "w");

	if(in==NULL || out==NULL){
		printf("error\n");
		fclose(in);
		fclose(out);
	}
	
	fscanf(in, "%d", &t);
	for(int i=0; i<t; i++){
		fscanf(in, "%s", s);
		fscanf(in, "%d", &k);
		result = pancake(s, k);
		if(result==-1)
			fprintf(out, "Case #%d: %s\n", i+1, "IMPOSSIBLE");
		else
			fprintf(out, "Case #%d: %d\n", i+1, result);

		for(int x=0; x<strlen(s); x++){
			s[x]='\0';
		}
	}
	
	fclose(in);
	fclose(out);


}
int pancake(char s[], int k){
	int n = strlen(s);
	int index=0;
	int tf=1;
	for(int i=0; i<=(n-k); i++){
		if(s[i]=='-'){
			index++;
			for(int j=i; j<i+k; j++){
				if(s[j]=='-')
					s[j]='+';
				else if(s[j]=='+')
					s[j]='-';
			}
		}//if
		
	}
	for(int i=0; i<n; i++){
		if(s[i]=='-')
			tf=0;
	}
	if(!tf) return -1;
	else return index;
}