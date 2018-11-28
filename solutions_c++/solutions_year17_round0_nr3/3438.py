#include <bits/stdc++.h>
#define ll long long
using namespace std;
struct node
{
	ll l, r, len;
};
bool compare(node &n1, node &n2)
{
	return (n1.len < n2.len || (n1.len == n2.len && n1.l > n2.l));
}
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int t;
	vector<node> v;
	cin >> t;
	for(int i = 1; i <= t; i++)
	{
		v.clear();
		node temp;
		ll n, k;
		cin >> n >> k;
		temp.l = 0, temp.r = n - 1, temp.len = n;
		v.push_back(temp), push_heap(v.begin(), v.end(), compare);
		for(int j = 1; j < k; j++)
		{
			temp = v.front();
			pop_heap(v.begin(), v.end(), compare), v.pop_back();
//			cout << temp.l << " " << temp.r << " " << temp.len << "\n";
			ll mid = temp.l + ((temp.r - temp.l) / 2);
//			cout << "Mid = " << mid << "\n\n";
			node temp1, temp2;
			temp1.l = temp.l, temp1.r = mid - 1, temp1.len = temp1.r - temp1.l + 1;
			temp2.l = mid + 1, temp2.r = temp.r, temp2.len = temp2.r - temp2.l + 1;
			if(temp1.len > 0)
				v.push_back(temp1), push_heap(v.begin(), v.end(), compare);
			if(temp2.len > 0)
				v.push_back(temp2), push_heap(v.begin(), v.end(), compare);
		}
		temp = v.front();
		cout << "Case #" << i << ": ";
		ll mid = temp.l + ((temp.r - temp.l) / 2);
		temp.l = mid - temp.l;
		temp.r = temp.r - mid;
		cout << max(temp.l, temp.r) << " " << min(temp.l, temp.r) << "\n";
	}
	return 0;
}
