#include <bits/stdc++.h>

using namespace std;


int main(int argc, char const *argv[])
{
	ios_base::sync_with_stdio(0);

	cout.precision(10);

	int T;
	cin>>T;
	for (int t = 1; t <= T; ++t)
	{
		
		long double D;
		int N;
		cin>>D;
		cin>>N;

		long double maxTimeAtEnd = 0;

		for (int i = 0; i < N; ++i)
		 {
		 	long double K, S;
		 	cin>>K>>S;
		 	maxTimeAtEnd = max(maxTimeAtEnd, (D-K)/S);
		 } 

		 cout<<"Case #"<<t<<": "<<(D)/maxTimeAtEnd<<"\n";


	}


	return 0;
}