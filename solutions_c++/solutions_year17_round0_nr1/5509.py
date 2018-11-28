#include <stdio.h>
#include <cstring>
#include <algorithm>

using namespace std;

int main()
{
	//freopen("input.txt", "r", stdin);

	char s[1001];
	int k;
	int t;
	scanf("%d", &t);

	for(int id=1; id<=t; id++){
		scanf("%s", s);
		scanf("%d", &k);
		int len = 0;
		for(int i=0; s[i]; i++){
			len = i+1;
		}
		int count = 0;
		for(int i=0; i<=len-k; i++){
			if(s[i]=='-'){
				for(int j=i; j<i+k; j++){
					if(s[j]=='-') s[j]='+';
					else s[j]='-';
				}
				count++;
			}
		}
		for(int i=len-k; i<len; i++){
			if(s[i]=='-') count = -1;
		}
		printf("Case #%d: ", id);
		if(count==-1){
			printf("IMPOSSIBLE\n");
		}
		else{
			printf("%d\n", count);
		}
	}

    return 0;
}
