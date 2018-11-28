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

int is_tidy (char *s)
{
	for (int i = 1; s[i]; i++)
		if (!(s[i] >= s[i-1])) return 0;

	return 1;
}

char *update (char *s)
{
	int n = strlen(s);

	for (int i = 0; i < n-1; i++)
	{
		if (s[i] <= s[i+1])
			continue;

		s[i]--;

		for (int j = i+1; j < n; j++)
			s[j] = '9';

		break;
	}

	while (*s == '0') s++;

	return s;
}

void main()
{
	int n = getint();

	for (int i = 0; i < n; i++)
	{
		char *s = getline();

		while (true)
		{
			if (is_tidy(s))
			{
				printf("Case #%u: %s\n", i+1, s);
				break;
			}

			s = update(s);
		}
	}
}
