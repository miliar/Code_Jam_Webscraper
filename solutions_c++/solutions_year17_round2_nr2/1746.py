#include <bits/stdc++.h>
using namespace std;
struct node
{
	int col, no;
};
bool compare(node &n1, node &n2)
{
	return n1.no > n2.no;
}
char map_col[] = {'R', 'O', 'Y', 'G', 'B', 'V'};
bool arr[][6] = {{false, false, true, true, true, false},
				{false, false, false, false, true, false},
				{true, false, false, false, true, true},
				{true, false, false, false, false, false},
				{true, true, true, false, false, false},
				{false, false, true, false, false, false}};
int permutation[1005];
bool is_possible(int n, int i, int col[])
{
	if(i == n)
		return true;
	bool flag[6];
	for(int j = 0; j < 6; j++)
		flag[j] = (col[j] > 0);
	int prev = (i + n - 1) % n, next = (i + 1) % n;
	if(permutation[prev] != -1)
		for(int j = 0, c = permutation[prev]; j < 6; j++)
			flag[j] = flag[j] & arr[c][j];
	if(permutation[next] != -1)
		for(int j = 0, c = permutation[next]; j < 6; j++)
			flag[j] = flag[j] & arr[c][j];
	vector<node> v;
	node temp;
	for(int j = 0; j < 6; j++)
		if(flag[j])
			temp.col = j, temp.no = col[j], v.push_back(temp);
	sort(v.begin(), v.end(), compare);
	for(int j = 0; j < v.size(); j++)
	{
		temp = v[j];
		col[temp.col]--;
		permutation[i] = temp.col;
		if(is_possible(n, i + 1, col))
			return true;
		col[temp.col]++;
		permutation[i] = -1;
	}
	return false;
}
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int t;
	cin >> t;
	for(int ii = 1; ii <= t; ii++)
	{
		int n, col[6];
		bool flag = true;
		cin >> n >> col[0] >> col[1] >> col[2] >> col[3] >> col[4] >> col[5];
		for(int i = 0; i < n; i++)
			permutation[i] = -1;
		cout << "Case #" << ii << ": ";
		for(int i = 0; i < 6 && flag; i++)
		{
			int this_col = col[i], sum = 0;
			for(int j = 0; j < 6; j++)
				if(arr[i][j])
					sum += col[j];
			if(sum < this_col)
				flag = false;
		}
		if(!flag || !is_possible(n, 0, col))
			cout << "IMPOSSIBLE";
		else
			for(int i = 0; i < n; i++)
				cout << map_col[permutation[i]];
		cout << "\n";
	}
	return 0;
}
