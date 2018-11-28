//============================================================================
// Name        : CodeJam_Bathroom_Stalls.cpp
// Author      : Kristiyan Balabanov
// Version     :
// Copyright   : All mine!!!
// Description :
//============================================================================

#include <stdio.h>
#include <map>

#define lld long long

using namespace std;

map <lld, lld> openings;
map <lld, lld>::reverse_iterator  mit;

int main()
{
	FILE* f = fopen("out.txt", "w+");
	short cases;
	lld stalls, visitors, left, right;

	scanf("%hd", &cases);

	for(short c = 1; c <= cases; ++c)
	{
		scanf("%lld %lld", &stalls, &visitors);

		openings.clear();
		openings[stalls]++;
		mit = openings.rbegin();

		for(lld i = 0; i < visitors-1; ++i)
		{
			while(!(*mit).second) // check if there are any elements with this key left
				mit++;
			stalls = (*mit).first;
			openings[stalls]--;

			if(stalls <= 1) // there are only single stalls remaining
				break;

			stalls--;

			if(stalls & 1) // odd
			{
				openings[(stalls >> 1) + 1]++;
				openings[stalls >> 1]++;
				//printf("%lld: %lld = %lld + %lld\n", i, stalls, (stalls >> 1) + 1, (stalls >> 1));
			}
			else // even
			{
				openings[stalls >> 1]++;
				openings[stalls >> 1]++;
				//printf("%lld: %lld = %lld + %lld\n", i, stalls, (stalls >> 1), (stalls >> 1));
			}
		}

		while(!(*mit).second) // check if there are any elements with this key left
			mit++;
		stalls = (*mit).first;
		stalls--;
		if(stalls & 1) // odd
		{
			left = (stalls >> 1) + 1;
			right = stalls >> 1;
		}
		else // even
		{
			left = stalls >> 1;
			right = left;
		}

		fprintf(f, "Case #%hd: %lld %lld\n", c, left, right);
		//printf("Case #%hd: %lld %lld\n", c, left, right);
	}

	return 0;
}
