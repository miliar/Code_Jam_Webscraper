#include<iostream>
#include<vector>
#include<algorithm>
#include<queue>

struct range_t
{
	long long from;
	long long to;
	long long range;

	
	range_t( long long mFrom, long long mTo )
	{
		from = mFrom;
		to = mTo;
		range = (from+to)/2;
	}
	range_t()
	{}
};

bool operator < ( range_t a, range_t b )
{
	return a.to-a.from < b.to-b.from;
}

void Bathroom( long long n, long long k )
{
	long long from = 0;
	long long to = n-1;
	std::priority_queue< range_t > ranges;
	range_t first( from, to );
	ranges.push( first );
		
	for( long long i=0;i<k-1;i++ )
	{

		range_t cur = ranges.top();
		ranges.pop();
		
		range_t newRange1( cur.from, cur.range-1);
		range_t newRange2( cur.range+1, cur.to );
		if( newRange1.to - newRange1.from >= 0 )
			ranges.push( newRange1 );
		if( newRange2.to - newRange2.from >= 0 )
			ranges.push( newRange2 );

	}
	range_t fin = ranges.top();
	long long mid = fin.range;
	long long ls = mid-fin.from;
	long long rs = fin.to-mid;
	std::cout<<std::max(ls, rs)<<" "<<std::min(ls, rs)<<std::endl;
}

int main()
{
	int times;
	std::cin>>times;
	for( int i=0;i<times;i++ )
	{
		long long n, k;
		std::cin>>n>>k;
		std::cout<<"Case #"<<i+1<<": ";
		Bathroom( n, k );
	}
}
