#include <cstdio>
#include <map>

struct MyPair {
	long long _max, _min;
	MyPair( long long n ) {
		Set( n / 2, n / 2 - (1 - n % 2) );
	}
	MyPair(long long a, long long b) {
		Set( a, b );
	}
	inline bool operator<(const MyPair& rhs) const { return _min > rhs._min || (_min == rhs._min && _max > rhs._max); }
	inline bool operator==(const MyPair& rhs) const { return _min == rhs._min && _max == rhs._max; }
	inline long long Max() const { return _max; }
	inline long long Min() const { return _min; }
	inline void Set( long long a, long long b ) {
		if( a > b ) {
			_max = a; _min = b;
		} else {
			_max = b; _min = a;
		}
	}
};

typedef std::map<MyPair, long long>			 		MyMap;
typedef std::map<MyPair, long long>::const_iterator MyMapCIter;

MyPair solve( long long n, long long k ) {
	long long cur = 0;
	MyMap m;
	m[MyPair(n)] = 1;
	while( true ) {
		MyMapCIter it = m.cbegin();
		long long curCnt = it->second;
		cur += curCnt;
		MyPair curPair(it->first);
		if(cur >= k) {
			 return curPair;
		}
		m.erase(it);
		
		m[MyPair(curPair.Max())] += curCnt;
		m[MyPair(curPair.Min())] += curCnt;
	}
}

int main() {
	int T;
	long long K, N;
	scanf("%d", &T);
	for( int i = 1; i <= T; i++ ) {
		scanf( "%lld %lld", &N, &K );
		MyPair p( solve( N, K ) );
		printf( "Case #%d: %lld %lld\n", i, p.Max(), p.Min() );
	}
	return 0;
}
