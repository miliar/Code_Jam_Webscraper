///////////////////////////////////////////////////////////////////////////////
// TESTING PARAMETERS
///////////////////////////////////////////////////////////////////////////////
// TESTING PARAMETERS
const char* FILENAME="A%d.in";
int FILE_FROM = 0;
int FILE_TO = 0;

#include <cstdlib>
#include <cstdio>

const bool OUT_FILE = true;
FILE *FILE_OUT;

///////////////////////////////////////////////////////////////////////////////

void ProcessFile(FILE* fin)
{
	int T;
	fscanf(fin, "%d", &T);
	for (int i=0; i<T; ++i)
	{
		int N, P, G, res;
		int g[4];
		g[0] = g[1] = g[2] = g[3] = 0;
		fscanf(fin, "%d %d", &N, &P);
		for (int j = 0; j < N; ++j) {
			fscanf(fin, "%d", &G);
			++g[G % P];
		}
		res = g[0];
		switch (P)
		{
		case 2: res += (g[1] + 1) / 2; break;
		case 3: 
			if (g[2] >= g[1]) {
				res += g[1];
				g[2] -= g[1];
				g[1] = 0;
				res += (g[2] + 2) / 3;
			} else
			{
				res += g[2];
				g[1] -= g[2];
				g[2] = 0;
				res += (g[1] + 2) / 3;
			}
			break;
		case 4:
			//g[3]
			break;
		}
		fprintf(FILE_OUT, "Case #%d: %d\n", i+1, res);
	}
}

///////////////////////////////////////////////////////////////////////////////

int main(int argc, char* argv[])
{
	char fileName[256];
	printf ("Which file: ");
	fgets ( fileName, 256, stdin );
	if (fileName[0]>13)
	{
		int i = atoi (fileName);
		FILE_FROM = FILE_TO = i;
	}
	for (int file_from=FILE_FROM; file_from<=FILE_TO; ++file_from)
	{
		sprintf(fileName, FILENAME, file_from);
		FILE *fin = fopen(fileName, "r");
		if (!fin)
		{
			printf("!!! CANNOT INF FILE %s", fileName);
			continue;
		} else {
			printf("Processing file: %s ...\n", fileName);
		}
		if (OUT_FILE)
		{
			char fileNameOut[256];
			sprintf(fileNameOut, "%s.out", fileName);
			FILE_OUT = fopen(fileNameOut, "w");
		} else
		{
			FILE_OUT = stdout;
		}
		ProcessFile(fin);
		fclose(fin);
		if (OUT_FILE)
			fclose(FILE_OUT);
	}
	printf("\nREADY!!!\n");
	getc(stdin);
	return 0;
}
