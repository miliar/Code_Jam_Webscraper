#include <iostream>
#include <string>

using namespace std;
using UInt = unsigned long long int;

int main()
{
	UInt I;
	cin >> I;
	for (UInt i = 0; i < I; ++i)
	{
		UInt N, K;
		cin >> N >> K;
		UInt p(1), M(0);
		while (!(p-1 < K && K <= 2*p-1))
		{
			++M; 
			p *= 2;
		}
		
		UInt res(N-p+1);
		UInt mod(res / p);
		UInt rem(res % p);
		UInt L = (K - (p-1) <= rem) ? mod+1 : mod;
		UInt y = (L % 2 == 0) ? L/2 : (L-1)/2;
		UInt z = (L % 2 == 0) ? L/2-1 : (L-1)/2;
		cout << "Case #" << (i+1) << ": " << y << " " << z << endl;
	}
}
