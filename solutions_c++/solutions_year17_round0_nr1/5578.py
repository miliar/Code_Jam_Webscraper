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
    int K, i, j, flips=0;
    std::string S;
    cin >> S >> K;

    for(i = 0; i <= S.size() - K; i++)
        if(S[i] == '-')
            for(j = 0, flips = flips+1; j < K; j++)
                S[i+j] = S[i+j] == '-' ? '+' : '-';

    bool possible = true;
    for(i = 0; i < S.size() && (possible = S[i] == '+'); i++);

    if(possible)
        printf("Case #%d: %d\n", casenum+1, flips);
    else
        printf("Case #%d: IMPOSSIBLE\n", casenum+1);
}

int main()
{
    int T;
    cin >> T;

    for(int i = 0; i < T; i++)
    {
        docase(i);
    }
	return 0;
}
