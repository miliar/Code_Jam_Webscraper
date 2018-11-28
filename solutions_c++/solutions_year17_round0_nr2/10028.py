#include <iostream>

// forward declarations
bool tidyCheck(unsigned long long int i);
unsigned long long int findPrevTidy(unsigned long long int i);

void tidycheck_problem()
{
	unsigned long long int numProblems = 0;
	std::cin >> numProblems;

	for (int i = 0; i < numProblems; i++) {
		unsigned long long int num;
		std::cin >> num;
		unsigned long long int solution = findPrevTidy(num);

		std::cout << "case #" << i + 1 << ": " << solution << std::endl;
	}
}

unsigned long long int findPrevTidy(unsigned long long int i)
{
	while (!tidyCheck(i)) {
		i--;
	}

	return i;
}

bool tidyCheck(unsigned long long int i)
{
	unsigned long long int x = i % 10;// get ones place
	i /= 10;			// remove ones place

	while (i != 0) {	// if i is a single digit, loop doesn't proceed
		unsigned long long int y = i % 10;	// get next number
		i /= 10;		// remove from number
		if (x < y)		// if ones place is less than next, not a tidy number
			return false;
		else
			x = y;		// prepare for next loop iteration
	}

	return true;
}

int main()
{
	tidycheck_problem();

	return 0;
}