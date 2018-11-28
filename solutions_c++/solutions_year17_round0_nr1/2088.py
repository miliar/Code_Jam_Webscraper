#include <cstdio>
#include <iostream>
#include <vector>
#include <complex.h>


using namespace std;

int k;
vector<bool> state;

int solve (int start) {
	for (; ; start++) {
		if (state[start] == false)
			break;
		if (start + 1 == state.size ())
			return 0;
	}

	if (start + k > state.size ()) {
		return -1;
	}

	for (int i = start; i < start + k; i++)
		state[i] = !state[i];

	int subresult = solve (start+1);
	if (subresult == -1)
		return -1;

	return 1 + subresult;
}

int main () {
	ios_base::sync_with_stdio (false), cin.tie (nullptr);

	freopen ("in.txt", "r", stdin);
	freopen ("out.txt", "w", stdout);

	int t;
	scanf ("%d", &t);
	for (int tc = 0; tc < t; tc++) {
		char str[1001];
		scanf ("%s %d", str, &k);

		auto length = strlen (str);
		state = vector<bool> (length);
		for (int i = 0; i < length; i++)
			state[i] = str[i] == '+';

		int result = solve (0);

		if (result == -1)
			printf ("Case #%d: IMPOSSIBLE\n", tc + 1);
		else
			printf ("Case #%d: %d\n", tc + 1, result);
	}


	fflush (stdout);
	fclose (stdin);
	fclose (stdout);

	return 0;
}
