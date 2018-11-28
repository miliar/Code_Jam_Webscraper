#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <algorithm>
using namespace std;

struct Result
{
public:
	int max;
	int min;
};

struct Stall
{
public:
	bool used;
	int Ls;
	int Rs;
};


Result Bathroom(int aN, int aK);
Result Bathroom2(int aN, int aK);

int main()
{
	ifstream inputFile("input.txt");
	ofstream outputFile("output.txt");
	
	int T;
	int N;
	int K;

	inputFile >> T;
	for(int i = 0; i < T; i++)
	{
		inputFile >> N >> K;

		Result result = Bathroom2(N, K);

		outputFile << "Case #" << i+1 << ": " << result.max << " " << result.min << endl;
		
	}

	return 0;
}

Result Bathroom2(int aN, int aK)
{
	Result result;
	result.min = aN;
	result.max = -1;

	int* countAdjacentRoom = new int[aN+1];
	countAdjacentRoom[aN] = 1;
	memset(countAdjacentRoom, 0, aN * sizeof(int) );

	int maxAdjacentRoomIndex = aN;
	for(int i = 0; i < aK ; i++)
	{

		int maxAdjacentRoom = countAdjacentRoom[ maxAdjacentRoomIndex ];
		int min;
		int max;

		if( maxAdjacentRoomIndex % 2 == 0)
		{
			min = maxAdjacentRoomIndex/2 - 1;
			max = maxAdjacentRoomIndex/2;	
		}
		else
		{
			min = maxAdjacentRoomIndex/2;
			max = maxAdjacentRoomIndex/2;
		}

		countAdjacentRoom[min]++;
		countAdjacentRoom[max]++;

		countAdjacentRoom[ maxAdjacentRoomIndex ]--;

		if (countAdjacentRoom[ maxAdjacentRoomIndex ] == 0 )
		{
			while(maxAdjacentRoomIndex >= 0 && countAdjacentRoom[ maxAdjacentRoomIndex ] == 0)
				maxAdjacentRoomIndex--;
		}

		if(i == aK - 1)
		{
			result.min = min;
			result.max = max;
		}		
	}

	return result;
}

Result Bathroom(int aN, int aK)
{
	 Result result;
	 result.min = aN;
	 result.max = -1;

	 //initialize
	 Stall* stalls = new Stall[aN];
	 for(int i = 0; i < aN; i++)
	 {
		 stalls[i].used = false;
		 stalls[i].Ls = i-0;
		 stalls[i].Rs = aN - i - 1;
	 }

	 for(int i = 0; i < aK; i++)
	 {
		  int maxIndex = -1;
		  int maxmin = -1;
		  int maxmax = -1;
		  //compute min -> max
		  for(int j = 0; j < aN; j++)
		  {
			  if(stalls[j].used == false)
			  {
				  if(min(stalls[j].Ls, stalls[j].Rs) > maxmin)
				  {
						maxIndex = j;
						maxmin = min(stalls[j].Ls, stalls[j].Rs);
						maxmax = max(stalls[j].Ls, stalls[j].Rs);
				  }
				  else if(min(stalls[j].Ls, stalls[j].Rs) == maxmin)
				  {
					    if(max(stalls[j].Ls, stalls[j].Rs) > maxmax)
						{
							 maxIndex = j;
							 maxmin = min(stalls[j].Ls, stalls[j].Rs);
							 maxmax = max(stalls[j].Ls, stalls[j].Rs);
						}
				  }
			  }
		  }

		  //update
		  stalls[maxIndex].used = true;
		  int index = maxIndex - 1;
		  while( index >= 0 && stalls[index].used == false)
		  {
			  stalls[index].Rs = maxIndex - index - 1;
			  index--;
		  }


		  index = maxIndex + 1;
		  while( index < aN && stalls[index].used == false)
		  {
			  stalls[index].Ls = index - maxIndex - 1;
			  index++;
		  }

		  if(i == aK - 1)
		  {
			  result.max = maxmax;
			  result.min = maxmin;
		  }
	 }

	 return result;
}