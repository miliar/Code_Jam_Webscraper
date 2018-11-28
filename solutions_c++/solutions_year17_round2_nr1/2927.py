#include <iostream>

using namespace std;

double doCase()
{
	int destination;
	int horses;
	cin >> destination;
	cin >> horses;

	double minEta = -1;

	for (int n = 0; n < horses; ++n)
	{
		int initialPos;
		int speed;
		cin >> initialPos;
		cin >> speed;

		double eta = (destination - initialPos) / (double) speed;
		if (minEta < 0 || eta > minEta)
			minEta = eta;
	}

	return (double) destination / (double)minEta;
}

void main()
{
	int cases;
	cin >> cases;

	for (int n = 0; n < cases; ++n)
	{
		double result = doCase();
		cout << "Case #" << n + 1 << ": " << fixed <<  result << endl;
	}

	//system("pause");
}