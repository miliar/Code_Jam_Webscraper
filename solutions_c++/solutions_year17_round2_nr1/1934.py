#include <cstdlib>
#include <iostream>
#include "vector"
#include <string>
#include <fstream>
#include <iomanip>

using namespace std;

    double D,N;
//
// to print a vector
//
void printVector(vector<double> a)
{
  for (size_t i = 0;  i < a.size();  i++) 
  {
    cout << a[i] << endl;
  }
}

//
//
//
double getArray()
{
	vector<double> vect;
	int i = 1;

	double dist, speed, time, max;
	cin >> dist >> speed;
	dist = D - dist;
	time = dist/speed;
	max = time;

	while(i < N)
	{
		cin >> dist >> speed;
		dist = D - dist;
		time = dist/speed;
		if(max < time)
			max = time;
		i++;
	}

	return max;
}

//
// main function
//
int main()
{
	ofstream output;
  output.open("Horses.txt");
  int Tests, count = 0; // Counting which test case
  string pancakes = "";
  cin >> Tests; // Taking input

  while(Tests != 0)
  {
  	count++;
    Tests--;
    cin >> D >> N;
    double all = getArray();
    output << fixed;
    output << "Case #" << count << ": "<< setprecision(6)<<  D/all << endl;
  }

}
