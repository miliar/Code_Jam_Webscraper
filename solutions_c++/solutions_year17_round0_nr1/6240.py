#include <bits/stdc++.h>
char s[10009];
int k;
int len;
int findnext(int p){
	int i,j;
	for(i = p ; i < len ; i++){
		if(s[i] == '-'){
			return i;
		}
	}
	return -1;
}
int main(){
	int t,t1 = 1;
	scanf("%d",&t);
	int i,j;
	while(t--){
		scanf("%s %d",s,&k);
		len = strlen(s);
		int st = 0,count = 0;
		while(1){
			//printf("%d %d\n",st,len);
			st = findnext(0);
			if(st == -1 || (len-st) < k ){
				break;
			}  
			for(i = st ; i <= st+k-1 ; i++){
				if(s[i] == '-'){
					s[i] = '+';
				}
				else{
					s[i] = '-';
				}
			}
			count++;
		}
		if(findnext(0) == -1){
			printf("Case #%d: %d\n",t1,count);
		}
		else{
			printf("Case #%d: IMPOSSIBLE\n",t1);
		}
		t1++;
	}
}