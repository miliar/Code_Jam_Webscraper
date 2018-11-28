/*
 * ./executable < input > output
 */
#include <iostream>
#include <sstream>
#include <string>
using namespace std;
#define HAPPY '+'
#define BLANK '-'
int main()
{
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++)
	{
		string S;
		int K;
		cin >> S;
		cin >> K;
		int turns = 0;
		for(int i = 0; i < S.length() - K + 1; i++)
			if(S[i] == BLANK)
			{
				turns++;
				for(int j = i; j < i+K; j++)
					S[j] = (S[j]==HAPPY) ? BLANK : HAPPY;
			}
		bool possible = true;
		for(int i = 0; i < K; i++)
			if(S[S.length()-1-i] == BLANK)
			{
				possible = false;
				break;
			}
		cout << "Case #" << t << ": ";
		if(possible)
			cout << turns << endl;
		else
			cout << "IMPOSSIBLE" << endl;
	}
}
