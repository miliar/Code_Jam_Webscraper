//============================================================================
// Name        : CodeJam_B.cpp
// Author      : Kristiyan Balabanov
// Version     :
// Copyright   : All mine!!!
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <stdio.h>
#include <map>

#define lld long long

using namespace std;

int main()
{
	FILE* f = fopen("out.txt", "w+");
	short cases;
	double max_speed, cand;
	long distance, horses, distI, speedI;

	scanf("%hd", &cases);

	for(short c = 1; c <= cases; ++c)
	{
		max_speed = 10000000000000000.0;
		scanf("%ld %ld", &distance, &horses);

		for(int i = 0; i < horses; ++i)
		{
			scanf("%ld %ld", &distI, &speedI);
			cand = ((double) speedI * distance) / (distance - distI);
			max_speed = (max_speed > cand) ? cand : max_speed;
		}

		fprintf(f, "Case #%hd: %lf\n", c, max_speed);
		//printf("Case #%hd: %.6lf\n", c, max_speed);
	}

	return 0;
}
