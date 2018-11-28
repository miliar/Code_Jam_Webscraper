#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

void change(char* p,int j)
{
	while(*(p+j) != '\0')
	{
		*(p+j) = '9';
		p++;
	}
}

int main()
{
	int T;
    scanf("%d",&T);
	char N[20];
	bool ans;
    for(int i=1;i<=T;i++)
    {
		ans = false;
		cin >> N;
		int j = 0;
		while(j<20 && N[j+1] != '\0')
		{
			if(N[j] > N[j+1])
			{
				change(N,j+1);
				N[j] -= 1;
				j = 0;
			} else {
				j++;
			}
        }
		printf("CASE #%d: ",i);
		j = 0;
		while(N[j] != '\0')
		{
			if(N[j] != '0' || ans)
			{
				printf("%c",N[j]);
				ans = true;
			}
			j++;
		}	
		printf("\n");
	}
	return 0;
}
