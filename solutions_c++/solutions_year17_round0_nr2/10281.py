#include<stdio.h>
#include<string.h>
int main(void)
{
	FILE *fp;
	FILE *fp2;

	fp = fopen("output.txt","wt");
	fp2 = fopen("B-small-attempt3.in","r");
	long int T,N;
	//char NB[23] = {0, };
	long int count = 0;
	int flag = 0;
	int a,b,temp,temp2;
	fscanf(fp2,"%d",&T);
	for(int i = 0 ; i < T; i++)
	{
		fscanf(fp2,"%ld",&N);
		if(N < 10)
			temp2 = N;
		else if(N == 10)
			temp2 = 9;
		else{
			for(long int j = 11 ; j <= N; j++)
			{
				temp = j;
				while(1)
				{
					a = temp%10;
					temp = temp/10;
					b = temp%10;
					if(temp == 0)
						break;
					if(b <= a)
						flag = 1;
					else
					{
						flag = 0;
						break;
					}
				}
				if(flag == 1)
				{
					count++;
					temp2 = j;
				}
				flag = 0;
			}
		}
		fprintf(fp,"Case #%d: %ld\n",(i+1),temp2);
	}

	fclose(fp);
	fclose(fp2);

	return 0;
}