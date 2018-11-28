#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <cstring>
#define getcx getchar_unlocked
char a[18];
int b[18];
char c[18];
inline void inp( int &n )//fast input function
{
   n=0;
   int ch=getcx();int sign=1;
   while( ch < '0' || ch > '9' ){if(ch=='-')sign=-1; ch=getcx();}

   while(  ch >= '0' && ch <= '9' )
           n = (n<<3)+(n<<1) + ch-'0', ch=getcx();
   n=n*sign;
}
int remove_zeroes()
{
	int k=0;
	while(b[k]==0)
	{
		k++;
	}
	for (int i = 0; a[i] != '\0'; ++i)
	{
		c[i]=b[k+i];
	}
	return k;

}
int main(int argc, char const *argv[])
{
	int T,m=0;
	inp(T);
	while(m<T)
	{
		// printf("fuck\n");
		scanf("%s",a);
		// printf("%s\n",a );
		int i;
		for (i = 0; a[i] != '\0'; ++i)
		{
			b[i]=int(a[i])-48;
			// printf("%d",b[i] );
		}
		// printf("\n");
		int lenght =i,pos=0;
		for (int i = 0; i < lenght; ++i)
		{
			if(b[i]>b[i+1])
			{
				b[i]-=1;
				pos=i;
				for (int i = pos+1; i < lenght; ++i)
				{
					b[i]=9;
				}
				break;

			}

		}
		for (int i = pos; i > 0; --i)
		{
			if(b[i]<b[i-1])
			{
				b[i-1]-=1;
				b[i]=9;
			}
			else{
				break;
			}
		}
		int ze_le=remove_zeroes();
		printf("Case #%d: ",m+1 );
		for (i = 0; i<lenght-ze_le; ++i)
		{
			printf("%d",c[i] );
		}
		printf("\n");
		m++;	
	}
	return 0;
}