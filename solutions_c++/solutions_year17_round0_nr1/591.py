#include <cstdio>
#include <cstring>
#include <cstdlib>
using namespace std;
int main()
{
	FILE *fp, *fo;
	
	int n, m, tot, tt;
	fp = fopen("a.input", "r");
	fo = fopen("a.output", "w");
	fscanf(fp, "%d\n", &tot);
	for (tt = 0; tt < tot; tt++)
	{
		int flip[2001] = {0}, ans = 0;
		char s[2001] = "";
		fscanf(fp, "%s%d\n", &s, &m);
		n = strlen(s);
		fprintf(fo, "Case #%d: ", tt+1);
		for (int i = 0; i <= n-m; i++)
		{
			if (s[i] != '+')
			{
				ans++;
				for (int j = i; j < i + m; j++)
					if (s[j] == '+')
						s[j] = '-';
					else
						s[j] = '+';
			}		
		}
		for (int i = 0; i < n; i++)
			if (s[i] != '+')
				ans = -1;
		if (ans == -1)
			fprintf(fo, "IMPOSSIBLE\n");
		else
			fprintf(fo, "%d\n", ans);
	}
	fclose(fp);
	fclose(fo);
	return 0;	
} 
