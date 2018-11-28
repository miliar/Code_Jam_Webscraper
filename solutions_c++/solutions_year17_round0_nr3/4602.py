
#include "stdafx.h"


#include <iostream>
#include<string>
#include<fstream>
#include<map>
#include<algorithm>
using namespace std;


bool compare(pair<uint64_t,int> val1, pair<uint64_t, int> val2)
{
	if (val1.first < val2.first)
		return true;
	else 
		return false;

}
int getTimes(uint64_t val)
{
	int times = 0;
	while (val > 0)
	{
		val = val / 2;
		times++;
	}
	return times-1;
}

int main() {
	int t;
	uint64_t n;
	uint64_t k;
	string outputFile = "G:/Code Jam/BathroomStalls/output.txt";
	string inputFile = "G:/Code Jam/BathroomStalls/input.txt";
	ofstream output;
	ifstream input;

	input.open(inputFile);
	output.open(outputFile);
	input >> t;
	int cas = 1;
	
	while (t--)
	{
		map<uint64_t,int> partitions;
		input >> n >> k;
		
		partitions[n] = 1;
		int it = 0;
		int count = 0;
		uint64_t ans;
		bool isFound = false;
		while (true)
		{
			map<uint64_t, int>::reverse_iterator it = partitions.rbegin();
				uint64_t key = (*it).first;
				int nums = (*it).second;
				count = count + nums;

				partitions.erase(key);
				if (count >= k)
				{
					ans = key;
					break;
				}
				else if (key % 2 == 0)
				{
					key = key / 2;
					if (partitions.find(key) == partitions.end())
						partitions[key] = nums;
					else
						partitions[key] += nums;
					key--;
					if (partitions.find(key) == partitions.end())
						partitions[key] = nums;
					else
						partitions[key] += nums;
				}
				else
				{
					key = key / 2;
					if (partitions.find(key) == partitions.end())
						partitions[key] = 2*nums;
					else
						partitions[key] += 2*nums;
				}
			
		}		
		if (ans % 2 == 0)
		{
			output << "Case #"<<  cas << ": " << ans / 2 << " " << (ans / 2)-1 << "\n";
		}
		else
		{
			output << "Case #" <<  cas << ": " << ans / 2 << " " << ans / 2 << "\n";
		}
		cas++;
	}
	input.close();
	output.flush();
	output.close();
	// your code goes here
	return 0;
}

