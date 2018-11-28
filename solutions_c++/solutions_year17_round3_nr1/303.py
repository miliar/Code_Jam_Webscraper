///////////////////////////////////////////////////////////////////////////////
// TESTING PARAMETERS
///////////////////////////////////////////////////////////////////////////////
// TESTING PARAMETERS
const char* FILENAME="A%d.in";
int FILE_FROM = 0;
int FILE_TO = 0;

#include <cstdlib>
#include <cstdio>
#include <vector>
#define _USE_MATH_DEFINES
#include <math.h>
#include <algorithm>
#include <functional>

const bool OUT_FILE = true;
FILE *FILE_OUT;

///////////////////////////////////////////////////////////////////////////////
struct PANCAKE
{
	int R, H;

	double Surface() const {
		return (double)H * 2.0 * (double)R * M_PI;
	}

	bool operator<(const PANCAKE& other) const
	{
		return this->Surface() > other.Surface();
	}
};

void ProcessFile(FILE* fin)
{
	int C;
	fscanf(fin, "%d", &C);
	for (int i=0; i<C; ++i)
	{
		int N, K, RMax = 0;
		fscanf(fin, "%d %d", &N, &K);
		std::vector<PANCAKE> S;
		S.resize(N);
		for (int j = 0; j < N; ++j)
			fscanf(fin, "%d %d", &S[j].R, &S[j].H);
		std::sort(S.begin(), S.end());
		double res = 0;
		for (int j = 0; j < K; ++j) {
			res += S[j].Surface();
			if (S[j].R > RMax)
				RMax = S[j].R;
		}
		double RMaxSurface = (double)RMax * (double)RMax * M_PI;
		res += RMaxSurface;
		double HMax = S[K-1].Surface();

		double diffMax = 0;
		for (int j = K; j < N; ++j) {
			double diff = S[j].Surface() - HMax + (double)S[j].R * (double)S[j].R * M_PI - RMaxSurface;
			if (diff > diffMax)
				diffMax = diff;
		}
		if (diffMax > 0)
			res += diffMax;

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
