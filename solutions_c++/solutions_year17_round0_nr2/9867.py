#include <fstream>
#include <string>
#include <cmath>

using namespace std;

int lastTidyNumber(string lastNumberIn);

int main()
{
	ifstream inStream;
	inStream.open("B-small-attempt8.in");
	ofstream outStream;
	outStream.open("B-solution.out");

	if (inStream.is_open())
	{
		string inputLine;
		getline(inStream, inputLine);
		int inputlength = stoi(inputLine);
		for(int j = 0; j < inputlength; j++)
		{
			getline(inStream, inputLine);
			outStream << "Case #" << j + 1 << ": " << lastTidyNumber(inputLine) << endl;
		}
		inStream.close();
		outStream.close();
	}
}

int lastTidyNumber(string lastNumberIn)
{
	int orderOfMagnitude = lastNumberIn.length() - 1;
	int lastNumber = stoi(lastNumberIn);

	for (int i = (orderOfMagnitude - 1); i >= 0; i--)
	{
		int lowerOrder = fmod((lastNumber / pow(10, i)), 10);
		int higherOrder = fmod((lastNumber / pow(10, i + 1)), 10);

		if (lowerOrder < higherOrder)
		{
			lastNumber = trunc((lastNumber / pow(10, i + 1)))*pow(10, i + 1) - 1;
			i = orderOfMagnitude;
		}
	}

	return lastNumber;
}