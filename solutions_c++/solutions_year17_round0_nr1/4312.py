#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <string>

using namespace std;

FILE* streamOut = stdout;
FILE* streamIn = stdin;

char buffer[1001];

void solve(int tNumber)
{
	string t;
	int k;

	fscanf(streamIn, "%s%d", buffer, &k);
	t = buffer;

	int ans = 0;

	for (int i = 0; i <= t.length() - k; ++i)
	{
		if (t[i] == '-') {
			for (int j = i; j < i + k; ++j)
				t[j] = (t[j] == '-') ? '+' : '-';
			ans++;
		}
	}

	fprintf(streamOut, "Case #%d: ", tNumber);

	for (int i = 0; i < t.length(); ++i) {
		if (t[i] == '-') {
			fprintf(streamOut, "IMPOSSIBLE\n");
			return;
		}
	}

	fprintf(streamOut, "%d\n", ans);

	return;
}

int main()
{
	fopen_s(&streamIn, "input.txt", "r");
	fopen_s(&streamOut, "output.txt", "w");

	int TC;
	fscanf(streamIn, "%d", &TC);
	for (int i = 1; i <= TC; ++i) {
		solve(i);
	}

	return 0;
}