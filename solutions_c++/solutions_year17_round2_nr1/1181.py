#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <set>
#include <list>
#include <map>
#include <deque>
#include <string>

using namespace std;

int t,T;

#define ULL unsigned long long

void runtestcase()
{	
	ULL D,N;
	cin >> D >> N;
	vector<ULL> K(N), S(N);
	for (ULL n=0; n<N; n++)
		cin >> K[n] >> S[n];

	ULL m = 0;
	for (ULL n=1; n<N; n++)
	{
		if ((D-K[n]) * S[m] > (D-K[m]) * S[n])
			m = n;
	}
	
	printf("%.6f", double(D)*double(S[m])/(double(D)-double(K[m])));
}

void main()
{	
	cin >> T;
	for (t = 1; t <= T; t++)
	{
		cerr << t;
		cout << "Case #" << t << ": ";
		runtestcase();
		cout << endl;
	}	
}