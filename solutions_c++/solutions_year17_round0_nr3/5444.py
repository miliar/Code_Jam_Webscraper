#include <cstdio>
#include <vector>

using namespace std;

int arr[1005];
int min_val[1005];
int max_val[1005];

int get_eligible(int n) {
	int max_value = -1;

	for (int i = 0; i < n+2; ++i)
	{
		if (max_value < min_val[i])
		{
			max_value = min_val[i];
		}
	}

//	printf("max_val1 = %d\n", max_value);

	vector < int > el;

	for (int i = 0; i < n+2; ++i)
	{
		if (min_val[i] == max_value)
		{
			el.push_back(i);
		}
	}

	if (el.size() == 1)
	{
		return el[0];
	}

/*
	for (int i = 0; i < el.size(); ++i)
	{
		printf("%d ", el[i]);
	}
	printf("\n");
*/
	vector < int > el2;
	max_value = -1;
	for (int i = 0; i < el.size(); ++i)
	{
		if (max_value < max_val[el[i]])
		{
			max_value = max_val[el[i]];
		}
	}

/*	printf("max_val2 = %d\n", max_value);

	for (int i = 0; i < el2.size(); ++i)
	{
		printf("%d ", el2[i]);
	}
	printf("\n");

*/	for (int i = 0; i < el.size(); ++i)
	{
		if (max_val[el[i]] == max_value)
		{
			el2.push_back(el[i]);
		}
	}

	return el2[0];
}

void calc_lr(int n) {
	for (int i = 0; i < n+2; ++i)
	{
		if (arr[i] == 1)
		{
			min_val[i] = -1;
			max_val[i] = -1;
			continue;
		}
		int j;
		for (j = i-1; j > -1; --j)
		{
			if (arr[j] == 1)
				break;
		}

		int left_space = i - j - 1;

		for (j = i+1; j < n+1; ++j)
		{
			if (arr[j] == 1)
				break;
		}

		int right_space = j - i - 1;
		min_val[i] = min(left_space, right_space);
		max_val[i] = max(left_space, right_space);
	}
/*
	for (int i = 0; i < n+2; ++i)
	{
		printf("%d ", min_val[i]);
	}

	printf("\n");
	for (int i = 0; i < n+2; ++i)
	{
		printf("%d ", max_val[i]);
	}
	printf("\n");
	*/
}

int main(void) {

	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int t, n, k;

	scanf("%d", &t);

	for (int i = 0; i < t; ++i)
	{
		scanf("%d%d", &n, &k);

		for (int j = 0; j < n+2; ++j)
		{
			arr[j] = 0;
		}

		arr[0] = 1;
		arr[n+1] = 1;

		for (int j = 0; j < k-1; ++j)
		{
			calc_lr(n);
			arr[get_eligible(n)] = 1;
			//printf("%d\n", get_eligible(n));

//			for (int l = 0; l < n+2; ++l)
//			{
//				printf("%d ", arr[l]);
//			}
//			printf("\n");
		}

		calc_lr(n);
		int res = get_eligible(n);
		printf("Case #%d: %d %d\n",i+1, max_val[res], min_val[res]);
	}

	return 0;
}