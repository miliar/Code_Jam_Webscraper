#include <iostream>
#include <vector>

//Problem A

typedef struct {
	long long beginKm;
	long long speed;
} horse_t;

typedef std::vector< horse_t > horses_t;

double getMaxSpeed( const horses_t& horses, long long roadLength )
{
	double maxTime = 0.0d;
	
	for( const auto& horse : horses )
	{
		double thisTime = (double)( roadLength - horse.beginKm ) / (double)horse.speed;
		if( thisTime > maxTime ) maxTime = thisTime;
	}
	
	return (double)roadLength / maxTime;
}

int main()
{
	std::cout.precision(20);
	long long cases;
	std::cin >> cases;
	
	for ( long long i = 1; i <= cases; ++i )
	{
		long long roadLength;
		std::cin >> roadLength;
		long long nHorses;
		std::cin >> nHorses;
		
		horses_t horses( nHorses );
		
		for ( long long j = 0; j < nHorses; ++j )
		{
			std::cin >> horses[j].beginKm >> horses[j].speed;
		}
		
		std::cout << "Case #" << i << ": " << getMaxSpeed( horses, roadLength ) << "\n";
	}
}
