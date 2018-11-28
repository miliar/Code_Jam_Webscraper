#include <iostream>
#include <fstream>
#include <algorithm>
#include <list>
#include <stack>
#include <vector>
#include <string>
#include <cstring>
#include <cstdio>
#include <unordered_map>

using namespace std;

#define FACE	1
#define BLANK	0

void flip(char *buf, int pos, int N)
{
	for(int i = 0; i < N; i++)
		buf[i+pos] ^= 1;
}

bool isDone(char * buf, int l)
{
	for(int i = 0; i < l; i++) {
		if (buf[i] == BLANK) return false;
	}
	return true;
}

void disp(char *buf, int L)
{
	for(int i = 0; i < L; i++) {
		char ch = ' ';
		if (buf[i] == FACE) ch = '+';
		else if (buf[i] == BLANK) ch = '-';
		cout << ch;
	}
	cout << endl;
}

int go(char *buf, int L, int N)
{
	int step = 0;
	for (int i = 0; i <= L-N; i++) {
		if (buf[i] == BLANK) {
			flip(buf, i, N);
			step++;
		}
	}

	if (!isDone(buf, L)) return -1;
	return step;
}

int main(int ac, char **av)
{
	int T;
	cin >> T;
	for (int i = 0 ; i < T; i++) {
		char buf[4000];
		int N, L;
		cin >> buf >> N;
		L = strlen(buf);
		//cout << buf << " " << L << " " << N << endl;
		for (int j = 0; j < L; j++) {
			if (buf[j] == '-') buf[j] = BLANK;
			else if (buf[j] == '+') buf[j] = FACE;
		}
		int step = go (buf, L, N);
		cout << "Case #" << (i+1) << ": ";
		if (step >= 0) cout << step;
		else cout << "IMPOSSIBLE";
		cout << endl;
	}
	return 0;
}

