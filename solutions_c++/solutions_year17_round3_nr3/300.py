///////////////////////////////////////////////////////////////////////////////
// TESTING PARAMETERS
///////////////////////////////////////////////////////////////////////////////
// TESTING PARAMETERS
const char* FILENAME="C%d.in";
int FILE_FROM = 0;
int FILE_TO = 0;

#include <cstdlib>
#include <cstdio>
#include <vector>
#include <algorithm>

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
		int N, K;
		fscanf(fin, "%d %d", &N, &K);

		double X;
		fscanf(fin, "%lf", &X);

		vector<double> P;
		P.resize(N);
		for (int j = 0; j < N; ++j)
			fscanf(fin, "%lf", &P[j]);
		std::sort(P.begin(), P.end());
		while (X>0)
		{
			int j = 1;
			for (; j < N && P[j] == P[0]; ++j);
			double Goal = j<N ? P[j] : 1;
			if ((Goal -P[0])*(double)j<X)
			{
				X -= (Goal - P[0])*(double)j;
				for (int k = 0; k<j; ++k)
					P[k] = Goal;
			}
			else {
				double S = P[0] + X / (double)j;
				for (int k = 0; k<j; ++k)
					P[k] = S;
				break;
			}
			if (j >= N)
				break;
		}

		double res = 1;
		for (int j = 0; j < N; ++j)
			res *= P[j];

		fprintf(FILE_OUT, "Case #%d: %f\n", i+1, res);
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
