#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <map>
#include <math.h>

using namespace std;

int main()
{
    int T;
    int R,C;
    int i,j,x,k,m,kx,ky;
    int kxmin,kxmax;
    int kymin,kymax;
    int isOK;
    char row[30];
    char cake[30][30];
    char letters[26];

    cin >> T;
    
    for (x=0;x<T;x++)
    {

	cin >> R;
	cin >> C;
	for (i=0;i<R;i++)
	{
		cin >> row;
		for (j=0;j<C;j++)
			cake[i][j] = row[j];
	}
	k=0;
	for (i=0;i<R;i++)
		for (j=0;j<C;j++)
			if (cake[i][j]!='?')
				letters[k++] = cake[i][j];
	

	for (m=0;m<k;m++) // solve for each letter
	{
		// find the letter on the cake
		for (i=0;i<R;i++)
		for (j=0;j<C;j++)
			if (cake[i][j]==letters[m])
			{
				kx = i;
				ky = j;
				break;
			}
		// try to grow around kx,ky	
		// find the limits
		i=1;
		while (ky-i>=0 && cake[kx][ky-i]=='?')
			i++;
		kymin = ky-i+1;
		i=1;
		while (ky+i<C && cake[kx][ky+i]=='?')
			i++;
		kymax = ky+i-1;
		j=1;
		while (kx-j>=0 && cake[kx-j][ky]=='?')
			j++;
		kxmin = kx-j+1;
		j=1;
		while (kx+j<R && cake[kx+j][ky]=='?')
			j++;
		kxmax = kx+j-1;
	
		for (j=kymin;j<=kymax;j++) // fill in the row
			cake[kx][j]=letters[m];

		for (i=kx+1;i<=kxmax;i++)
		{
			isOK = 1;
			for (j=kymin;j<=kymax;j++)
			{
				if (cake[i][j]!='?' && cake[i][j]!=letters[m])
				{
					isOK=0;
					break;
				}
			}	
			if (isOK==0) break;
			else
			{
				for (j=kymin;j<=kymax;j++)
					cake[i][j]=letters[m];
			}
		}
		
		for (i=kx-1;i>=kxmin;i--)
		{
			isOK = 1;
			for (j=kymin;j<=kymax;j++)
			{
				if (cake[i][j]!='?' && cake[i][j]!=letters[m])
				{
					isOK=0;
					break;
				}
			}	
			if (isOK==0) break;
			else
			{
				for (j=kymin;j<=kymax;j++)
					cake[i][j]=letters[m];
			}
		}
	}

        printf("Case #%d:\n",x+1);
	for (i=0;i<R;i++)
	{
		for (j=0;j<C;j++)
			printf("%c",cake[i][j]);
		printf("\n");
	}

    }
}
