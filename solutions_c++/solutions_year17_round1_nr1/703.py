#include<stdio.h>
#include<stdlib.h>
#include<algorithm>

main() {
	freopen("A-large.in", "r", stdin);
	freopen("outBigA.txt", "w", stdout);
	
	char a[35][35];
	int t, tc = 1;
	scanf("%d", &t);
	int r, c; 
	while(t--) {
		scanf("%d %d", &r, &c);
		for(int i = 0; i < r; i++) {
			scanf("%s", a[i]);
		}
		for(int i = 0; i < r; i++) {
			char cur = '?';
			for(int j = 0; j < c; j++) {
				if(a[i][j] != '?') {
					cur = a[i][j];
					break;
				}
			}
			
			if(cur != '?') {
				for(int j = 0; j < c; j++) { 
					if(a[i][j] == '?') {
						a[i][j] = cur;
					} else {
						cur = a[i][j];
					}
				}
			}
		}
		
		int row;
		for(int i = 0; i < r; i++) {
			int j;
			for(j = 0; j < c; j++) {
				if(a[i][j] != '?') break;
			}
			if(j < c) {
				row = i;
				break;
			}
		}
		//printf("%d\n", row);
		
		for(int i = 0; i < r; i++) {
			bool nothing = true;
			for(int j = 0; j < c; j++) {
				if(a[i][j] != '?') { 
					nothing = false; 
					break; 
				}
			}
			if(nothing) {
				for(int j = 0; j < c; j++) {
					a[i][j] = a[row][j];
				}
			} else {
				row = i;
			}
		}
		
		printf("Case #%d:\n", tc++);
		for(int i = 0; i < r; i++) {
			printf("%s\n", a[i]);
		}
	}
}

