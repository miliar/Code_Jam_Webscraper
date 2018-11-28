#include <bits/stdc++.h>
using namespace std;

int ile[5], zapile[5];
int n, p;

int policz()
{
	for(int i = 0 ; i < p ; i++)
		ile[i] = zapile[i];
	vector <int> vec;
	int poprz = 0;
	for(int i = 1 ; i <= n ; i++)
	{
		int c = (6 - poprz) % p;
		while(ile[c] == 0)
			c = rand() % p;
		vec.push_back(c);
		ile[c]--;
		poprz += c;
		poprz %= p;
	}
	int sum = 0, wyn = 0;
	for(int i = 0 ; i < (int)vec.size() ; i++)
	{
		if(sum == 0)
			wyn++;
		sum += vec[i];
		sum %= p;
	}
	return wyn;
}

int solve()
{
	scanf("%d%d", &n, &p);
	for(int i = 0 ; i < p ; i++)
		ile[i] = 0;
	for(int i = 1 ; i <= n ; i++)
	{
		int a;
		scanf("%d", &a);
		ile[a % p]++;
	}
	for(int i = 0 ; i < p ; i++)
		zapile[i] = ile[i];
	int wyn = 100000;
	for(int i = 0 ; i < 10000 ; i++)
		wyn = min(wyn, policz());
	return wyn;
}

int main()
{
	srand(1234);
	int t;
	scanf("%d", &t);
	for(int i = 1 ; i <= t ; i++)
	{
		printf("Case #%d: %d\n", i, solve());
	}
}
