#include <stdio.h>
#include <iostream>

using namespace std;

void printPre(char c, int count)
{
	while(count--)
		printf("%c", c);
}

int main()
{
	int T = 0;
	scanf("%d", &T);
	//cout << T << endl;
	char wp;
	scanf("%c", &wp);
	for(int c=1;c<=T;++c)
	{
		printf("Case #%d: ", c);
		char pre;
		int pre_count = 1;
		scanf("%c", &pre);
		bool ifBroke = false;
		bool ifAnyOutput = false;

		while(1)
		{
			char curr;
			scanf("%c", &curr);
			if(ifBroke)
			{
				if(curr < '0' || curr > '9')
				{
					printf("\n");
					break;
				}
				else
				{
					printf("9");
					continue;
				}
			}
			//when ifBroke == false
			if(curr < '0' || curr > '9')
			{
				printPre(pre, pre_count);
				printf("\n");
				break;
			}
			if(curr > pre)
			{
				printPre(pre, pre_count);
				ifAnyOutput = true;
				pre = curr;
				pre_count = 1;
			}
			else if(curr == pre)
			{
				pre_count++;
			}
			else
			{
				//when like 1110
				if(ifAnyOutput || pre != '1')
					printf("%c", pre-1);
				for(int i=0;i<pre_count;++i)
					printf("9");
				ifAnyOutput = true;
				ifBroke = true;
			}

		}
		
	}

	return 0;
}