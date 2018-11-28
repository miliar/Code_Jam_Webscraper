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
#include <functional>
#include <algorithm>

using namespace std;

const bool OUT_FILE = true;
FILE *FILE_OUT;

///////////////////////////////////////////////////////////////////////////////

struct ACTIVITY
{
	int C;
	int D;
	bool isC;

	bool operator<(const ACTIVITY& other) const
	{
		return C < other.C;
	}

	int endtime() const { return D; }
	int range() const { return D-C; }
};

void ProcessFile(FILE* fin)
{
	int T;
	fscanf(fin, "%d", &T);
	for (int i=0; i<T; ++i)
	{
		int AC, AJ, c, d, C=0, J=0;
		fscanf(fin, "%d %d", &AC, &AJ);
		vector<pair<int, int> > CActivities;
		vector<ACTIVITY> Activities;
		Activities.resize(AJ+AC);
		for (int j = 0; j < AJ+AC; ++j)
		{
			fscanf(fin, "%d %d", &Activities[j].C, &Activities[j].D);
			Activities[j].isC = j<AC;
			if (j < AC)
				C += Activities[j].range();
			else
				J += Activities[j].range();
		}

		sort(Activities.begin(), Activities.end());
		int LastTime = Activities.back().endtime();
		bool LastC = Activities.back().isC;
		
		int CCRanges = 0, CJRanges = 0, JJRanges = 0;
		vector<int> CC, JJ;
		int res = 0;
		for (const ACTIVITY& a : Activities)
		{
			int range = a.C >= LastTime ? a.C-LastTime : a.C + 1440 - LastTime;
			if (a.isC == LastC)
			{
				if (LastC) {
					CC.push_back(range);
					CCRanges += range;
				}
				else {
					JJ.push_back(range);
					JJRanges += range;
				}
			}
			else {
				CJRanges += range;
				++res;
			}
			LastC = a.isC;
			LastTime = a.endtime();
		}
		sort(CC.begin(), CC.end(), greater<int>());
		sort(JJ.begin(), JJ.end(), greater<int>());

		C += CCRanges;
		J += JJRanges;

		if (C > J)
		{
			J += CJRanges;
			for (int i = 0; C > J &&i < CC.size(); ++i, res += 2)
			{
				J += CC[i];
				C -= CC[i];
			}
		} else if (C<J)
		{
			C += CJRanges;
			for (int i = 0; C < J &&i < JJ.size(); ++i, res += 2)
			{
				C += JJ[i];
				J -= JJ[i];
			}
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
