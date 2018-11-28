#include<bits/stdc++.h>
using namespace std;
# define ll long long
# define mod 1000000007
# define MAX 1000011
int main()
{
	ifstream in("file/a.txt");
	ofstream out("file/b.txt");
	/*ifstream in("file/d.txt");*/
	/*ofstream out("file/c.txt");*/
	cin.sync_with_stdio(false);
	int var = 0, t;
	ll n, k, steps, ans, left, right, num;
	in >> t;
	while (t--)
	{
		var++;
		set <ll> st, filler;
		map <ll, ll> cnt;
		set <ll> ::iterator R;
		out << "Case #" << var << ": ";
		in >> n >> k;
		cnt[n] = 1;
		steps = 1;
		st.insert(n);
		k--;
		while (k >= steps)
		{
			filler.clear();
			cout << k << ' ' << steps << '\n';
			cout << "Numbers:\n";
			for (R = st.begin(); R != st.end(); R++) {
				num = *R;
				cout << num << ' ' << cnt[num] << '\n';
				left = (num - 1) / 2;
				right = num / 2;
				if (left == right) {
					filler.insert(left);
					cnt[num] += cnt[num];
					cnt[left] += cnt[num];
				}
				else {
					filler.insert(left);
					filler.insert(right);
					cnt[left] += cnt[num];
					cnt[right] = cnt[num];
				}
			}
			cout << "---END---\n";
			k -= steps;
			steps += steps;
			st.clear();
			for (R = filler.begin(); R != filler.end(); R++)
				st.insert(*R);
		}
		k++;
		cout << k << '\n';
		for (R = st.begin(); R != st.end(); R++)
			cout << *R << ' ' << cnt[*R] << '\n';
		if (st.size() == 1) {
			R = st.end();
			R--;
			num = *R;
			if (k == 0)
				out << num << ' ' << num << '\n';
			else{
				left = (num - 1) / 2;
				right = num / 2;
				out << max(left, right) << ' ' << min(left, right) << '\n';
			}
		}
		else {
			R = st.end();
			R--;
			right = *R;
			R--;
			left = *R;
			if (k == 0)
				out << max(right,left) << ' ' << min(left,right) << '\n';
			else {
				if (k <= cnt[right])
					num = right;
				else
					num = left;
				left = (num - 1) / 2;
				right = num / 2;
				out << max(left, right) << ' ' << min(left, right) << '\n';
			}
		}
		cout << "Done: #" << var << '\n';
	}
	return 0;
}