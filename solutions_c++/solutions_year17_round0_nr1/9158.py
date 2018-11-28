#include <bits/stdc++.h>
using namespace std;

int t, i, k, res, s, v;
char pan[1010];
char c;

int main(){

	scanf("%d\n" , &t);

	for(int p = 0 ; p < t ; p++){
		i = res = v = 0;
		//printf("%d case\n", p);
		while(true){
			scanf("%c" , &c);
			//printf("%c\n", c);
			if(c == ' '){
				s = i;
				break;
			}
			else pan[i] = c;
			i++;
			//printf("%d\n", i);
		}
		scanf("%d" , &k);
		scanf("%c" , &c);
		//printf("%d\n", k);
		for(int i = 0 ; i <= s - k ; i++){
			if(pan[i] == '-'){
				res++;
				for(int o = 0 ; o < k ; o++){
					if(pan[i+o] == '+') pan[i+o] = '-';
					else pan[i+o] = '+';
				}
			}
		}
		for(int i = (s - k) ; i < s ; i++){
			if(pan[i] == '-') {
				v = 1;
				break;
			}
		}
		if(v == 0) printf("Case #%d: %d\n", p+1 , res);
		else printf("Case #%d: IMPOSSIBLE\n", p+1);
	}

	return 0;

}