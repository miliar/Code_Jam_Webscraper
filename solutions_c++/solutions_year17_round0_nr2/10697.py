/* This program is a solution to the tidy numbers problem in Google code Jam Qualification round'2017
 *
 * AUTHOR: SHATROOPA SAXENA
 * DATE  : 9th APRIL'2017
 */

//Header files
#include<iostream>


//user defined functions
bool isTidy(long int number)
{
	/* @params
	 *
	 * param number: input number
	 *
	 * Description: This function returns true if 'number' is a tidy number, else it returns false
	 */
	int next = number % 10;		// to keep track of the next digit
	int x; 				//keep track of current digit
	
	number = number / 10;
	while(number > 0)
	{
		x = number % 10;
		if(x > next)
			return false;
		number = number / 10;
		next = x;
	}
	return true;
}

//main method
int main()
{
	//input variables
	int numberOfTestCases;		//number of test cases
	long int n;			//count uptil n

	//auxillary variables
	int test = 1;			//particular test case

	std::cin >> numberOfTestCases;
	
	while(test <= numberOfTestCases)
	{	
		//output variables
		long int largestTidyNumber;

		//take input
		std::cin >> n;
		largestTidyNumber = n;

		while(largestTidyNumber > 0)
		{
			if(isTidy(largestTidyNumber))
				break;
			largestTidyNumber--;
		}


		//print output
		std::cout << "Case #" << test << ": " << largestTidyNumber << std::endl;
		//proceed to next test case
		test++;
	}	
}
