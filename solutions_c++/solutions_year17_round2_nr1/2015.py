#include <stdio.h>
#include <string>
#include <iostream>
#include <sstream>
#include <algorithm>
using namespace std;

std::string readline()
{
	std::string l;
	std::getline(cin, l);
	//cout << l << endl;
	return l;
}

void docase(int casenum)
{
	int d, n;
	cin >> d >> n;
	int64_t K[1000], S[1000];

	for(int i = 0; i < n; i++)
		cin >> K[i] >> S[i];

	double T[1000];
	for(int i = 0; i < n; i++)
	{
		T[i] = double(d - K[i]) / double(S[i]);
	}

	double mt = T[0];
	for(int i = 0; i < n; i++)
		mt = max(mt, T[i]);

	double result = d / mt;


	printf("Case #%d: %f\n", (casenum+1), result);
}

int main()
{
	int N;
	cin >> N;
	for(int i = 0; i < N; ++i)
		docase(i);
	return 0;
}