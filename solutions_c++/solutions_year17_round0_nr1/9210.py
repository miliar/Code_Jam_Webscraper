#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int main()
{
	int test,count=1;
	cin >> test;
	while(test--)
	{
		getchar();
		char array[1004];
		int k;
		scanf("%s %d",array,&k);
              //  printf("%s\n%d\n",array,k);
		int len,i,j;
		len=strlen(array);
		int flip=0;
		for(i=0;i<=len-k;i++)
		{
                //   printf("loop1\n");
			if(array[i]!='+')
			{
				flip++;
				for(j=i;j<=i+k-1;j++)
				{
                         //         printf("loop2 ");
					if(array[j]=='-')
						array[j]='+';
					else
						array[j]='-';
				}
			}

		}
            // printf("for loop complete\n");
		int s,flag=0;
		if(len>=k)
			s=len-k;
		else
			s=0;
		for(i=s;i<len;i++)
		{
			if(array[i]=='-')
			{
				flag=1;
				break;
			}
		}
		if(flag==0)
			printf("Case #%d: %d\n",count,flip);
		else
			printf("Case #%d: IMPOSSIBLE\n",count);
		count++;
	}
	return 0;
}
