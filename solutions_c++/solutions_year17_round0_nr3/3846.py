#include <iostream>
#include <algorithm>
#include <set>
#include <cmath>
using namespace std;
typedef unsigned long long ull;

struct Stall
{
	ull id, ls, rs;
	bool operator<(const Stall &other) const
	{
		if (min(ls,rs) != min(other.ls,other.rs))
			return min(ls,rs) > min(other.ls,other.rs);
		else if (max(ls,rs) != max(other.ls,other.rs))
			return max(ls,rs) > max(other.ls,other.rs);
		return id < other.id;
	} 
	void print() {cout << id << " " << ls << " " << rs << endl;}
	Stall(ull id, ull ls, ull rs) : id(id), ls(ls), rs(rs) {}
};

void simulate(ull n, ull k, ull &y, ull &z)
{
	set<Stall> pq;
	ull id = ceil(n/2.0);
	pq.insert(Stall(id, id-1, n-id));
	for (int i = 0; i < k-1; ++i)
	{
		const Stall &s = *(pq.begin());
		ull s_id = s.id;
		ull s_ls = s.ls;
		ull s_rs = s.rs;
		pq.erase(pq.begin());
		if (s_ls != 0)
		{
			ull left_id = s_id - s_ls/2 - 1;
			ull left_ls = left_id - s_id + s_ls;
			ull left_rs = s_id - left_id - 1;
			pq.insert(Stall(left_id, left_ls, left_rs));
		}
		if (s_rs != 0)
		{
			ull right_id = s_id + ceil(s_rs/2.0);
			ull right_ls = right_id - s_id - 1;
			ull right_rs = s_id + s_rs - right_id;
			pq.insert(Stall(right_id, right_ls, right_rs));
		}
	}
	const Stall &s = *(pq.begin());
	y = max(s.ls, s.rs);
	z = min(s.ls, s.rs);
}

int main()
{
	int numTests;
	cin >> numTests;
	for (int t = 1; t <= numTests; ++t)
	{
		ull n,k;
		cin >> n >> k;
		ull y,z;
		simulate(n,k,y,z);
		cout << "Case #" << t << ": " << y << " " << z << endl;
	}	
}