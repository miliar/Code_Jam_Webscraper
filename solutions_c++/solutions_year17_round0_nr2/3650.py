#include <cstdio>
#include <cstring>

int t,n;
char arr[19];

void printAnsw(int tc){
	printf("Case #%d: ",tc);
	int i=0;
	while(arr[i]==0) i++;
	for(; i<n; i++){
		printf("%d",arr[i]);
	}
	printf("\n");
}

int main(){
	//freopen("B-large.in","r",stdin);
	scanf("%d",&t);

	for(int tc=1; tc<=t; tc++){
		scanf("%s",arr);
		n = strlen(arr);

		//printf("%s %d\n",arr,n);
		for(int i=0; i<n; i++) arr[i] -= 48;

		for(int i=n-1; i>0; i--){
			if(arr[i-1] > arr[i]){
				//1.앞에 줄이기
				arr[i-1]--;
				arr[i]=9;
				//2.뒤에 맞추기
				for(int j=i+1; j<n; j++){
					if(arr[j]==9) break;
					arr[j]=9;
				}
			}
		}		

		printAnsw(tc);

	}
}