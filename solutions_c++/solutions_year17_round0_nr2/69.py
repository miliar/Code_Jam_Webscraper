#include<stdio.h>
#include<string.h>

char st[44]; int len;

void test(int tn){
	scanf("\n%s", st); len=strlen(st);
	printf("Case #%d: ", tn);

	for(int i=0; i<len; i++){
		bool ok=1;
		for(int j=i; j<len; j++){
			if(st[i] > st[j]){ ok=0; break; }
			if(st[i] < st[j]) break;
		}
		if(!ok){
			if(st[i] != '1')putchar(st[i]-1);
			for(int j=i+1; j<len; j++)printf("9");
			break;
		}
		putchar(st[i]);
	}
	puts("");
}

int main(){
	int t;
	freopen("B-large.in","r",stdin); freopen("output.txt","w",stdout);
	scanf("%d", &t);
	for(int i=1; i<=t; i++)test(i);
	return 0;
}
