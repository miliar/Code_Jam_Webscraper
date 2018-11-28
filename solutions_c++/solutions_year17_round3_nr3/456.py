#include <bits/stdc++.h>


using namespace std;


int N, K;

long double U, probability[55];

long double sum;

void read()
{
	scanf( "%d%d", &N, &K);
	scanf( "%Lf", &U);
	sum = U;
	for (int i = 0; i < N; ++i)
	{
		scanf( "%Lf", &probability[i]);
		sum+= probability[i];
	}
//	sort(pancakes, pancakes+N);
	//chosen.clear();
}

void solve()
{
	int count = N;
	sort(probability, probability + N);
	for( int i = N-1; i >=0; --i)
	{
		if( (sum/(long double)count - probability[i]) < 0)
		{
			sum -= probability[i];
			count--;
		}
	}


	long double result = 1.0;
	for( int i = N-1; i >=0; --i)
	{
		if( (sum/(long double)count - probability[i]) < 0)
		{
			result*=probability[i];
		}
		else
			result *= sum/(long double)count;
	}

	printf("%.7Lf\n", result);
	return;			
}



int main(int argc, char const *argv[])
{
	ios_base::sync_with_stdio(0);

	int T;
	scanf( "%d", &T);
	cout.precision(7);

	for (int t = 1; t <= T; ++t)
	{
		printf("Case #%d: ", t);
		read();
		solve();


	}

	return 0;
}