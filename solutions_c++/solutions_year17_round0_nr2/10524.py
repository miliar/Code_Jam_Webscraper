#include <stdio.h>
#include <string.h>

int main(){

	FILE *r = fopen("B-small-attempt2.in", "r");
	FILE *w = fopen("B-small-attempt2.out", "w");

	int i,j,k,m;
	int temp,n,val,cnt,ans,flag;
	int arr[20] = {0,};

	fscanf(r, "%d", &n);
	for(i=1;i<=n;i++)
	{
		fscanf(r, "%d", &val);
		cnt = 1;
		temp = val;
		while(temp>=10){ //자리수?
			cnt++;
			temp /= 10;
		}
		
		for(j=val; j>=0; j--)
		{
			memset(arr,0,20);
			temp = j;
			for(k=0;k<cnt;k++) // j마다 각 자리수 배열에 저장 
			{
				arr[k] = (temp%10);
				temp = temp/10;
			}
			
			flag = 1; 
			for(m=0;m<cnt;m++){ // 자리수 비교 
					
				if(arr[m] < arr[m+1]){
					flag = 0;			
					break;
				}
			}
			if(flag ==1)  // 다 돌았으면 
			{
				ans = j;
				fprintf(w, "case #%d: %d\n", i,ans);	
				break;
			}
		}			
	}
}