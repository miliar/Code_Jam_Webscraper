#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <map>
#include <math.h>

using namespace std;

int checkS(char *S, int len)
{
	int i;
	for (i=0;i<len;i++)
		if (S[i]=='-') return 0;
	return 1;
}

int main()
{
    int T;
    char S[1001];
    int K;
    int i,j,x;
    int r = 0;

    cin >> T;
    
    for (x=0;x<T;x++)
    {

	cin >> S;
	cin >> K;
	
	if (!checkS(S,strlen(S)) && K>strlen(S))
        	printf("Case #%d: IMPOSSIBLE\n",x+1);
		

	i = 0;
	r = 0;
	while (!checkS(S,strlen(S)) && ((i+K)<=strlen(S)))
	{
		while (i<strlen(S) && S[i]=='+') // find first -
			i++;
		if (i==strlen(S)) break;
		if (i+K>strlen(S)) break;

		for (j=i;j<i+K;j++)
			if (S[j]=='-') S[j] = '+';
			else (S[j]='-');
		r++;
	}
	if ((i+K>strlen(S)) && !checkS(S,strlen(S)))
	{
        	printf("Case #%d: IMPOSSIBLE\n",x+1);
	}
	else
        	printf("Case #%d: %d\n",x+1,r);

    }
}
