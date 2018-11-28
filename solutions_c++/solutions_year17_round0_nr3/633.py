#include <bits/stdc++.h>
using namespace std;
const char* fileIn = "problemC.txt";
const char* fileOut = "problemCOut.txt";
const bool submitting = true;
void solveCase(int caseNumber);
void printCase(int caseNumber, long long k);
int main()
{
	if(submitting)
	{
		freopen(fileIn, "r", stdin);
		freopen(fileOut, "w", stdout);
	}
	int t;
	scanf("%d", &t);
	for(int caseNumber = 1; caseNumber <= t; caseNumber++)
		solveCase(caseNumber);
	return 0;
}

typedef long long ll;
map<ll, ll> cnt;
void solveCase(int caseNumber)
{
	fprintf(stderr, "Test %d\n", caseNumber);
	ll n, k;
	scanf("%lld%lld",&n,&k);
	cnt.clear();
	priority_queue<ll> pq;
	pq.push(n);
	cnt[n] = 1ll;
	while(555>333)
	{
		ll best = pq.top();
		pq.pop();
		ll count = cnt[best];
		if(count >= k)
		{
			printCase(caseNumber, best);
			break;
		}
		k -= count;
		ll rem1 = (best - 1) / 2;
		ll rem2 = best / 2;
		if(rem1 > 0) 
		{
			if(cnt[rem1] == 0)
				pq.push(rem1);
			cnt[rem1] += count;
		}
		if(rem2 > 0) 
		{
			if(cnt[rem2] == 0)
				pq.push(rem2);
			cnt[rem2] += count;
		}
	}
}
void printCase(int caseNumber, long long k)
{
	long long answer1 = k / 2;
	long long answer2 = (k - 1) / 2;
	printf("Case #%d: ", caseNumber);
	printf("%lld %lld\n", answer1, answer2);
}