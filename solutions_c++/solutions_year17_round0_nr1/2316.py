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
	int T, K;
	fscanf(fin, "%d", &T);
	for (int i=0; i<T; ++i)
	{
		char S[1024];
		fscanf(fin, "%s", &S);
		fscanf(fin, "%d", &K);
		int flips = 0;
		for (char* c = S; *c && flips>=0; ++c) {
			if (*c == '-') {
				++flips;
				for (char* d = c; d < c + K; ++d)
				{
					if (!*d) {
						flips = -1;
						break;
					}
					*d = *d == '+' ? '-' : '+';
				}
			}
		}
		if (flips>=0)
			fprintf(FILE_OUT, "Case #%d: %d\n", i+1, flips);
		else
			fprintf(FILE_OUT, "Case #%d: IMPOSSIBLE\n", i + 1);
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
