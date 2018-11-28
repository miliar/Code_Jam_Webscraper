#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <string>
#include <vector>

using namespace std;

typedef long long ll;

FILE* streamOut = stdout;
FILE* streamIn = stdin;

vector<int> buffer;

bool is_tidy(ll n)
{
	int last = 9;

	while (n)
	{
		if (n % 10 > last)
			return false;
		last = n % 10;
		n /= 10;
	}

	return true;
}

int first_disorder_index()
{
	for (int i = 0; i < buffer.size() - 1; ++i) {
		if (buffer[i] > buffer[i + 1])
			return i;
	}

	return -1;
}

ll solveBruteForce(ll n)
{
	if (n == -1)
		fscanf(streamIn, "%I64d", &n);

	while (n)
	{
		if (is_tidy(n)) {
			fprintf(streamOut, "%I64d\n", n);
			return n;
		}
		n--;
	}

	return -1;
}

ll solve(ll n)
{
	if (n == -1)
		fscanf(streamIn, "%I64d", &n);

	buffer.clear();
	buffer.shrink_to_fit();

	ll tmp = n;
	while (tmp)
	{
		buffer.push_back(tmp % 10);
		tmp /= 10;
	}

	reverse(buffer.begin(), buffer.end());

	int ind = first_disorder_index();
	if (ind == -1) {
		fprintf(streamOut, "%I64d\n", n);
		return n;
	}

	int j = ind;
	while (j >= 0 && buffer[j] == buffer[ind])
		j--;

	j++;

	ll res = 0;

	if (j == 0 && buffer[0] == 1) {
		for (int i = 0; i < buffer.size() - 1; ++i)
			res = res * 10 + 9;
		fprintf(streamOut, "%I64d\n", res);
		return res;
	}

	for (int i = 0; i < j; ++i) {
		res = res * 10 + buffer[i];
	}
	res = res * 10 + buffer[j] - 1;
	for (int i = j + 1; i < buffer.size(); ++i)
		res = res * 10 + 9;

	fprintf(streamOut, "%I64d\n", res);

	return res;
}

int main()
{
	fopen_s(&streamIn, "input.txt", "r");
	fopen_s(&streamOut, "output.txt", "w");

	int TC;
	fscanf(streamIn, "%d", &TC);
	for (int i = 1; i <= TC; ++i) {
		fprintf(streamOut, "Case #%d: ", i);
		solve(-1);
	}

	return 0;
}