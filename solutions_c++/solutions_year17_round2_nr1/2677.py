#include <cstdint>
#include <list>
#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>
namespace cruise_control
{
double solve( double distance, const std::vector< std::pair< double, double > >& riders )
{
	std::vector< double > times;
	std::transform( std::begin( riders ), std::end( riders )
				  , std::back_inserter( times )
				  , [distance]( auto& rider ) {
						return (distance - rider.first) / rider.second;
				    });
	return distance / *std::max_element(std::begin(times), std::end(times));
}
} // namespace cruise_control

int main()
{
	int cases;
	std::cin >> cases;
	for (int i = 0; i < cases; ++i)
	{
		double distance = 0;
		std::size_t riders = 0;
		std::cin >> distance >> riders;
		std::vector< std::pair< double, double > > riderInfo;
		riderInfo.reserve(riders);
		for (std::size_t j = 0; j < riders; ++j)
		{
			double position = 0;
			double speed = 0;
			std::cin >> position >> speed;
			riderInfo.emplace_back( position, speed );

		}
		std::cout << "Case #" << i + 1 << ": " << std::fixed << std::setprecision(6) << cruise_control::solve( distance, riderInfo ) << std::endl;
	}
}