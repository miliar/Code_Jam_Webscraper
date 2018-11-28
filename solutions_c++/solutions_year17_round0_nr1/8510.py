#include <iostream>

int main() {
    FILE* fpin = fopen("c:\\A-small.in", "r");
	FILE* fpout = fopen("c:\\A.out","w");

	int T;
	fscanf(fpin, "%d", &T);
	int k;
	for(int i = 0; i < T; i++)
	{
		char s[1001] = {0};
		fscanf(fpin, "%s %d", &s, &k);
		printf("Case #%d: ", i+1);
		int len = strlen(s);
		int c =0;
		for(int i = 0; i < len-k+1 ; i++)
		{
			if(s[i] == '+') continue;
			for (int j = 0 ; j < k; j++)
				if(s[j+i] == '-')
					s[j+i] = '+';
				else
					s[j+i] = '-';
			c++;
		}
		
		int c1 = 0;
		for(int i = 0; i < len; i++)
			if(s[i] == '+')
				c1++;

		if(c1 == len)
			printf("%d\n", c);
		else
			printf("IMPOSSIBLE\n", c);
	}

	fclose(fpin);
	fclose(fpout);

	return 0;
}
