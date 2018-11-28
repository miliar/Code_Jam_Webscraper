#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int T;
    scanf("%d",&T);
    for(int t=1;t<=T;t++)
    {
        printf("Case #%d: ",t);
        char str[25];
        scanf(" %s", str+1);
        int len = strlen(str+1);

        for(int i=1; i<=len-1; i++)
        {
        	if(str[i] <= str[i+1])
        		continue;
        	while(i>1 && str[i] == str[i-1])
        		i--;
        	str[i]--;
        	for(int j=i+1; j<=len; j++)
        		str[j] = '9';
        }
        if(str[1] == '0')
        	printf("%s\n", str+2 );
        else
        	printf("%s\n", str+1 );
    }
    return 0;
}
