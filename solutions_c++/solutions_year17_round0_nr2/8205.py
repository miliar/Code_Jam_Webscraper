#include<bits/stdc++.h>
using namespace std;

char num[20];

int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int t, ca = 0;
	scanf("%d",&t);
	while(t--){
		scanf("%s",num);
		int len = strlen(num);
		int i = 0, start = 0;
		while(i < len - 1){
			if(num[i] > num[i+1]){
				num[i]-=1;
				if(i > 0 && num[i-1] > num[i]){
					--i;
					continue;
				}
				else if(i == 0 && num[i] == '0'){
					start++;
				}
				for(int j = i+1; j < len; ++j){
					num[j] = '9';
				}
				break;
			}
			i++;
		}
		printf("Case #%d: %s\n",++ca,num+start);	
	}
	return 0;
}

