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
    int K,N;
    int i,j,x,k;
    int min, max;
    int maxmin, maxmax;
    int maxj;
    int *free;
    int numFree;

    cin >> T;
    
    for (x=0;x<T;x++)
    {

	cin >> N;
	cin >> K;
	free = (int *)malloc(sizeof(int)*N);

	numFree = 1;
	free[0] = N;

	for (i=0;i<K;i++)
	{
		maxmax = free[0]/2;
		if ((free[0]%2)==0) maxmin = maxmax-1;
                        else maxmin = maxmax;
		maxj = 0;
		for (j=1;j<numFree;j++)
		{
			max = free[j]/2;
			if ((free[j]%2)==0) min = max-1;
			else min = max;

			if (min>maxmin) {
				maxmin = min;
				maxmax = max;
				maxj = j;
			}
			else if (min==maxmin)
			{
				if(max>maxmax)
				{
					maxmin = min;
					maxmax = max;
					maxj = j;
				}
			}
		}
		free[maxj] = maxmin;
		free[numFree] = maxmax;
		numFree = numFree+1;
	}

        printf("Case #%d: %d %d\n",x+1,maxmax,maxmin);

    }
}
