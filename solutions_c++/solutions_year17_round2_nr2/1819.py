#include <stdio.h>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
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
	int C[6] = {'R', 'O', 'Y', 'G', 'B', 'V'};
	pair<char, int> counts[6];
	int N;
	char U[1001] = {0};
	int numU = 0;

	cin >> N;
	for(int i = 0; i < 6; i++)
	{
		counts[i].first = C[i];
		cin >>counts[i].second;
	}

	sort(counts, counts+6, [](pair<char, int> a, pair<char, int> b) {return a.second < b.second;});
	for(int i = 0; i < 6; i++)
		for(int j = 0; j < counts[i].second; j++)
		U[numU++] = counts[i].first;

	//printf("%s\n\n", U);
	char out[1001] = {0};
	int j = 0;
	for(int i = 0; i < numU; i += 2)
		out[i] = U[j++];
	for(int i = 1; i < numU; i += 2)
		out[i] = U[j++];
    //printf("%s\n", out);

    bool impossible = false;
    for(int i = 0; i < numU && !impossible; ++i)
    	impossible = out[i] == out[(i+1) % numU];

    if(impossible)
		printf("Case #%d: IMPOSSIBLE\n", (casenum+1));
	else
		printf("Case #%d: %s\n", (casenum+1), out);
}

int main()
{
	int N;
	cin >> N;
	for(int i = 0; i < N; ++i)
		docase(i);
	return 0;
}