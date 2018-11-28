// ConsoleApplication96.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <queue>
#include <vector>
#include <list>
#include <iostream>
#include <set>
using namespace std;

struct emptyslot
{
	int left;
	int right;
	int val;
	int idx;
};

class SlotCompare
{
public:
	bool operator() (emptyslot S1, emptyslot S2)
	{
		if (S1.val == S2.val)
		{
			return S1.left > S2.left;
		}
		else
		{
			return S1.val < S2.val;
		}
	}
};



void fillSlots(int N, int k, int &y, int &z, int tc)
{
	y = -1, z = -1;
	std::priority_queue<emptyslot, std::vector<emptyslot>, SlotCompare> pq;

	vector<int> slotsList(N + 2);
	vector<int> leftSlots(N + 2);
	vector<int> rightSlots(N + 2);

	leftSlots.assign(N + 2, -1);
	rightSlots.assign(N + 2, -1);

	slotsList[0] = 1;
	slotsList[N + 1] = 1;

	emptyslot e{ 1, N, N, 0 };

	pq.push(e);

	int finalIndex = -1;

	for (int i = 0; i < k; i++)
	{
		emptyslot nextSlot = pq.top();
		pq.pop();

		int maxSize = nextSlot.val;
		int maxIdx = nextSlot.idx;

		int slotIdx = -1;
		int l = nextSlot.left;
		int r = nextSlot.right;
		if (maxSize % 2 == 0)
		{
			slotIdx = (l + r - 1) / 2;
		}
		else
		{
			slotIdx = (l + r - 1) / 2 + 1;
		}

		slotsList[slotIdx] = 1;

		finalIndex = slotIdx;

		// insert two slots to left and right of index
		if (l <= (slotIdx - 1))
		{
			emptyslot leftSlot{ l, slotIdx - 1, slotIdx - 1 - l + 1, maxIdx };
			pq.push(leftSlot);
		}

		if ((slotIdx + 1) <= r)
		{
			emptyslot rightSlot{ slotIdx + 1, r, r - slotIdx, maxIdx + 1 };
			pq.push(rightSlot);
		}
	}

	{
		int* ls = (int *)malloc((N + 2) * sizeof(int));
		ls[0] = -1;
		ls[N + 1] = -1;
		int* rs = (int *)malloc((N + 2) * sizeof(int));
		rs[0] = -1;
		rs[N + 1] = -1;
		int* minlsrs = (int *)malloc((N + 2) * sizeof(int));
		minlsrs[0] = -1;
		minlsrs[N + 1] = -1;
		int* maxlsrs = (int *)malloc((N + 2) * sizeof(int));
		maxlsrs[0] = -1;
		maxlsrs[N + 1] = -1;

		// check each slot
		//for (int s = 1; s <= N; s++)
		int s = finalIndex;
		{
			minlsrs[s] = -1;
			maxlsrs[s] = -1;

			// occupied
			//if (slotsList[s] == 1)
			//	continue;

			int l = 0;
			for (int p = s - 1; p >= 0; p--)
			{
				if (slotsList[p] == 1)
					break;
				l++;
			}

			int r = 0;
			for (int p = s + 1; p < N + 2; p++)
			{
				if (slotsList[p] == 1)
					break;
				r++;
			}

			ls[s] = l;
			rs[s] = r;
			z = std::min(l, r);
			y = std::max(l, r);
		}

		cout << "Case #" << tc << ": " << y << " " << z << "\n";
	}
}

int main()
{
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		int N, k;
		int y, z;
		cin >> N >> k;
		fillSlots(N, k, y, z, i);
	}

    return 0;
}

