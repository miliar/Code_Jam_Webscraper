#include <iostream>
#include <direct.h>
#include <time.h>
//#include <cmath>
#include <assert.h>

#define STL
#ifdef STL
	#include <string>
	#include <sstream>
    #include <algorithm>
    #include <vector>
    //#include <list>
    #include <map>
	//#include <set>
	#include <iterator>
#endif
using namespace std;

char S[1001];
int K;

void swap(int p) {
	for (int i=p; i<p+K; i++)
		if (S[i] == '-')
			S[i] = '+';
		else 
			S[i] = '-';
}

void runCase(int Case)
{
    cout << "Case #" << Case+1 << ": ";
	cerr << "Case #" << Case+1 << endl;

	int len = strlen(S);
	int count = 0;

	for (int p=0; p<len; p++) {
		if (S[p] == '+')
			continue;

		if (p+K > len) {
			cout << "IMPOSSIBLE" << endl;
			return;
		}

		swap(p);
		count++;
	}

	cout << count << endl;
}

void Run()
{
    int T;
    cin >> T;

    for (int i=0; i < T; i++)
    {
		// Read input
        cin >> S;
        cin >> K;

		// Solve
        runCase(i);
    }
}


void main()
{
	#define FILE_NAME "A-large" 
    FILE* in = freopen(FILE_NAME ".in",  "r", stdin);
    FILE* out= freopen(FILE_NAME ".out", "w", stdout);
	assert(in != NULL);

    Run();

    //system("pause");
}

