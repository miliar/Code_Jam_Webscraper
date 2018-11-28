#include <stack>
#include <iostream>
#include <string>
#include <vector>
#include <cstddef>
#include <algorithm>
#include <iomanip>   

using namespace std;

int digitCount(double A)
{
	int b = (int)A, k = b, counter = 0;
	while(b != 0 )
	{
		k = b%10;
		b = b/10;
		counter++;
	}
	return counter;

}
int main()
{
	double T, counter = 1;
	cin >> T ;

	while(T != 0 )
	{
		double D, N;
		cin >> D >> N;
		double max = 0;

		while( N != 0)
		{
			N--;
			double speed = 0, start;
			cin >> start >> speed;

			double left = D - start;
			double TimeTaken = left / speed;
			if( TimeTaken >= max)
			{
				max = TimeTaken;
			}
		}

		double mySpeed = D / max;

       cout << noshowpoint << "Case #" <<counter++<<": ";
       cout  << showpoint << setprecision(digitCount(mySpeed) + 6)<< mySpeed << endl;
		T--;
	}
	return 0;
}