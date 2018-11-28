#include <cstdlib>
#include <iostream>
#include "vector"
#include <string>
#include <fstream>

using namespace std;

 		int c,r;

vector<char> getArray(int maxLen)
{
	vector<char> vect;
	int i = 0;

	string ran;
	cin >> ran;


	while(i < maxLen)
	{
		vect.push_back(ran[i]);
		i++;
	}

	return vect;
}

//
// to print a vector
//
void printVector(vector<vector<char> > matrix)
{

}


vector<vector<char> > fillUp(vector<vector<char> > matrix, int row, int col)
{
	char temp = matrix[row][col];
	int i;
	if(temp != '?')
	{
		for(i = row + 1; i < r; i++)
		{
			if(matrix[i][col] != '?')
				break;

			matrix[i][col] = temp;
		}

		for(i = row - 1; i >= 0; i--)
		{
			if(matrix[i][col] != '?')
				break;

			matrix[i][col] = temp;
		}
	}
	return matrix;
}

vector<vector<char> > fillUpAgain(vector<vector<char> > matrix, int row, int col)
{
	char temp = matrix[row][col];
	int i;
	if(temp != '?')
	{
		for(i = col + 1; i < c; i++)
		{
			if(matrix[row][i] != '?')
				break;

			matrix[row][i] = temp;
		}

		for(i = col - 1; i >= 0; i--)
		{
			if(matrix[row][i] != '?')
				break;

			matrix[row][i] = temp;
		}
	}

	return matrix;
}
//
// main function
//
int main()
{
	ofstream output;
  output.open("cakesOutput.txt");
  int Tests, count = 0; // Counting which test case
  string pancakes = "";
  cin >> Tests; // Taking input

  while(Tests != 0)
  {
  	count++;
    Tests--;

    int temp;
    cin >> r >> c;
	  temp = r;

	  vector<vector<char> > matrix;

    while(temp)
    {
    	temp--;
    	matrix.push_back(getArray(c));
    }

    for(int i = 0 ; i < r; i++) //for rows
    {
    	for(int j = 0; j < c; j++) // for columns
    	{
    		matrix = fillUp(matrix, i , j);
    	}
    	//cout << endl;
    }

    for(int i = 0 ; i < r; i++) //for rows
    {
    	for(int j = 0; j < c; j++) // for columns
    	{
    		matrix = fillUpAgain(matrix, i , j);
    	}
    	//cout << endl;
    }

    output << "Case #" << count << ":" << endl;
    
    for(int i = 0 ; i < r; i++) //for rows
    {
    	for(int j = 0; j < c; j++) // for columns
    	{
    		output<< matrix[i][j];
    	}
    	output << endl;
    }

    c = 0;
    r = 0;

  }
  return 0;
 }
