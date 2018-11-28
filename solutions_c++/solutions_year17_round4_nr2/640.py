///////////////////////////////////////////////////////////////////////////////
// TESTING PARAMETERS
///////////////////////////////////////////////////////////////////////////////
// TESTING PARAMETERS
const char* FILENAME="B%d.in";
int FILE_FROM = 0;
int FILE_TO = 0;

#include <cstdlib>
#include <cstdio>
#include <vector>

using namespace std;

const bool OUT_FILE = true;
FILE *FILE_OUT;

///////////////////////////////////////////////////////////////////////////////

void ProcessFile(FILE* fin)
{
	int T;
	fscanf(fin, "%d", &T);
	for (int i=0; i<T; ++i)
	{
		int N, C, M, R = 0, P = 0, p, b;
		fscanf(fin, "%d %d %d", &N, &C, &M);

		R = (M + N - 1) / N; // ideally

		vector<int> NN;
		NN.resize(N);
		vector<int> T;
		T.resize(C);
		for (int j = 0; j < M; ++j) {
			fscanf(fin, "%d %d", &p, &b);
			++NN[p-1];
			if (++T[b-1] > R)
				R = T[b-1];
		}
		int All = 0;
		for (int j = 0; j < N; ++j)
		{
			All += NN[j];
			int RNew = (All + j) / (j + 1);
			if (RNew > R)
				R = RNew;
		}
		for (int j = 0; j < N; ++j)
			if (NN[j] > R)
				P += NN[j] - R;
		fprintf(FILE_OUT, "Case #%d: %d %d\n", i+1, R, P);
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
