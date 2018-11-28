#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <cstring>
#define getcx getchar_unlocked
char a[1000];
int b[1000];
char c[1000];
inline void inp( int &n )//fast input function
{
   n=0;
   int ch=getcx();int sign=1;
   while( ch < '0' || ch > '9' ){if(ch=='-')sign=-1; ch=getcx();}

   while(  ch >= '0' && ch <= '9' )
           n = (n<<3)+(n<<1) + ch-'0', ch=getcx();
   n=n*sign;
}
void flip_4(int k,int l)
{
	for (int i = k; i < k+l; ++i)
	{
		b[i]+=1;
		b[i]%=2;
		// printf("%d\n",b[i] );
	}
}

void convert()
{
	for (int i = 0; a[i] != '\0'; ++i)
	{
		if (a[i]=='+')
		{
			b[i]=1;
		}
		else if(a[i]=='-')
		{
			b[i]=0;
		} 
	}
}

int  search(int k)
{
	for (int i = k; a[i] != '\0'; ++i)
	{
		if (b[i]==0)
		{
			return i;
		}
	}
	return -1;
}
int lenght1()
 {
 	int i;
 	for ( i = 0; a[i] != '\0'; ++i)
 	{
 		/* code */
 		
 	}
 	return i;
 }

int main(int argc, char const *argv[])
{
	int T,k,flag=1,l;
	int m=0,m2=0;
	
	inp(T);
	while(m2<T)
	{
		flag=1;
		scanf("%s %d",a,&k);
		convert();
		l=lenght1();
		int j=search(0);
		// printf("%d\n", j);
		m=0;
		while(j!= -1)
		{
			if (j>l-k)
			{
				/* code */
				flag=0;
				// printf("fuck2 %d\n",j);
				break;
			}

			// printf("fuck1 %d %d\n",j,l);
			flip_4(j,k);

			for (int i = 0; i < l; ++i)
			{
				// printf("%d",b[i]);
			}
			// printf("\n");

			j=search(j);
			// printf("%d j %d flag\n", j,flag);

			m++;
		}

		if (!flag)
		{
			convert();
			for (int i = 0; i < l; ++i)
			{
				// printf("%d",b[i]);
			}
			// printf("\n");
			for (int i = 0; i < l; ++i)
			{
				c[i]=b[l-i-1];

			}
			for (int i = 0; i < l; ++i)
			{
				b[i]=c[i];
			}
			int j=search(0);
			m=0;
			
			while(j!=-1)
			{
		        if (j>l-k)
				{
					/* code */
					flag=0;
					// printf("fuck2 %d\n",j);
					break;
				}
				for (int i = 0; i < l; ++i)
				{
					// printf("%d",b[i]);
				}
				// printf("\n");
				flip_4(j,k);
				j=search(j);

				m++;
			}

		}
		if (!flag)
		{
			printf("Case #%d: IMPOSSIBLE\n",m2+1);
		}
		else
		{
			printf("Case #%d: %d\n",m2+1,m);
		}
		m2++;
	}
	

	
	return 0;
}