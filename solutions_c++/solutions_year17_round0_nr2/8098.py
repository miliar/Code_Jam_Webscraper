#include <cstdio>
#include <cstring>
using namespace std;

int main()
{
	int num;
	scanf("%d",&num);
	for(int i=0;i<num;++i){
		int tmp, cnt=0, in[19]={0}, idx;
		char str[18];
		memset(str,'\0',18);
		scanf("%s",str);
		int n = strlen(str), z=1, x=18, y=0;
		while(z <= x-n) in[z++] = 0;
		while(z <= x) in[z++] = str[y++] - '0';
		idx = 18-n;
		for(int j=18;j>idx;--j){
			if(in[j] < in[j-1]) {
				for(int k=18;k>=j;--k){
					in[k] = 9;
				}
				in[j-1]--;
			}
		}
		for(int j=0;j<19;++j){
			if(in[j]!=0)
				break;
			cnt++;
		}
		printf("Case #%d: ",i+1);
		for(int j=cnt;j<19;++j)
			printf("%d",in[j]);
		printf("\n");
	}
	return 0;
}
