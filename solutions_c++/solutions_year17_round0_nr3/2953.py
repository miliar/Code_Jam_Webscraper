#include <cstdlib>
#include <iostream>
#include "vector"
#include <string>
#include <fstream>
#include <queue>  
#include <map> 

using namespace std;


//
// main function
//
int main()
{
  long long int Tests, count = 0; // Counting which test case
  cin >> Tests; // Taking input
  
  ofstream output; 
  output.open("bathroomOutput.txt"); // ouput file

  while(Tests != 0) // while tests are over
  {
  	count++;
  	Tests--;
  	queue<long long int> mainQueue; // contains the main queue
  	map<long long int, long long int> mainMap;

  	long long int size = 0, people = 0, min = 0, max = 0;
  	cin >> size >> people;

  	//mainVector.push_back(size);
  	mainQueue.push(size); // first putting the size on the queue
  	mainMap[size] = 1; // mapping it

  	while(people) // till there people exists to put in bathrooms
  	{
  		long long int quotient = mainQueue.front(); // taking the front out of queue
  		mainQueue.pop();

  		if(quotient % 2 == 1)
  		{
  			//cout << "pushing odd " << quotient/2 << endl;
  			min = quotient/2;
  			max = quotient/2;
  		}
  		else
  		{
  			max = quotient/2;
  			if(quotient/2 != 0)
  				min = (quotient/2) - 1;
  		}

  		if(people - mainMap[quotient] >= 0) // checking if they can skip computations
  		{
  			if(min != max)
  			{
  				if(mainMap[max] == 0)
  				{
  					mainQueue.push(max);
  					cout << "pushed " << max <<endl;
  				}
  				if(mainMap[min] == 0)
  				{
  					mainQueue.push(min);
  					cout << "pushed " << min << endl;
  				}

  				mainMap[max] += mainMap[quotient];
				mainMap[min] += mainMap[quotient];

				people = people - mainMap[quotient];

			}

			else
			{
				if(mainMap[max] == 0)
  				{
  					mainQueue.push(max);
  					cout << "pushed " << max << endl;
  				}

				mainMap[max] += mainMap[quotient]*2;

				people = people - mainMap[quotient];

			}
  		}

  		else
  			people = 0;

  	}

  	output << "Case #" << count << ": " << max << " " << min << endl;

  }
}

//  certain bathroom has N + 2 stalls in a single row; the stalls on the left and right ends are permanently occupied by the bathroom guards. The other N stalls are for users.

// Whenever someone enters the bathroom, they try to choose a stall that is as far from other people as possible. To avoid confusion, they follow deterministic rules: For each empty stall S, they compute two values LS and RS, each of which is the number of empty stalls between S and the closest occupied stall to the left or right, respectively. Then they consider the set of stalls with the farthest closest neighbor, that is, those S for which min(LS, RS) is maximal. If there is only one such stall, they choose it; otherwise, they choose the one among those where max(LS, RS) is maximal. If there are still multiple tied stalls, they choose the leftmost stall among those.

// K people are about to enter the bathroom; each one will choose their stall before the next arrives. Nobody will ever leave.

// When the last person chooses their stall S, what will the values of max(LS, RS) and min(LS, RS) be?

// Solving this problem

// This problem has 2 Small datasets and 1 Large dataset. You must solve the first Small dataset before you can attempt the second Small dataset. You will be able to retry either of the Small datasets (with a time penalty). You will be able to make a single attempt at the Large, as usual, only after solving both Small datasets.

// Input

// The first line of the input gives the number of test cases, T. T lines follow. Each line describes a test case with two integers N and K, as described above.

// Output

// For each test case, output one line containing Case #x: y z, where x is the test case number (starting from 1), y is max(LS, RS), and z is min(LS, RS) as calculated by the last person to enter the bathroom for their chosen stall S.

// Limits

// 1 ≤ T ≤ 100.
// 1 ≤ K ≤ N.
// Small dataset 1

// 1 ≤ N ≤ 1000.
// Small dataset 2

// 1 ≤ N ≤ 106.
// Large dataset

// 1 ≤ N ≤ 1018.