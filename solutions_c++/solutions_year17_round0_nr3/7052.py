#include <iostream>
using namespace std;

int pickStall (int*, int, int, int);
int computeLS(int*, int);
int computeLR(int*, int);

int main()
{
	int numTestCases;
	
	cin >> numTestCases;
	
	int numberStalls;
	int numberPeople;
	
	int stallPicked;

	
	
	for (int i=0; i<numTestCases; i++)
	{
		cin >> numberStalls;
		cin >> numberPeople;

		
		//Array to keep track of which stalls are occupied
		int* stalls = new int[numberStalls+2];
		
		//Initialize array elements
		stalls[0]=1;
		stalls[numberStalls+1]=1;
		
		for (int j=1; j<=numberStalls; j++)
		{
			stalls[j]=0;
		} 
		
		
		int lastPerson = 0;
		for (int k=0; k<numberPeople; k++)
		{
			if (k==numberPeople-1)
			{
				lastPerson = 1;
			}
			stallPicked = pickStall(stalls, numberStalls, lastPerson, i+1);
			stalls[stallPicked] = 1;
		}
		
		
	}
}

int pickStall (int* stallArray, int nStalls, int lPerson, int caseNum)
{
	int ls, lr;
	int currentMinL;
	int totalMinL=-1;
	int indexTotalMinL = -1;
	int currentMaxL = -1;
	int totalMaxL = -1;
	int indexTotalMaxL = -1;
	
	for (int i=0; i<nStalls+2; i++)
	{
		//If stall is unoccupied
		if (stallArray[i]==0)
		{
			//Distance to closest L and R neighbor
			ls = computeLS(stallArray, i);
			lr = computeLR(stallArray, i);
			
			if (ls<lr)
			{
				currentMinL = ls;
				currentMaxL = lr;
			}
			else
			{
				currentMinL = lr;
				currentMaxL = ls;
			}
			
			if (currentMinL > totalMinL)
			{
				totalMinL = currentMinL;
				indexTotalMinL = i;
				totalMaxL = currentMaxL;
				indexTotalMaxL = i;
			}
			else if (currentMinL == totalMinL)
			{
				//choose one in which max(Ls, Rs) is maximal
				if (currentMaxL>totalMaxL)
				{
					indexTotalMinL = i;
					indexTotalMaxL = i;
					totalMinL = currentMinL;
					totalMaxL = currentMaxL;
				}
				else if (currentMaxL==totalMaxL)
				{
					//If those the same, choose leftmost, which means ignore new one since we are going left to right through array
				}

				
			}
		}
	}
	
	if (lPerson)
	{
		cout << "Case #" << caseNum << ": ";
		cout << totalMaxL << " " << totalMinL << "\n";
	}
	return indexTotalMinL;
}

int computeLS(int* stallArray, int currentIndex)
{
	int currentElement = 0;
	int i=0;

	while (currentElement == 0)
	{
		i++;
		currentElement = stallArray[currentIndex-i];

	}
	
	return i-1;
}

int computeLR(int* stallArray, int currentIndex)
{
	int currentElement = 0;
	int i=0;

	while (currentElement == 0)
	{
		i++;
		currentElement = stallArray[currentIndex+i];

	}
	
	return i-1;
}
