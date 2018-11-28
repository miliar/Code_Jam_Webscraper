#include <stdio.h>

int N;
int c1, c12, c2, c23, c3, c13;
char arr[1010];
char tarr[1010];

void Fill(int o1, int o2, int o3, char ch1, char ch2, char ch3, int p1, int p2, int p3){
	//printf("Fill %d %d %d %c %c %c %d %d %d\n", o1, o2, o3, ch1, ch2, ch3, p1, p2, p3);
	o1 -= p1;
	o2 -= p2;
	o3 -= p3;
	N -= (p1+p2+p3)*2;
	
	int ct = 0;
	int prevct = -2;
	while(o1 > 0){
		if(arr[ct] == '.' && ct - prevct > 1){
			arr[ct] = ch1;
			o1--;
			prevct = ct;
		}
		ct++;
		if(ct == N){
			ct = 0;
			prevct -= N;
		}
	}
	
	while(o2 > 0){
		if(arr[ct] == '.' && ct - prevct > 1){
			arr[ct] = ch2;
			o2--;
			prevct = ct;
		}
		ct++;
		if(ct == N){
			ct = 0;
			prevct -= N;
		}
	}
	
	while(o3 > 0){
		if(arr[ct] == '.' && ct - prevct > 1){
			arr[ct] = ch3;
			o3--;
			prevct = ct;
		}
		ct++;
		if(ct == N){
			ct = 0;
			prevct -= N;
		}
	}
	
	//debug
	//for(int i=0; i<N; i++) printf("%c", arr[i]);
	//printf("\n");
	
	bool isR=false;
	bool isY=false;
	bool isB=false;
	ct = 0;
	for(int i=0; i<N; i++){
		tarr[ct] = arr[i];
		ct++;
		if(arr[i] == 'R' && !isR){
			while(c23 > 0){
				tarr[ct] = 'G';
				tarr[ct+1] = 'R';
				ct += 2;
				c23--;
			}
			isR = true;
		}
		if(arr[i] == 'Y' && !isY){
			while(c13 > 0){
				tarr[ct] = 'V';
				tarr[ct+1] = 'Y';
				ct += 2;
				c13--;
			}
			isY = true;
		}
		if(arr[i] == 'B' && !isB){
			while(c12 > 0){
				tarr[ct] = 'O';
				tarr[ct+1] = 'B';
				ct += 2;
				c12--;
			}
			isB = true;
		}
	}
	
	for(int i=0; i<ct; i++) printf("%c", tarr[i]);
	printf("\n");
}

void Alter(int num, char ch){
	char ot;
	if(ch == 'R') ot = 'G';
	else if(ch == 'Y') ot = 'V';
	else if(ch == 'B') ot = 'O';
	
	for(int i=0; i<num; i++) printf("%c%c", ch, ot);
	printf("\n");
}

int main(){
	int jcase;
	
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	
	scanf("%d", &jcase);
	for(int icase=0; icase<jcase; icase++){
		scanf("%d %d %d %d %d %d %d", &N, &c1, &c12, &c2, &c23, &c3, &c13);
		for(int i=0; i<N; i++) arr[i] = '.';
		bool isPossible = true;
		
		if(c1 < c23) isPossible = false;
		if(c2 < c13) isPossible = false;
		if(c3 < c12) isPossible = false;
		if((c1 == c23 && c1 != 0) && (c2+c3+c12+c13 > 0)) isPossible = false;
		if((c2 == c13 && c2 != 0) && (c1+c3+c12+c23 > 0)) isPossible = false;
		if((c3 == c12 && c3 != 0) && (c1+c2+c13+c23 > 0)) isPossible = false;
		if(c1-c23 + c2-c13 < c3-c12) isPossible = false;
		if(c1-c23 + c3-c12 < c2-c13) isPossible = false;
		if(c3-c12 + c2-c13 < c1-c23) isPossible = false;
		if(!isPossible){
			printf("Case #%d: IMPOSSIBLE\n", icase+1);
			continue;
		}
		
		printf("Case #%d: ", icase+1);
		if(c1 == c23 && c1 != 0) Alter(c1, 'R');
		else if(c2 == c13 && c2 != 0) Alter(c2, 'Y');
		else if(c3 == c12 && c3 != 0) Alter(c3, 'B');
		else{
			if(c1-c23 >= c2-c13 && c2-c13 >= c3-c12) Fill(c1, c2, c3, 'R', 'Y', 'B', c23, c13, c12);
			else if(c1-c23 >= c3-c12 && c3-c12 >= c2-c13) Fill(c1, c3, c2, 'R', 'B', 'Y', c23, c12, c13);
			else if(c2-c13 >= c1-c23 && c1-c23 >= c3-c12) Fill(c2, c1, c3, 'Y', 'R', 'B', c13, c23, c12);
			else if(c2-c13 >= c3-c12 && c3-c12 >= c1-c23) Fill(c2, c3, c1, 'Y', 'B', 'R', c13, c12, c23);
			else if(c3-c12 >= c1-c23 && c1-c23 >= c2-c13) Fill(c3, c1, c2, 'B', 'R', 'Y', c12, c23, c13);
			else if(c3-c12 >= c2-c13 && c2-c13 >= c1-c23) Fill(c3, c2, c1, 'B', 'Y', 'R', c12, c13, c23);
		}
	}
	return 0;
}
