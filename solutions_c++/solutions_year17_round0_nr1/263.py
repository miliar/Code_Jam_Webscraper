#include <stdio.h>
#include <string.h>

char arr[1010];
int sz;

void Flip(int id){
	for(int i=id; i<id+sz; i++){
		if(arr[i] == '-') arr[i] = '+';
		else arr[i] = '-';
	}
}

int main(){
	int jcase;
	
	freopen("A-large.in", "r", stdin);
	//freopen("A-large.out", "w", stdout);
	
	scanf("%d", &jcase);
	for(int icase=0; icase<jcase; icase++){
		scanf("%s %d", arr, &sz);
		int len = strlen(arr);
		int ans = 0;
		
		for(int i=0; i<len-sz+1; i++){
			if(arr[i] == '-'){ 
				Flip(i);
				ans++;
			}
		}
		
		bool isGood = true;
		for(int i=len-sz+1; i<len; i++){
			if(arr[i] == '-'){
				isGood = false;
				break;
			}
		}
		
		if(isGood) printf("Case #%d: %d\n", icase+1, ans);
		else printf("Case #%d: IMPOSSIBLE\n", icase+1);
	}
	
	return 0;
}
