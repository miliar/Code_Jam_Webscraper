#include <stdio.h>
#include <stdint.h>
#include <string.h>

//requires no leading zeroes, only 0-9 and NUL
//usage: lt(a,b) <=> a < b
bool lt(char* a, char* b)
{
	for (int i=0;a[i] || b[i];i++)
	{
		if (a[i] && !b[i]) return false;
		if (b[i] && !a[i]) return true;
	}
	for (int i=0;a[i];i++)
	{
		if (a[i]<b[i]) return true;
		if (a[i]>b[i]) return false;
	}
	return true;
}

int main()
{
	int loops;
	scanf("%i", &loops);
	
	for (int L=0;L<loops;L++)
	{
		char max[50];
		scanf("%s", max);
		char out[50]="";
		
		memset(out, '1', strlen(max));
		if (lt(out, max))
		{
			for (int i=0;max[i];i++)
			{
				out[i]='1';
			}
			for (int i=0;max[i];i++)
			{
				char orig=out[i];
				char test=orig;
				while (test!='9')
				{
					test++;
					memset(out+i, test, strlen(out+i));
					if (!lt(out, max))
					{
						memset(out+i, test-1, strlen(out+i));
						break;
					}
				}
			}
		}
		else
		{
			for (int i=0;max[i+1];i++)
			{
				out[i]='9';
				out[i+1]='\0';
			}
		}
		
		if (false)
		{
		fail:
			printf("Case #%i: IMPOSSIBLE\n", L+1);
		}
		else
		{
			printf("Case #%i: %s\n", L+1, out);
		}
	}
}
