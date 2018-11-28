#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <climits>
#include <queue>
#include <utility>
#include <set>
#include <bitset>
#include <stdio.h>

using namespace std;

struct compare {
  bool operator() (pair<int,int> const & lhs, pair<int,int> const & rhs) const
  {
  	if(lhs.first==rhs.first)
    	return lhs.second<rhs.second;
	else
		return lhs.first>rhs.first;
  }
};

int main(int argc, char const *argv[])
{
	int t;
	cin>>t;
	for (int i = 1; i <= t; ++i)
	{
		long long n,k;
		cin>>n>>k;
		long long ls,rs;
		long long l=0;
		set<pair<long,long>,compare> myqueue;
		myqueue.insert(make_pair(n,1));
		while(l<k)
		{
			int curr_n = myqueue.begin()->first;
			int index = myqueue.begin()->second;
			myqueue.erase(myqueue.begin());
			if(curr_n==0)
				continue;
			if (curr_n%2!=0)
			{
				ls=(curr_n-1)/2;
				rs=(curr_n-1)/2;
				myqueue.insert(make_pair(ls,index));
				myqueue.insert(make_pair(ls,index+ls+1));
			}
			else{
				ls=(curr_n/2-1);
				rs=(curr_n/2);
				myqueue.insert(make_pair(ls,index));
				myqueue.insert(make_pair(rs,index+ls+1));
			}
			l++;
		}
		cout<<"Case #"<<i<<": "<<max(ls,rs)<<" "<<min(ls,rs)<<endl;
	}
	return 0;
}