#include <bits/stdc++.h>

using namespace std;

char s[1005];

int main(){

	int t, r, len, flips, j;
	bool possible;

	scanf("%d",&t);

	for(int i=0; i<t; i++){
		scanf("%s %d",s,&r);

		flips = j = 0;
		possible = true;
		len = strlen(s);
		while(j<len){
			if(s[j] == '-'){
				if(j+r > len){
					possible = false;
					break;
				}
				flips++;
				for(int k=j; k<j+r; k++){
					if(s[k] == '-')
						s[k] = '+';
					else
						s[k] = '-';
				}
			} 
			j++;
				
		}

		printf("Case #%d: ",i+1);
		
		if(possible)
			printf("%d\n",flips);
		else
			printf("IMPOSSIBLE\n");
	}
	


	return 0;
}
