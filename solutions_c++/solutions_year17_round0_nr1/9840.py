#include <iostream>  // includes cin to read from stdin and cout to write to stdout
using namespace std;  // since cin and cout are both in namespace std, this saves some text

#define PUSH(_X_, _LEN_, _COUNT_, _START_) strncpy(STACK_S[idx_STACK], _X_, _LEN_); STACK_C[idx_STACK][0] = _COUNT_; STACK_C[idx_STACK][1] = _START_;idx_STACK++;
#define POP(_X_, _LEN_, _COUNT_, _START_) idx_STACK--; strncpy(_X_, STACK_S[idx_STACK], _LEN_); _COUNT_ = STACK_C[idx_STACK][0]; _START_ = STACK_C[idx_STACK][1];
char STACK_S[1000][1001];
int STACK_C[1000][2];
int idx_STACK;

void main() {
	int testcase, count, i, strat;
	int len;
	int K;
	char S[1001] = { 0, };

	cin >> testcase;  // read t. cin knows that t is an int, so it reads it as such.

	for (int t = 1; t <= testcase; ++t) {
		cin >> S >> K;  // read n and then m.
		len = strlen(S);
		idx_STACK = 0;

		PUSH(S, len, 0, 0);

		while (idx_STACK > 0)
		{
			POP(S, len, count, strat);

			/// CHECK ALL '+'
			for (i = 0; i < len; i++)
			{
				if (S[i] == '-')
				{
					break;
				}
			}

			if (len == i)
			{
				break;
			}

			for (int j = strat; j <= (len - K); j++)
			{
				char S_[1001] = { 0, };

				strncpy(S_, S, len);

				for (int m = j; m < (j + K); m++)
				{
					if (S_[m] == '-')
					{
						S_[m] = '+';
					}
					else
					{
						S_[m] = '-';
					}
				}
				PUSH(S_, len, (count + 1), (j + 1));
			}

			count = -1;
		}
		
		if (count >= 0)
		{
			cout << "Case #" << t << ": " << count << endl;
		}
		else
		{
			cout << "Case #" << t << ": IMPOSSIBLE" << endl;
		}
		// cout knows that n + m and n * m are ints, and prints them accordingly.
		// It also knows "Case #", ": ", and " " are strings and that endl ends the line.
	}
}