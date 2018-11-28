#include <math.h>
#include <stdio.h>
#include <iostream>

using namespace std;

unsigned len(unsigned i){
	    return i > 0 ? (int) log10 ((double) i) + 1 : 1;
}

int main(void){
	int n;
	unsigned x;
	scanf("%d",&n);
	for (int i = 1; i <= n; ++i)
	{
		cin>>x;

		for (int j = 1; j <= len(x)-1; ++j)
		{
			if ( (  ( x% (unsigned) pow(10,j)) / pow(10,j-1))  >=  ( (	int)(  ( x% (unsigned) pow(10,j+1)) / pow(10,j)) ) )	
			{
				continue;
			}
			x=x-1;
			j=0;
		}
		printf("Case #%d: %d", i, x );
		cout << endl;
	}
	}
