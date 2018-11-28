#include <cmath>
#include <cstdint>
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
	return l;
}

void docase(int casenum)
{
    uint64_t N;
    cin >> N;
    std::string S;
    int i, exp=0;

    while(true)
    {
        S = std::to_string(N);
        for(i = int(S.size())-1; i >= 0 && (i > 0 && S[i-1] <= S[i]); i--);

        if(i == 0)
            break;

        uint64_t v = pow(10, exp++);
        uint64_t m = pow(10, exp);
        while(N % m != (m-1))
            N -= v;
    }

    printf("Case #%d: %s\n", casenum+1, S.c_str());
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
