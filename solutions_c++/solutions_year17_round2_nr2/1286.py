#include <stdio.h>
#include <bits/stdc++.h>

using namespace std;

int s[1010];
int f;

int main () {
	
	int t;
	
	scanf("%d", &t);
	
	for (int i = 0; i < t; i++) {
		int n, r, o, y, g, b, v;
		int aa, bb, cc;
		
		scanf("%d %d %d %d %d %d %d", &n, &r, &o, &y, &g, &b, &v);
		f = 0;
		
		printf("Case #%d: ", i + 1);
		
		if (g) {
			aa = r - (g + 1);
		} else {
			aa = r;
		}
		if (o) {
			bb = b - (o + 1);
		} else {
			bb = b;
		}
		if (v) {
			cc = y - (v + 1);
		} else {
			cc = y;
		}
		
		if (r == g && !v && !y && !o && !b) {
			for (int j = 0; j < n; j++) {
				printf("R");
				j++;
				printf("G");
			}
			printf("\n");
			continue;
		}
		if (!r && !g && v == y && !o && !b) {
			for (int j = 0; j < n; j++) {
				printf("V");
				j++;
				printf("Y");
			}
			printf("\n");
			continue;
		}
		if (!r && !g && !v && !y && o == b) {
			for (int j = 0; j < n; j++) {
				printf("O");
				j++;
				printf("B");
			}
			printf("\n");
			continue;
		}
		
		if (aa < 0 || bb < 0 || cc < 0) {
			printf("IMPOSSIBLE\n");
			continue;
		}
		int w;
		if (aa > bb) {
			if (aa > cc) {
				w = 0;
			} else {
				w = 2;
			}
		} else {
			if (bb > cc) {
				w = 1;
			} else {
				w = 2;
			}
		}
		
		if (g) {
			s[f++] = 'R';
			for (int j = 0; j < g; j++) {
				s[f++] = 'G';
				s[f++] = 'R';
			}
		}
		if (w == 2) {
			s[f++] = 'Y';
			cc--;
		}
		if (o) {
			s[f++] = 'B';
			for (int j = 0; j < o; j++) {
				s[f++] = 'O';
				s[f++] = 'B';
			}
		}
		if (w == 0) {
			s[f++] = 'R';
			aa--;
		}
		if (v) {
			s[f++] = 'Y';
			for (int j = 0; j < v; j++) {
				s[f++] = 'V';
				s[f++] = 'Y';
			}
		}
		if (w == 1) {
			s[f++] = 'B';
			bb--;
		}
		char esp = s[0];
		char last = s[f-1];
		
		while (aa+bb+cc) {
			
// 			printf("%d %d %d %c %c\n", aa, bb, cc, esp, last);
			
			if (last == 'B') {
				
				if (aa == 0 && cc == 0) {
					s[f++] = esp;
					break;
				}
				
				if (aa == cc) {
					if (esp == 'R') {
						s[f++] = 'R';
						aa--;
					} else {
						s[f++] = 'Y';
						cc--;
					}
				} else {
					if (aa > cc) {
						s[f++] = 'R';
						aa--;
					} else {
						s[f++] = 'Y';
						cc--;
					}
				}
			}
			if (last == 'R') {
				
				if (bb == 0 && cc == 0) {
					s[f++] = esp;
					break;
				}
				
				if (bb == cc) {
					if (esp == 'B') {
						s[f++] = 'B';
						bb--;
					} else {
						s[f++] = 'Y';
						cc--;
					}
				} else {
					if (bb > cc) {
						s[f++] = 'B';
						bb--;
					} else {
						s[f++] = 'Y';
						cc--;
					}
				}
			}
			if (last == 'Y') {
				
				if (aa == 0 && bb == 0) {
					s[f++] = esp;
					break;
				}
				
				if (aa == bb) {
					if (esp == 'R') {
						s[f++] = 'R';
						aa--;
					} else {
						s[f++] = 'B';
						bb--;
					}
				} else {
					if (aa > bb) {
						s[f++] = 'R';
						aa--;
					} else {
						s[f++] = 'B';
						bb--;
					}
				}
			}
			last = s[f-1];
		}
		if (s[0] == s[f-1]) {
			printf("IMPOSSIBLE\n");
		} else {
			for (int j = 0; j < n; j++) {
				printf("%c", s[j]);
			}
			printf("\n");
		}
	}
	
	return 0;
	
}
