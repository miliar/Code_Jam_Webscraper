#include <cstdio>
#include <cstring>

int t,n,k,cnt;
char arr[101];

void flip(int i){
	if(i+k > n) return;
	for(int j=i; j<i+k; j++){
		if(arr[j]=='-') arr[j]='+';
		else arr[j]='-';
	}
	cnt++;
}

void printAnsw(int tc){
	printf("Case #%d: ",tc);
	for(int i=0; i<n; i++){
		if(arr[i] == '-'){
			printf("IMPOSSIBLE\n");
			return;
		}
	}
	printf("%d\n",cnt);
}

int main(){
	//freopen("A-large.in","r",stdin);

	scanf("%d",&t);
	
	for(int tc=1; tc<=t; tc++){
		scanf("%s %d",arr,&k);
		n = (unsigned)strlen(arr);

		cnt = 0;
		for(int i=0; i<n; i++){
			if(arr[i]=='-'){
				flip(i);
			}
		}

		printAnsw(tc);
	}

	return 0;
}