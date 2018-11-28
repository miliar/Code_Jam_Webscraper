#include<iostream>
#include<algorithm>
using namespace std;

double arr[1010];
double dt[1010];
int main()
{
	freopen("input.in", "r+", stdin);
	freopen("output.out", "w+", stdout);
	int T;
	scanf("%d", &T);
	int count = 1;
	while (T--)
	{
		int D, H;double Max = 0;
		scanf("%d %d", &D, &H);
		for (int i = 0; i < H; i++)
		{
			scanf("%lf %lf", &dt[i], &arr[i]);
			dt[i] = (double)(D - dt[i])/arr[i];
			if (dt[i] > Max)
				Max = dt[i];
		}
		printf("Case #%d: %.8lf\n",count++, D / Max);
	}

}