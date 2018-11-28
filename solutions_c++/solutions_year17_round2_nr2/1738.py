#include <cstdlib>
#include <iostream>
#include "vector"
#include <string>
#include <fstream>
#include <iomanip>

using namespace std;

string majo = "";



int getMax(vector<int> all)
{
	int max = all[1], max_index = 1, i;
	for( i = 2; i < all.size(); i++)
	{
		if(all[i] > max)
		{
			max = all[i];
			max_index = i;
		}

	}

	if(max_index == 1)
		majo = majo + "R";
	else if(max_index == 3)
		majo = majo + "Y";
	else if(max_index == 5)
		majo = majo + "B";
	return max_index;
}

vector<int> getArray(int maxLen)
{
	vector<int> vect;
	int i = 0;


	while(i < maxLen)
	{
		int count;
		cin >> count;
		vect.push_back(count);
		i++;
	}

	return vect;
}

//
// to print a vector
//
void printVector(vector<int> a)
{
  for (size_t i = 0;  i < a.size();  i++) 
  {
    cout << a[i] << " ";
  }
  cout << endl;
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
  	majo = "";
  	count++;
    Tests--;
    vector<int> all = getArray(7);
    int red = all[1], blue = all[5], yellow = all[3], total = all[0], max = 0;
    vector<int> temp;

    if(red > blue + yellow || blue > red + yellow || yellow > red + blue)
   	{
    	output << "Case #" << count << ": "<< "IMPOSSIBLE" << endl;
    	total = 0;
   	}

    while(total)
    {
    	temp = all;
    	if(max)
    		temp[max] = 0;
    	max = getMax(temp);
    	all[max] = all[max] - 1;
    	//printVector(all);
    	total--;


    }
    if(majo != "")
    {
    	if(majo[majo.length() - 1] == majo[0])
    	{
    		char temp = majo[majo.length() - 1];
    		majo[majo.length() -  1] = majo[majo.length() - 2];
    		majo[majo.length()- 2] = temp;
    	}
    	output << "Case #" << count << ": "<< majo << endl;
    }
  }
}