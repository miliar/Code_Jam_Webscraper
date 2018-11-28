#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <queue>

using namespace std;

unsigned long _max;
unsigned long _min;

struct Interval 
{
    unsigned long start_;
	unsigned long end_;
    unsigned long vacant_left;
	unsigned long vacant_right;
	unsigned long max_;
	unsigned long min_;
	
	Interval (unsigned long left, unsigned long right)
	{
		start_ = left;
		end_ = right;
		unsigned long n = right - left + 1;
		
		if (n % 2 == 0)
		{
			vacant_left = n/2 - 1;
			vacant_right = n/2;
		}
		else
		{
			vacant_left = n/2;
			vacant_right = n/2;
		}
		
		max_ = std::max (vacant_left, vacant_right);
		min_ = std::min (vacant_left, vacant_right);
	
	    //cout << "Created interval: " << start_ << ";" << end_ << ";" << vacant_left << ";" << vacant_right << ";" << max_ << ";" << min_ << endl;
	
	}
};

class Compare
{
public:	
	bool operator ()(Interval a, Interval b)
	{
		if (a.min_ != b.min_)
		{
			return (a.min_ < b.min_);
			
		}else
		{
			if (a.max_ != b.max_)
			{
				return (a.max_ < b.max_);
			}
			else
			{
				return (a.start_ < b.start_);
			}
		}
	}
};
	
priority_queue <Interval, std::vector<Interval>, Compare > queue_;

void divide_partition ()
{
	Interval to_be_divided = queue_.top ();
	queue_.pop ();
	
	if (to_be_divided.vacant_left > 0)
	{
		Interval interval_left (to_be_divided.start_, to_be_divided.start_ + to_be_divided.vacant_left-1);
		queue_.push (interval_left);
	}
	
	if (to_be_divided.vacant_right > 0)
	{
		Interval interval_right (to_be_divided.end_ - to_be_divided.vacant_right + 1, to_be_divided.end_);
		queue_.push (interval_right);
	}
}

void start (unsigned int n)
{
	Interval interval (1, n);
	queue_.push (interval);
}

void iterate (unsigned int k, unsigned int n)
{
	//cout << "K:" << k << ";N" << n << endl;
	start (n);
	for (int j=1;j < k;j++)
	{
		divide_partition ();	
	}
	_max = queue_.top().max_;
	_min = queue_.top().min_;
}

int main (int argc, char* argv[])
{
   unsigned int n; 
   cin >> n;
   for (unsigned int i=0;i<n;i++)  
   { 
      unsigned long n, k;
      cin >> n >> k;
	  queue_ = priority_queue <Interval, std::vector<Interval>, Compare > ();
	  iterate (k, n);
	  cout << "Case #"<< i+1 <<":" << " " << _max << " " << _min << endl;
   }
}
