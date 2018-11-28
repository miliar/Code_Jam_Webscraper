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
	ULL N, K;
	cin >> N >> K;  // ??
	ULL n, zn;
	n = 0;
	zn = 1;
	ULL S[70], L[70], k[70], kp[70];
	S[0] = 1;
	L[0] = 0;
	k[0] = N;
	kp[0] = N+1;

	while (zn <= K)
	{
		n++;
		zn *= 2;
		if (k[n-1] % 2 == 0)
		{
			k[n] = (k[n-1] - 2) / 2;
			kp[n] = k[n-1] / 2;
			S[n] = S[n-1];
			L[n] = 2*L[n-1] + S[n-1];
		}
		else
		{
			k[n] = (k[n-1] - 1) / 2;
			kp[n] = kp[n-1] / 2;
			S[n] = 2*S[n-1] + L[n-1];
			L[n] = L[n-1];
		}
	}
	if (K < L[n-1] + zn/2)
	{
		if (k[n-1] % 2 == 0)
			cout << kp[n] << " " << kp[n];
		else
			cout << kp[n] << " " << k[n];
	}
	else
	{
		if (k[n-1] % 2 == 0)
			cout << kp[n] << " " << k[n];
		else
			cout << k[n] << " " << k[n];
	}
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