#include <iostream>
#include <assert.h>
using namespace std;

long long N, K;

long long h, l;
int ch, cl;

long long getLow(long long n)
{
	if (n%2==0)
		return n/2-1;
	else 
		return n/2;
}

void setHL() 
{ 
	int cls = cl;

	// handle h
	if (h%2 != 0)
		ch *= 2;
	else
		cl += ch;

	// handle l
	if (l != h) {
		if (l%2 != 0)
			cl += cls;
		else
			ch += cls;
	}

	h = h/2;
	l = getLow(l);
}

void runCase(int Case)
{
    cout << "Case #" << Case+1 << ": ";
	cerr << "Case #" << Case+1 << endl;

	int level = 1;
	h = l = N;
	ch = 1;
	cl = 0;

	while (true) {
		if (K < ((long long)1<<level))
			break;

		setHL();
		level++;
	}

	long long idx = K - ((long long)1<<(level-1));

	if (idx < ch) 
		cout << h/2 << " " << getLow(h) << endl;
	else 
		cout << l/2 << " " << getLow(l) << endl;
}

void Run()
{
    int T;
    cin >> T;

    for (int i=0; i < T; i++)
    {
		// Read input
        cin >> N;
		cin >> K;

		// Solve
        runCase(i);
    }
}


void main()
{
	#define FILE_NAME "C-small-2-attempt1" 
    FILE* in = freopen(FILE_NAME ".in",  "r", stdin);
    FILE* out= freopen(FILE_NAME ".out", "w", stdout);
	assert(in!=NULL && out!=NULL);

    Run();

    //system("pause");
}

