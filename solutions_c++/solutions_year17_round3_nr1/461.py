#include <bits/stdc++.h>


using namespace std;


int N, K;

pair<long long, long long> pancakes[1000];
vector< int > chosen;

void read()
{
	scanf( "%d%d", &N, &K);
	for (int i = 0; i < N; ++i)
	{
		scanf( "%lld%lld", &pancakes[i].second,&pancakes[i].first);
	}
//	sort(pancakes, pancakes+N);
	//chosen.clear();
}

void solve()
{
	long long result = 0;

	//assume each is bottom one

	for (int i = 0; i < N; ++i)
	{

		priority_queue<long long> Q;

		while(!Q.empty())
			Q.pop();

		for (int j = 0; j < N; ++j)
		{
			if(i == j)
				continue;
			if( pancakes[i].second >= pancakes[j].second)
				Q.push( pancakes[j].second*pancakes[j].first );
		}
		if(Q.size()  >= K-1)
		{
			long long tempResult = pancakes[i].second*pancakes[i].second + pancakes[i].first*pancakes[i].second*2;
			for (int j = 0; j < K-1; ++j)
			 {
			 	tempResult+= 2*Q.top();
			 	Q.pop();
			 } 
			result = max(result,tempResult);
		}
	}




	printf("%.7Lf\n", (long double)result*M_PI);
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