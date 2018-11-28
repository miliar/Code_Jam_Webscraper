#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#define PANCAKE_SIZE 1000

using namespace std;  // since cin and cout are both in namespace std, this saves some text

// pancake array flip pancake index to flip size
// pancake : pancake state
// index : flip to pancake first index
// flip : flip pancake index
void flipPancake(bool* pancake, int index, int flip)
{
	for (int i = index; i < index + flip; i++)
	{
		pancake[i] = !pancake[i];
	}
}

void main() {
	int t;

	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.

	char input[PANCAKE_SIZE + 1];
	bool pancake[PANCAKE_SIZE + 1];
	int flip;
	bool check, finalCheck;
	int size;
	int result;

	for (int i = 1; i <= t; ++i) {
		cin >> input;  // read n and then m.
		cin >> flip;	// flipable pancake size

		check = true;
		result = 0;

		// save pancake state
		for (int i = 0; i < PANCAKE_SIZE+1; i++)
		{
			if (input[i] == '-') pancake[i] = false;
			else if (input[i] == '+') pancake[i] = true;
			else if (input[i] == 0)
			{
				size = i;
				break;
			}

			check &= pancake[i];
		}

		result = 0;

		if (!check)
		{
			for (int flipIndex = 0; flipIndex < size - flip + 1; flipIndex++)
			{
				if (!pancake[flipIndex])
				{
					flipPancake(pancake, flipIndex, flip);
					result++;
				}
			}
		}

		finalCheck = true;
		for (int flipIndex = 0; flipIndex < size; flipIndex++)
		{
			finalCheck &= pancake[flipIndex];
		}

		cout << "Case #" << i << ": ";   // print result
		
		// impossible case
		if (!finalCheck) cout << "IMPOSSIBLE" << endl;
		else			  cout << result << endl;
	}
}