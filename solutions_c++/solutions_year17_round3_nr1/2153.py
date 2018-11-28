//From code Jam, Problem A. Ample Syrup
#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>
using namespace std;

constexpr long double pi = 3.141592653589793238462643383279502884;

struct pan
{
    long double r;
    long double t;
    long double s;
    pan(long double a,long double b ,long double c) :
        r{ a }, s{ b }, t{ c } {};
    bool operator<(const pan& o) {
	return r > o.r;
    }
};

std::vector< pan > data;
long sz;
long double malus;
long n,k;

long double solve( long idx, long ck )
{
    if( ck > k ) {
	return 0;
    }
    long double best{ 0 };
    while ( idx < sz )
    {
	long double t = solve( idx + 1, ck + 1 ) + data[ idx ].s;
	if( ck > 1 ) {
	    t -= data[ idx ].t;
	}
	if( t > best ) {
	    best = t;
	}
	++idx;
    }
    return best;
}

int main()
{
    long tt;
    cin >> tt;
    for( long t{1} ; t <= tt ; ++t )
    {
	data.clear();
	malus = 0;
	//std::vector< pan > tmp_data;
	cin >> n >> k;
	while( n-- )
	{
	    long double r,h;
	    cin >> r >> h;
	    data.push_back( pan( r, 2 * pi * r * h + r * r * pi , r * r * pi ) );
	}
	std::sort(data.begin(),data.end());
/*	long double last_r{ 0 };
	for( auto&& t_d : tmp_data ) {
	    if( t_d.r != last_r ) {
		data.push_back( t_d );
		last_r = t_d.r;
	    }
	}*/

	sz = data.size();
/*
	for( auto e : data ) {
	    std::cout<<std::setprecision(20)<<e.r<<" "<<e.s<<std::endl;
	}*/

	//solve( 0, 1 , 0 );
	std::cout<<"Case #"<<t<<": "<<std::setprecision(20)<<solve( 0, 1 )<<std::endl;
    }
}
