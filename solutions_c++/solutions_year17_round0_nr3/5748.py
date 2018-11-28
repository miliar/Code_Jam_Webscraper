#include <iostream>
#include <cstdlib>
#include <vector>
#include <queue>

typedef unsigned long long ull;
//#define _DEBUG_ 1

void solve_valid(ull *x, ull *y, ull n, ull k)
{
	ull w, v;
	size_t i;
	std::priority_queue<ull> queue;
	queue.push(n);

	// do k - 1 times 
	for(i = 1; i < k; ++i)
	{
		w = queue.top();
		queue.pop();
		v = (w-1)>>0x1;
		queue.push(v);
		queue.push((w-1)-v);
	}

	w = queue.top();
	*y = (w-1)>>0x1;
	*x = (w-1)-*y;
}


/*
 * Build the path to the root and store the ids of the visited nodes 
 * Iterate the way back computing the size of the blocks at the given
 * nodes
 * For 10**18 elements this method needs at most log(10**18)/log(2) 
 * iterations (~60)
 * O(log(k)) where k are the number of people
 * The number of actual stalls has no impact on the performance
 */
void solve(ull *x, ull *y, ull n, ull k)
{
	ull parentid;
	std::vector<ull> parents;
	parentid = k - 1;
	ull value, l, r;
	value = n;

	//
	// Add the path to the root, without adding the root itself 
	//
	while(parentid != 0)
	{
		// Add the current id and compute the id of the parent
		parents.push_back(parentid);
		parentid = (parentid - 1) >> 0x1;
	}

	//
	// Go back from the root to the node computing the value for
	// each traversed node
	//
	for(int i = parents.size() - 1; i >= 0; --i)
	{
		bool is_left = ((parents[i] - 1) >> 0x1) == (parents[i] >> 0x1);
		r = (value - 1) >> 0x1;
		l = (value - 1) - r;
		value = is_left ? l : r;
#ifdef _DEBUG_
		std::cout << value << std::endl;
#endif
	}
	if(value != 0)
	{
		*y = (value-1)>>0x1;
		*x = (value-1)-*y;
	}
	else
	{
		*x = *y = 0;
	}
}


int main(int argc, char **argv)
{
	ull x, y;
#ifndef _DEBUG_
	ull k, n; 
	int t, i;
#endif	
#ifdef _DEBUG_
	solve(&x, &y, 1000, 500);
#else
	std::cin >> t;
	for(i = 1; i <= t; ++i)
	{
		std::cin >> n >> k;
		solve_valid(&x, &y, n, k);
		std::cout << "Case #" << i << ": " << std::max(x, y) << " " << std::min(x, y) << std::endl;
	}
#endif
	return 0;
}
