#include <iostream>
#include <direct.h>
#include <assert.h>

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

long long N;
long long tens[19];

int isTide(long long n) {
	int c = 0;
	int dr = n % 10;
	n /= 10;

	while (n) {
		c++;
		int dl = n % 10;
		if (dl > dr)
			return c;

		n /= 10;
		dr = dl;
	}
	return 0;
}


void runCase(int Case)
{
    cout << "Case #" << Case+1 << ": ";
	cerr << "Case #" << Case+1 << endl;

	for (long long i=N; i>=0; i--) {
		int c = isTide(i);
		if (c == 0) {
			cout << i << endl;
			break;
		}
		else {
			long long d = i % tens[c];
			i -= d;
		}
	}
}

void Run()
{
    int T;
    cin >> T;

    for (int i=0; i < T; i++)
    {
		// Read input
        cin >> N;

		// Solve
        runCase(i);
    }
}


void main()
{
	#define FILE_NAME "B-large" 
    FILE* in = freopen(FILE_NAME ".in",  "r", stdin);
    FILE* out= freopen(FILE_NAME ".out", "w", stdout);
	assert(in!=NULL && out!=NULL);

	tens[0] = 1;
	for (int i=1; i<19; i++)
		tens[i] = tens[i-1] * 10;

    Run();

    //system("pause");
}

