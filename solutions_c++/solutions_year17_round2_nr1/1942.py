#include <bits/stdc++.h>
using namespace std;
struct node
{
	int pos, speed;
};
node arr[1005];
bool compare(node &n1, node &n2)
{
	return n1.pos > n2.pos;
}
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int t;
	cin >> t;
	for(int ii = 1; ii <= t; ii++)
	{
		int d, n;
		cin >> d >> n;
		for(int i = 0; i < n; i++)
			cin >> arr[i].pos >> arr[i].speed;
		sort(arr, arr + n, compare);
		double total_time = INT_MIN;
		for(int i = 0; i < n; i++)
		{
			double this_time = (double) (d - arr[i].pos) / arr[i].speed;
			if(this_time > total_time)
				total_time = this_time;
		}
		double speed = d / total_time;
		printf("Case #%d: %.7f\n", ii, speed);
	}
	return 0;
}
