#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>
#include <map>


// https://code.google.com/codejam/contest/dashboard?c=3264486#s=p2


typedef unsigned long my_type;

struct TSitInfo
{
	my_type nSitPos;
	my_type Ls,Rs;
	TSitInfo()
	{
		nSitPos = 0;
		Ls = Rs = 0;
	}
	TSitInfo(const my_type prev, const my_type next)
	{
		nSitPos = (next+prev)/2;
		assert(nSitPos>prev);
		Ls = nSitPos-prev-1;
		assert(next>nSitPos);
		Rs = next-nSitPos-1;
	}
	/*
	temp.nSitPos = mid;
	temp.Ls = mid-nCheckPos-1;
	temp.Rs = next-mid-1;
	*/
	my_type left() const
	{
		return nSitPos-Ls-1;
	}
	my_type right() const
	{
		return Rs+nSitPos+1;
	}
	bool operator < (const TSitInfo& rhs) const
	{
		// this means that the best sit will be last
		return IsOtherBetter(rhs);
	}
	// return true if the other sit is better than this one
	bool IsOtherBetter(const TSitInfo& other) const
	{
		{
			my_type myMin = std::min(Ls,Rs);
			my_type otherMin = std::min(other.Ls,other.Rs);

			if (myMin > otherMin)
				return false;
			if (myMin < otherMin)
				return true;
		}

		{
			my_type myMax = std::max(Ls,Rs);
			my_type otherMax = std::max(other.Ls,other.Rs);

			if (myMax > otherMax)
				return false;
			if (myMax < otherMax)
				return true;
		}

		return other.nSitPos < nSitPos;

		
	}
};

class CStalls
{	
	std::map<TSitInfo, my_type> mapFreeSits;
public:
	CStalls(my_type nFreeStalls)
	{
		TSitInfo info(0,nFreeStalls+1);
		mapFreeSits[info] = info.nSitPos;
	}
	TSitInfo SitPeople(my_type nTotalPeople)
	{
		TSitInfo info;
		for (my_type nCurPerson = 0; nCurPerson< nTotalPeople; ++nCurPerson)
			info = SitSinglePerson();
		return info;
	}
private:
	
	TSitInfo SitSinglePerson()
	{
		TSitInfo bestSit;
		// take the best sit from the back
		std::map<TSitInfo, my_type>::iterator lastIt = mapFreeSits.end();
		lastIt--;
		bestSit = lastIt->first;
		mapFreeSits.erase(lastIt);

		if (bestSit.Ls>0)
		{
			TSitInfo leftSit(bestSit.left(), bestSit.nSitPos);
			mapFreeSits[leftSit] = leftSit.nSitPos;
		}
		
		if (bestSit.Rs > 0)
		{
			TSitInfo rightSit(bestSit.nSitPos, bestSit.right());
			mapFreeSits[rightSit] = rightSit.nSitPos;
		}
		

		return bestSit;
	}

};

int main()
{
	
	int nTests;
	std::cin >> nTests;
	for (int nCase =0 ; nCase < nTests; ++nCase)
	{				
		my_type N, K;
		std::cin >> N;
		std::cin >> K;

		CStalls stalls(N);
		TSitInfo sitInfo = stalls.SitPeople(K);

		my_type maxLR = std::max(sitInfo.Ls, sitInfo.Rs);
		my_type minLR = std::min(sitInfo.Ls, sitInfo.Rs);
								
		std::cout<<"Case #"<<nCase+1<<": "<<maxLR<<" "<<minLR<<std::endl;
								
	}

	return 0;
}
