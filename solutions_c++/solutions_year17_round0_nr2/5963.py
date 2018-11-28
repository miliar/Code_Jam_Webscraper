#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <cmath>
#include <cstdlib>
using namespace std;  // since cin and cout are both in namespace std, this saves some text

// Prototypes
string nearestTidyNumber(string n);
void printArray(int array[], int numDigits);
int decrementArray (int digit, int numDigits, int array[]);
void splitNumber(string n, int array[], int numDigits);


int main() {
  int t;
  string n;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  
  for (int i = 1; i <= t; ++i) {
    cin >> n;  // read n from the input
    cout << "Case #" << i << ": " << nearestTidyNumber(n) << endl;
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }

  return 0;
}


string nearestTidyNumber(string n) {
	int numDigits = n.size(); // Calculate the size in digits
	// cout << "Num digits: " << numDigits << endl;

	if (numDigits == 1) return n; // Easy case for single digit numbers

	// Define a new array here
	// cout << "Split digit: ";
	int splitN [numDigits]; // Same size as number of digits in number

	splitNumber(n, splitN, numDigits); // Split the number into an array

	// printArray(splitN, numDigits);

	int digitCount = 0; // Start at the first digit


	while (digitCount < numDigits-1) {
		
		if (splitN[digitCount] <= splitN[digitCount + 1]) // Check the digits are correct
		{
			digitCount += 1; // Increment the digit
		}
		else
		{
			digitCount = decrementArray(digitCount, numDigits, splitN); // Decrement the array
		}
		// printArray(splitN, numDigits);

	}

	string output = "";
	for (int i = 0; i < numDigits; ++i)
	{
		// cout << splitN[i];
		if (i == 0 && splitN[0] == 0)
		{
			// do nothing
		}
		else 
		{
			output += to_string(splitN[i]);
		}
		
	}

	return output;
}


void printArray(int array[], int numDigits) {
	cout << "Current Array state: ";
	for (int i = 0; i < numDigits; ++i)
	{
		cout << array[i] << " ";
	}
	cout << endl;
}


void splitNumber(string n, int array[], int numDigits) {
	
	for (int i = 0; i < numDigits; i++)
	{
		array[i] = (int) (n[i] - '0');
	}
}



int decrementArray (int digit, int numDigits, int array[])
{
	int testN;
	if (digit == 0) // First digit
	{
		array[digit] -= 1; // Decrement by 1
		for (int i = (digit + 1); i < numDigits; ++i)
		{
			array[i] = 9; // Set the array to 9's
		}
		return 0;
	}
	else 
	{
		// Decrement the value
		testN = array[digit-1] * 10 + array[digit] - 1;
		array[digit-1] = testN / 10;
		array[digit] = testN % 10;
		for (int i = digit+1; i < numDigits; ++i)
		{
			array[i] = 9; // Set the rest of the array to 9's
		}

		return digit - 1; // Return the digit decremented
	}
}


