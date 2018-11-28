#include <iostream>
#include <cstdint>
#include <queue>

struct stall
{
	uint64_t position; // our stall number, treating the first non-guard stall as index 1
	uint64_t dLeft; // distance to next left occupied stall, is 1 when neighbour is occupied
	uint64_t dRight; // dist to right occupied

	friend bool operator<(const stall& l, const stall& r)
	{
		auto lLims = std::minmax(l.dLeft, l.dRight);
		auto rLims = std::minmax(r.dLeft, r.dRight);
		if (lLims.first != rLims.first) // compare mins
			return lLims.first < rLims.first;
		else if (lLims.second != rLims.second) // compare max
			return lLims.second < rLims.second;
		else // compare position
			return l.position < r.position;
	}
};

stall posBetween(uint64_t left, uint64_t right)
{
	// no overflow avg for the large dataset
	uint64_t pos = (left >> 1) + (right >> 1) + (left & right & 0x1);
	return { pos, pos - left, right - pos };
}

stall fillStalls(uint64_t n, uint64_t k)
{
	std::priority_queue<stall> insertPoints;
	insertPoints.emplace(posBetween(0, n+1));
	stall stallTaken;
	while (k > 0)
	{
		stallTaken = insertPoints.top();
		insertPoints.pop();
		if(stallTaken.dLeft > 1) // if an empty stall exists between the one we just took and its neighbour, add a possible insertion point
			insertPoints.emplace(posBetween(stallTaken.position - stallTaken.dLeft, stallTaken.position));
		if (stallTaken.dRight > 1)
			insertPoints.emplace(posBetween(stallTaken.position, stallTaken.position + stallTaken.dRight));
		--k;
	}
	return stallTaken;
}

int main()
{
	uint64_t t, n, k;
	std::cin >> t;
	for (uint64_t i = 1; i <= t; ++i)
	{
		std::cin >> n >> k;
		stall res = fillStalls(n, k);
		std::cout << "Case #" << i << ": " 
			<< std::max(res.dLeft, res.dRight) -1 << " " // Our alg defines dist differently from google, fix up
			<< std::min(res.dLeft, res.dRight) -1 << std::endl;
	}
    return 0;
}