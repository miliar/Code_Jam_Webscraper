#include <cstdio>
#include <cstring>

void Flip(char* data, int start, int length)
{
	for (int i = start; i < start + length; i++)
	{
		if (data[i] == '-')data[i] = '+';
		else data[i] = '-';
	}
}

bool isSeikai(char* data)
{
	for (int i = 0; data[i]; i++)
		if (data[i] == '-')return false;
	return true;
}

int main(void)
{
	int testcase;
	int cnt = 0;
	FILE* f = fopen("A-large.in", "r");
	FILE* output = fopen("out.out", "w");
	fscanf(f,"%d", &testcase);
	for (int tc = 0; tc < testcase; tc++)
	{
		char buf[1001];
		int size, len;
		
		fscanf(f,"%s %d", buf, &size);
		len = strlen(buf);

		char* data = new char[len];
		strcpy(data, buf);
		for (int i = 0; i <= len-size; i++)
		{
			if (data[i] == '-')
			{
				Flip(data, i, size);
				i = 0;
				cnt++;
				printf("%d : %s\n", cnt, data);
			}
			if (cnt > (len - size + 1))
			{
				cnt = -1;
				break;
			}
		}
		if ( (cnt == -1) || !isSeikai(data))
		{
			fprintf(output,"Case #%d: IMPOSSIBLE\n", tc + 1);
		}
		else
		{
			fprintf(output,"Case #%d: %d\n", tc + 1, cnt);
		}
		cnt = 0;
	}
}