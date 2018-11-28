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
    char N[25];
    char R[25];
    int i,j,x,k;
    char tidy;

    cin >> T;
    
    for (x=0;x<T;x++)
    {

	cin >> N;
	tidy = 0;
	k = strlen(N);
	while (!tidy)
	{
		tidy = 1;
		for (i=0;i<k-1;i++)
		{
			if (N[i]>N[i+1])
			{
				tidy = 0;
				if (N[i]=='0') N[i]=9;
				else N[i]=N[i]-1;
				for (j=i+1;j<k;j++)
					N[j]='9';
			}
		}
	}
	// trim 0s at the beginning
	j=-1;
	for (i=0;i<k;i++)
	{
		if (N[i]=='0') j=i;
		else break;
	}
	for (i=j+1;i<k;i++)
	{
		R[i-j-1]=N[i];
	}
	R[k-j-1]=0;
	

        printf("Case #%d: %s\n",x+1,R);

    }
}
