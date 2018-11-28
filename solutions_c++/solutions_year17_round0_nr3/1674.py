#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef unsigned long T;
//typedef int T;

/*
struct node 
{
	T left, right;
	T idx;
	T min, max;

	node(const T _left, const T _right, const T _idx) :
		left(_left), right(_right), idx(_idx), min(std::min(left, right)), max(std::max(left, right)) {
	}

	void update_min_max()
	{
		min = std::min(left, right);
		max = std::max(left, right);
	}

	bool operator<(const node& o) const
	{
		return this->min < o.min || (this->min == o.min && this->max < o.max);
	}
};

struct node_cmp
{
   bool operator()(const node* a, const node* b)
   {
       return *a < *b;
   }
};

inline pair<T, T> solve(T n, T k)
{
	vector<node*> heap(n);
	vector<node*> lut(n);

	for (T i = 0; i < n; ++i)
	{
		T l = i, r = n - i - 1;
		heap[i] = lut[i] = new node(l, r, i);
	}

	T last_max = 0, last_min = 0;

	for (T i_person = 0; i_person < k; ++i_person)
	{
		make_heap(heap.begin(), heap.end(), node_cmp());
		pop_heap(heap.begin(), heap.end());
		node *n0 = heap.back();
		heap.pop_back();
		//cout << n0->max << " " << n0->min << " " << n0->idx << endl;
		last_max = n0->max;
		last_min = n0->min;
		lut[n0->idx] = nullptr;

		for (T i = n0->idx - 1; i >= 0 && lut[i]; i--)
		{
			node* n1 = lut[i];
			n1->right = n0->idx - i - 1;
			n1->update_min_max();
		}
		for (T i = n0->idx + 1; i < (T) lut.size() && lut[i]; i++)
		{
			node* n1 = lut[i];
			n1->left = i - n0->idx - 1;
			n1->update_min_max();
		}

		delete n0;

		//cout << last_max << ' ' << last_min << endl;
	}

	return pair<T, T>(last_max, last_min);
}
*/

inline pair<T, T> solve_fast(T n, T k)
{
	T l = n >> 1, r = (n-1) >> 1;
	if (k == 1)
		return pair<T, T>(l, r);

	if ((k-1) % 2)
		return solve_fast(l, k / 2);
	else
		return solve_fast(r, (k-1) / 2);
	//cout << l << ' ' << r << endl;

	return pair<T, T>(n, k);
}

int main()
{
	int t;
	T n, k;

	cin >> t;
	for (int i = 1; i <= t; ++i) {
		cin >> n >> k;
		pair<T, T> res = solve_fast(n, k);
		cout << "Case #" << i << ": " << res.first << ' ' << res.second << endl;
	}

	/*	
	T n = 12;
	for (T k = 1; k <= n; ++k)
	{
		pair<T, T> res = solve_fast(n, k);
		cout << k << ' ' << res.first << ' ' << res.second << endl;
	}
	*/

	return 0;
}


/*
25
12 12
6 5
6 5
3 2
3 2
2 2
2 2
1 1
1 1
1 0
1 0
1 0
1 0
1 0
1 0
0 0
0 0
0 0
0 0
0 0
0 0
0 0
0 0
0 0
0 0

12
6 5
3 2
2 2
1 1
1 0
1 0
1 0
0 0
0 0
0 0
0 0
0 0

6
3 2
1 1
1 0
0 0
0 0
0 0

5
2 2
1 0
1 0
0 0
0 0
*/
