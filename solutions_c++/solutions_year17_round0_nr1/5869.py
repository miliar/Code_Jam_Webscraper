#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char buffer[1024];
char *args[16];

char *getline (FILE *in=NULL)
{
	if (in == NULL) in = stdin;

	char *s = fgets(buffer, sizeof(buffer), in);
	if (s == NULL) return NULL;
	
	char *p = strchr(s, '\n');
	if (p != NULL) *p = '\0';

	return s;
}

int getint (FILE *in=NULL)
{
	char *s = getline(in);
	if (s == NULL) return 0;

	return atoi(s);
}

int split (char *s, char *delim)
{
	int i = 0;

	while (true)
	{
		s = strtok(s, delim);
		if (s == NULL) break;

		args[i++] = s;
		s = NULL;
	}

	return i;
}

int count (char *s, char t)
{
	int n = 0;
	
	for (int i = 0; s[i] != 0; i++)
	{
		if (s[i] == t) n++;
	}

	return n;
}

void main()
{
	int n = getint();

	for (int i = 0; i < n; i++)
	{
		if (split(getline(), " ") != 2)
			continue;

		int k = atoi(args[1]);
		char *s = args[0];

		int m = 0;

		int sj = 0;
		int ej = strlen(s) - k;

		if (count(s, '-') == 0)
		{
			printf("Case #%u: %u\n", i+1, m);
			continue;
		}

		for (int j = sj; j <= ej; j++)
		{
			if (s[j] == '+')
				continue;

			for (int t = 0; t < k; t++)
				s[j+t] = s[j+t] == '-' ? '+' : '-';

			m++;
		}

		if (count(s, '-') > 0)
			printf("Case #%u: IMPOSSIBLE\n", i+1, s);
		else
			printf("Case #%u: %u\n", i+1, m);
	}
}
