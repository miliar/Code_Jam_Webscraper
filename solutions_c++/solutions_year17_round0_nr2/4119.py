#include <stdio.h>
#include <iostream>
#include <string.h>

int main(void) {

	int t;
	scanf("%d", &t);
	for( int cnt=0; cnt<t; cnt++ ) {

		char n[20];
		scanf("%s", n);
		int size = strlen(n);

		int flag = 0;	// to -1
		bool ill = false;
		for( int i=1; i<size; i++ ) {
			if( n[i] > n[i-1] )
				flag = i;
			else if( n[i] < n[i-1] ) {
				ill = true;
				break;
			}
			// n[i]==n[i-1] : flag remains
		}


		printf("Case #%d: ", cnt+1);

		if( !ill ) {
			printf("%s\n", n);
		}
		else {
			for( int i=0; i<flag; i++ )
				printf("%c", n[i]);
			if( flag != 0 || n[flag]!='1'  )
				printf("%c", n[flag]-1);
			for( int i=flag+1; i<size; i++)
				printf("9");
			printf("\n");
		}

	}

	return 0;
}


