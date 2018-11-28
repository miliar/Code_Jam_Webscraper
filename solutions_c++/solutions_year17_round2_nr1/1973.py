#include <iostream>
#include <vector>
#include <iomanip>


using namespace std;


int main() 
{
	std::cin.sync_with_stdio(false);
	int T;
	cin >> T;
	cout << fixed << setprecision(6);
	for (int c = 0; c<T; ++c)
	{
		int D, N;
		cin >> D >> N;
		double v, x;
		double tmax = 0;
		for (int i=0; i<N; ++i)
		{
			cin >> x >> v;
			double t = (D-x)/v;
			if (t > tmax)
				tmax = t;
		}
		
		cout << "Case #" << c+1 << ": ";
		cout << D/tmax << endl;
	}
	

}
