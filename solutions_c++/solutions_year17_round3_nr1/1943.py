#include <iostream>
#include <functional>
#include <string>
#include <map>
#include <cmath>
#include <algorithm>
#include <vector>
#include <iomanip>
#include <math.h>

using namespace std;

#define debug cout

#define ll long long int

#define fori(n) for(int i = 0; i < n; i++)
#define forj(n) for(int j = 0; j < n; j++)
#define fork(n) for(int k = 0; k < n; k++)

#define forri(n) for(int i = n - 1; i >= 0; i--)
#define forrj(n) for(int j = n - 1; j >= 0; j--)
#define forrk(n) for(int k = n - 1; k >= 0; k--)
	
#define fori2(s,n) for(int i = s; i < n; i++)
#define forj2(s,n) for(int j = s; j < n; j++)
#define fork2(s,n) for(int k = s; k < n; k++)

#define forit(v) for(auto it = v.begin(); it != v.end(); it++)
#define forrit(v) for(auto it = v.rbegin(); it != v.rend(); it++)

#define M_PI           3.14159265358979323846 

int N, K;
ll R[1000], H[1000];
bool taken[1000];

ll side(ll rad, ll height)
{
	return 2 * rad * height;
}

ll surface(ll rad)
{
	return rad * rad;
}

ll add_surface(ll rad, ll max_rad)
{
	return rad * rad - max_rad * max_rad;
}

ll max_rad() 
{
	ll max = 0;

	fori(N)
		if (taken[i])
			if (max < R[i])
				max = R[i];

	return max;
}

int remove() 
{
	ll worst = 10000000000000;
	ll current = 0;
	ll max_r = max_rad();

	int pos = 0;

	fori(N) {
		if (taken[i]) {
			current = side(R[i], H[i]);

			if (max_r == R[i]) {
				taken[i] = false;
				current += add_surface(R[i], max_rad());
				taken[i] = true;
			}

			if (current < worst)
			{
				worst = current;
				pos = i;
			}
		}
	}

	return pos;
}

void RunInstance()
{
	cin >> N >> K;

	fori(N) {
		cin >> R[i] >> H[i];
		taken[i] = true;
	}

	fori(N-K)
	{
		taken[remove()] = false;
		
	}

	ll s = surface(max_rad());
	fori(N)
		if (taken[i])
			s += side(R[i], H[i]);

	cout << std::fixed << std::setprecision(9) << (long double)(s)*M_PI;
}	

// ======================================================== //

int main()
{
	int num_of_instances = 0;
	cin >> num_of_instances;

	for (int i = 1; i <= num_of_instances; ++i)
	{
		cout << "Case #" << i << ": ";
		RunInstance();
		cout << endl;
	}
}

