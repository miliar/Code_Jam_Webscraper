#include<bits/stdc++.h>
using namespace std;

int main(){
	int n,tc=1;
	scanf("%d",&n);
	
	while(n--){
		int cnt=0, k, len, fail=0;
		char arr[1010]={};
		
		getchar();
		scanf("%s %d",&arr,&k);
		len = strlen(arr);
		
		
		for(int i=0;i<len;i++){
			if(arr[i]=='-'){
				cnt++;
				if(i+k<=len){
					for(int j=i;j<i+k;j++){
						if(arr[j]=='-') arr[j]='+';
						else if(arr[j]=='+') arr[j]='-';
					}
				}
				else{
					fail=1;
					break;
				}
			}
		}
		
		if(fail==0) printf("Case #%d: %d\n",tc,cnt);
		else printf("Case #%d: IMPOSSIBLE\n",tc);
		tc++;		
	}
	
	return 0;
}
