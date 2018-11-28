#include <bits/stdc++.h>
using namespace std;

int pwr(int a, int b){
	if(b == 0) return 1;
	else return a*pwr(a, b-1);
}

int t, d, res;
char num[4];

int main(){

	scanf("%d" , &t);
	for(int p = 1 ; p <= t ; p++){
		res = 0;
		scanf("%d" , &d);
		for(int i = 0 ; i < 4 ; i++){
			num[i] = '0';
		}
		if(d/10 == 0) res = d;
		else{
			for(int i = 0 ; i < 4 ; i++){
				num[i] = '0' + d%10;
				d = d - (d%10);
				d = d/10;
			}
			while((num[0] < num[1]) or (num[1] < num[2]) or (num[2] < num[3])){
				if(num[0] != '0') num[0]--;
				else{
					num[0] = '9';
					if(num[1] != '0') num[1]--;
					else{
						num[1] = '9';
						if(num[2] != '0') num[2]--;
						else{
							num[2] = '9';
							num[3]--;
						}
					}
				}
			}
			for(int h = 0 ; h < 4 ; h++){
				res = res + (num[h] - '0')*pwr(10, h);
			}
		}
		printf("Case #%d: %d\n", p, res);
	}

	return 0;
}