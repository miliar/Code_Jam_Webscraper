#include <iostream>
#include <vector>
#include <string>
#include <ostream>
#include <algorithm>
#include <iterator>
#include <array>
#include <set>
#include <cassert>
#include <iomanip>

using namespace std;

template <class T> 
std::ostream& operator<<(std::ostream& os, const vector<T>& X)
{
	for (const auto& x : X)
		os << x << " ";
	return os;
}

int main() 
{
	long T;
	cin >> T;
    cout << setprecision(10);

	for (long t = 0; t < T; ++t)
	{
		cout << "Case #" << t+1 << ": ";
		long D; 
        long N;
        cin >> D >> N;
        vector<long> P(N);
        vector<long> S(N);
        double mayortiempo = 0;
        for (int w = 0; w < N; ++w)
        {
            cin >> P[w] >> S[w];
            double tiempoquetardara = double(D-P[w])/S[w];
            if (tiempoquetardara > mayortiempo)
                mayortiempo = tiempoquetardara;
        }
        cout << double(D)/mayortiempo << endl;
        
	}
	
	return 0;
}
