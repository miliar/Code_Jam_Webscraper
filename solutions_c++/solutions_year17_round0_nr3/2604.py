#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef unsigned long long int ulli;


typedef struct {
	pair<ulli, ulli> lower;
	pair<ulli, ulli> upper;	
} holder;

holder get_onlayer(holder o, ulli pow2)
{
	//cout << "DEBUG: pow2=" << pow2 << " lower=" << o.lower.first << "," << o.lower.second << " upper=" << o.upper.first << "," << o.upper.second << endl;


	if (pow2 == 1ll)
		return o;

	ulli a1, a2, a3, a4;
	a1 = (o.lower.first - 1) / 2ll;
	a2 = (o.lower.first - 1) - a1;
	a3 = (o.upper.first - 1) / 2ll;
	a4 = (o.upper.first - 1) - a3;
	
	holder p;
	p.lower.first = min({a1, a2, a3, a4});	p.lower.second = 0;
	p.upper.first = max({a1, a2, a3, a4});	p.upper.second = 0;
	
	if (a1 == p.lower.first)
		p.lower.second += o.lower.second;
	else
		p.upper.second += o.lower.second;

	if (a2 == p.lower.first)
		p.lower.second += o.lower.second;
	else
		p.upper.second += o.lower.second;

	if (a3 == p.lower.first)
		p.lower.second += o.upper.second;
	else
		p.upper.second += o.upper.second;

	if (a4 == p.lower.first)
		p.lower.second += o.upper.second;
	else
		p.upper.second += o.upper.second;

	return get_onlayer(p, pow2 / 2ll);
}


void solve_test_case(int case_num)
{
	ulli n, k;
	cin >> n >> k;

	ulli tail = 0ll, pow2 = 1ll;
	while (tail + pow2 < k){
		tail += pow2;
		pow2 *= 2ll;
	}

	ulli pos = k - tail;

	holder o;
	o.lower.first = n;	o.lower.second = 1;
	o.upper.first = n;	o.upper.second = 0;

	holder p = get_onlayer(o, pow2);

	ulli frlast;
	if (pos <= p.upper.second)
		frlast = p.upper.first;
	else
		frlast = p.lower.first;

	ulli ls = (frlast - 1) / 2ll;
	ulli rs = (frlast - 1) - ls;

	cout << "Case #" << case_num << ": " << max(ls, rs) << " " << min(ls, rs) << "\n";
}

int main()
{
//	std::ios::sync_with_stdio(false);

	int test_count;
	scanf("%d", &test_count);
	for (int t = 1; t <= test_count; t++)
		solve_test_case(t);

	return 0;
}
