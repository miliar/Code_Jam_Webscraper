#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <sstream>

using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define SZ(x) (int)(x.size())
#define F0(i,n) for(int i=0;i<n;i++)
#define F1(i,n) for(int i=1;i<=n;i++)


// ---------------------------------------------------
// ---------------------------------------------------

bool release = true;

void util(int N, int K, pair<int, int>& minmax)
{
	// if K == 1
	int w = 1, t = 1;

	while(w*2-1 < K) { w *= 2; t += w;}
	t -= w; w /= 2;
	int nPeopleLeft = K-t;

	if (!release)
	printf("total people already in %d, w %d, nPeopleLeft %d\n", t, w, nPeopleLeft);

	int nSlots = t+1, siz = (N-t)/(t+1), nLargeSlot = (N-t)%(t+1);

	if (!release)
	printf("#slots %d, #small slot %d, #big slot %d, small-big slot size (%d, %d)\n", nSlots, nSlots-nLargeSlot, nLargeSlot, siz, siz+1);

	int sizSlotLast = nPeopleLeft <= nLargeSlot ? siz+1 : siz;
	if (!release)
	printf("Slot size for last person %d\n", sizSlotLast);

	minmax.first = sizSlotLast/2;
	minmax.second = sizSlotLast%2==0 ? sizSlotLast/2-1 : sizSlotLast/2;
	
	if (!release)
	{
		if (sizSlotLast%2==0)
			printf("max, min [%d %d] \n", sizSlotLast/2, sizSlotLast/2-1);
		else
			printf("max, min [%d %d] \n", sizSlotLast/2, sizSlotLast/2);
	}
}

int main()
 {
	if (release)
	{
		// freopen("C-small-1-attempt0.in", "r", stdin);
		// freopen("C-small-1-attempt0.out", "w", stdout);

		freopen("C-small-2-attempt0.in", "r", stdin);
		freopen("C-small-2-attempt0.out", "w", stdout);
		
		// freopen("B-large.in", "r", stdin);
		// freopen("B-large.out", "w", stdout);

		int tt, tn; 
		cin >> tn;
		int N, K;

		F1(tt,tn) 
		{
			cin >> N; cin >> K;
			pair<int, int> minmax;
			util(N, K, minmax);

			printf("Case #%d: %d %d\n", tt, minmax.first, minmax.second);
		}
	}
	else
	{
		int N = 4, K = 2;
		pair<int, int> minmax;
		util(N, K, minmax);

	}

	return 0;
}