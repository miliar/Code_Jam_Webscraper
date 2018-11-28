#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

int main(void)
{
	int t;
	scanf("%d", &t);
	for(int tst = 1;tst <= t;tst++) {
	int k, res = 0;
	string S;
	cin >> S;
	scanf("%d", &k);
	for(int i = 0;i < int(S.size());i++)
	{
		if(S[i] == '-')
		{
			res++;
			int l = min(i, int(S.size())-k);
			//cout << i << " " << l << "\n";
			for(int j = l;j < l+k;j++)
			{
				if(S[j] == '-') S[j] = '+';
				else S[j] = '-';
			}
		}
	}

	bool done = 1;
	for(int i = 0;i < int(S.size());i++)
	{
		if(S[i] == '-') done = 0;
	}
	printf("Case #%d: ", tst);
	if(done) printf("%d\n", res);
	else printf("IMPOSSIBLE\n"); }
}