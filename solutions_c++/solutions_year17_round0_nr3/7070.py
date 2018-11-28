#include<fstream>
#include<string>
#include<sstream>
#include<iostream>
#include<math.h>
#include<iomanip>
#include<queue>
#include<map>
using namespace std;
//typedef map<int,map<int,int>> mmap;


class StallStat
{
public:
    int lower;
	int upper;

	int size;

	int chosen;
	int minscore;
	int maxscore;

	StallStat(int l, int up)
	{
		lower = l;
		upper = up;
		size = (upper - lower)  +1;
		calculate();
	}


	void calculate()
	{
		int mid = (upper + lower) / 2;
		bool odd = size%2 ==1;
		chosen = mid;
		minscore = mid - lower;
		maxscore = odd? minscore : (upper-mid);
	}

	bool operator <(const StallStat& other) const
	{
		return size < other.size;
	}
};


int main ()

{
	string ifile = "input.txt", ofile = "output.txt";
	ifstream input;
	input.open(ifile);
	stringstream ss;
	int cases;
	input>>cases;
	for(int c = 1; c <= cases; ++c)
	{
		int n,k;
		input>>n>>k;
		std::priority_queue<StallStat> stall;
		StallStat initial = StallStat(1, n);
	    stall.push(initial);
		bool *stallcheck = new bool[n+2];
		stallcheck[0] = true;
		stallcheck[n+1]=true;
		for(int i = 1;  i < (n+2); i++) 
			stallcheck[i] = false;
		int min,max;
		if (n == k)
		{
			min = 0, max =0;
		}
		else
		{
			for(int j = 0 ; j < k ; ++j)
			{
				vector<StallStat> options;
				StallStat first = stall.top();
				options.push_back(first);
				stall.pop();
				StallStat *chosen = NULL;
				//remove all of same size.

				while (stall.size() > 0 && stall.top().size == first.size)
				{
					options.push_back(stall.top());
					stall.pop();
				}

				//now we have everything of the same size. min, max as they should be the same.  then take the min low of the items in there
				for(std::vector<StallStat>::iterator it = options.begin(); it != options.end(); ++it) 
				{
					if(!chosen) 
						chosen = &(*it);
					else
					{
						if(chosen->lower > it->lower)
							chosen = &(*it);
					}
				}
				for(std::vector<StallStat>::iterator it = options.begin(); it != options.end(); ++it) 
				{
					if(chosen->lower != it->lower)stall.push(*it);
				}
				stallcheck[chosen->chosen] = true;
				StallStat right(chosen->lower, (chosen->chosen-1));
				StallStat left ((chosen->chosen+1 ), chosen->upper);
				if(right.size > 0)stall.push(right);
				if(left.size > 0)stall.push(left);
				min = chosen->minscore;
				max = chosen->maxscore;
			}
		}
		ss<<"Case #"<<c<<": "<<max<<" " <<min << "\n";
		delete [] stallcheck;
	}
	input.close();
	ofstream output;
	output.open(ofile);
	output<<ss.rdbuf();
	output.flush();
	output.close();
	return 0;
}	