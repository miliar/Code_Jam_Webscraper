#include <iostream>
#include <string>

using namespace std;

bool checkHappy(string S)
{
	bool flag = 1;
	int length = S.length();

	for (int i = 0; i < length; i++) {
		if (S[i] == '-') {
			flag = 0;
			break;
		}
	}
	return flag;
}
int countFlip(string S, int K)
{
	int flip = 0;
	int i = 0;
	int length = S.length();


	for (; i < length; i++) {
		while (S[i] == '+' && i <= length - K)
			i++;
		if (i > length - K)
			break;

		flip++;

		for (int j = i; j - i < K; j++) {
			if (S[j] == '+')
				S[j] = '-';
			else
				S[j] = '+';
		}
	}
	return checkHappy(S) ? flip : -1;
}

int main()
{
	int T;
	int K;
	string S;

	cin >> T;

	for (int i = 0; i < T; i++) {
		int result;

		cin >> S >> K;
		result = countFlip(S, K);
		cout << "Case #" << i + 1 << ": ";
		if (result < 0)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << result << endl;
	}

	return 0;
}
