///////////////////////////////////////////////////////////////////////////////
// TESTING PARAMETERS
///////////////////////////////////////////////////////////////////////////////
// TESTING PARAMETERS
const char* FILENAME="B%d.in";
int FILE_FROM = 0;
int FILE_TO = 0;

#include <cstdlib>
#include <cstdio>
#include <string>
#include <assert.h>

const bool OUT_FILE = true;
FILE *FILE_OUT;

///////////////////////////////////////////////////////////////////////////////

bool SolveSmall(std::string& res, int R, int Y, int B)
{
	while (R || Y || B) {
		if (R < 0 || Y < 0 || B < 0)
			return false;
		if (res.empty()) {
			if (R > Y && R > B) { res += 'R'; --R; }
			else
			{
				if (Y>B) { res += 'Y'; --Y; }
				else { res += 'B'; --B; }
			}
			continue;
		}
		switch (res.back()) {
		case 'R': if (Y > B || (Y == B && res.front() == 'Y')) { res += 'Y'; --Y;	} else { res += 'B'; --B; }
			break;
		case 'Y': if (R > B || (R == B && res.front() == 'R')) { res += 'R'; --R; } else { res += 'B'; --B; }
			break;
		case 'B': if (Y > R || (Y == R && res.front() == 'Y')) { res += 'Y'; --Y; } else { res += 'R'; --R; }
			break;
		}
	}
	return true;
}

bool Replace(std::string& res, std::string from, std::string to, int count)
{
	for (int i=0; i<count; ++i) {
		size_t start_pos = res.empty() ? 0 : res.find(from);
		if (start_pos == std::string::npos)
 			return false;
		res.replace(start_pos, res.empty() ? 0 : from.length(), res.empty() ? to.substr(1) : to);
	}
	return true;
}

bool Conflicts(char A, char B) {
	if (A == B)
		return true;
	switch (A)
	{
	case 'R': return B == 'V' || B == 'O';
	case 'Y': return B == 'G' || B == 'O';
	case 'B': return B == 'G' || B == 'V';
	case 'G': return B != 'R';
	case 'V': return B != 'Y';
	case 'O': return B != 'B';
	}
	return false;
}

void Check(std::string res, int R, int O, int Y, int G, int B, int V)
{
	for (int i = 0; i < res.size(); ++i) {
		char d = res[i>0 ? i-1 : res.size()-1];
		char c = res[i];
		assert(!Conflicts(c, d));
		switch (c) {
		case 'R': --R; break;
		case 'Y': --Y; break;
		case 'B': --B; break;
		case 'G': --G; break;
		case 'V': --V; break;
		case 'O': --O; break;
		}
		assert(R >= 0);
		assert(Y >= 0);
		assert(B >= 0);
		assert(G >= 0);
		assert(V >= 0);
		assert(O >= 0);
	}
}

void ProcessFile(FILE* fin)
{
	int T;
	fscanf(fin, "%d", &T);
	for (int t=0; t<T; ++t)
	{
		int N, R, O, Y, G, B, V;
		fscanf(fin, "%d %d %d %d %d %d %d", &N, &R, &O, &Y, &G, &B, &V);
		std::string res;
		res.reserve(N);
		if (!SolveSmall(res, R - G, Y - V, B - O) || !Replace(res, "R", "RGR", G) || !Replace(res, "Y", "YVY", V) || !Replace(res, "B", "BOB", O) || Conflicts(res.back(), res.front()) ) {
			fprintf(FILE_OUT, "Case #%d: IMPOSSIBLE\n", t + 1);
		}
		else {
			Check(res, R, O, Y, G, B, V);
			fprintf(FILE_OUT, "Case #%d: %s\n", t + 1, res.c_str());
		}
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
