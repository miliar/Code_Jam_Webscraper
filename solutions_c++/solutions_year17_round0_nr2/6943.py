#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;


int main()
{
	freopen("B-large.in","r",stdin);
	freopen("large.out","w",stdout);
	
	int task; scanf("%d", &task);
	for (int cs=1; cs<=task; cs++){
		char s[100];
		scanf("%s", s);
		int i=0;
		for (; i<(int)strlen(s)-1; i++)
		if (s[i]>s[i+1]){
			s[i]--;
			while (i>=1 && s[i-1]>s[i]){
				i--;
				s[i]--;
			}

			for (i++; i<(int)strlen(s); i++)
				s[i] = '9';

			break;
		}

		i = 0;
		while (i+1<strlen(s) && s[i]=='0')
			i++;

		printf("Case #%d: %s\n", cs, s+i);
	}	
	return 0;
}
