#include <iostream>
#include <string>
#include <string.h>
#include <cstdlib>
#include <cstdio>
#include <cfloat>
#include <vector>
#include <fstream>
#include <time.h>
#include <math.h>
#include <algorithm>


using namespace std;

pair<long long int,long long int> stalls(long long int n, long long int k)
{
	long long int next2_f,next2_s;
	pair<int,int> myints[1];
	if(n%2 == 0)
	{
		myints[0] = {make_pair((n/2)-1,n/2)};
	}
	else
	{
		myints[0] = {make_pair((n/2),n/2)};
	}
	std::vector<pair<int,int> > v(myints,myints+1);

  	std::make_heap (v.begin(),v.end());
  	
  	for(int l = 1; l < k; l++)
  	{
  		next2_f = v.front().first;
		next2_s = v.front().second;
		std::pop_heap (v.begin(),v.end()); v.pop_back();
		if(next2_f%2 == 0)
		{
			v.push_back(make_pair((next2_f/2)-1,next2_f/2)); std::push_heap (v.begin(),v.end());
		}
		else
		{
			v.push_back(make_pair((next2_f/2),next2_f/2)); std::push_heap (v.begin(),v.end());
		}
		if(next2_s%2 == 0)
		{
			v.push_back(make_pair((next2_s/2)-1,next2_s/2)); std::push_heap (v.begin(),v.end());
		}
		else
		{
			v.push_back(make_pair((next2_f/2),next2_f/2)); std::push_heap (v.begin(),v.end());
		}
	}
	return (v.front());
}

int main()
{
 	int t;
	long long int n,k;
	pair<long long int, long long int> required;
	fstream f1,f2;
	f2.open("output.txt", ios::in|ios::out|ofstream::trunc);
	f1.open("input.txt",ios::in|ios::out);
	f1>>t;
	for(int i = 0; i < t; i++)
	{
		f1>>n>>k;
		required = stalls(n,k);
		f2<<"Case #"<<i+1<<": "<<required.second<<" "<<required.first<<endl;
	}

	f2.close();
	f1.close();
	
  	std::cout << '\n';

}
