#include "stdio.h"
struct MyStruct
{
	int up;
	int down;
	double value;
};
int main()
{
	int t;
	scanf("%d", &t);

	for (int tc = 0; tc < t; tc++)
	{
		printf("Case #%d: ", tc + 1);

		int D, N;
		scanf("%d %d", &D, &N);

		int map[10001] = { 0 };

		MyStruct max;
		max.down = 0;
		max.up = 0;
		max.value = 0;
		for (int i = 0; i < N; i++)
		{
			int kj = 0;
			int mj = 0;
			scanf("%d %d", &kj, &mj);
			MyStruct temp;
			temp.up = (D - kj);
			temp.down = mj;
			temp.value = (float)temp.up / (float)temp.down;
			if (max.value < temp.value)
				max = temp;
		}
		float r = (((float)max.down * (float)D) / (float)max.up);

		printf("%.6f\n", r+0.0000005);
	}
}