#include<iostream>
#include<string>
#include<cmath>
#include<math.h>
#include<map>
#include<vector>
#include<algorithm>
using namespace std;

typedef unsigned long long ull;

void recursion(ull num , ull cur_level , ull final_level , map<ull,ull> &m )
{
	if(cur_level == final_level)
	{
		//insert in map
		if(m.find(num) != m.end())
		{
			m[num]++;
		}
		else
		{
			m.insert(make_pair(num , 1));
		}
		return;
	}

	ull part1 , part2;
	if(num%2 == 0)
	{
		part1 = num/2-1;
		part2 = num/2;
	}
	else
	{
		part1 = num/2;
		part2 = num/2;
	}

	recursion(part1  , cur_level +1 , final_level , m);
	recursion(part2  , cur_level +1 , final_level , m);
}

int main()
{
	int t,case_num=1;
	cin>>t;

	while(t--)
	{
		ull num , k;
		cin>>num>>k;
		if(num == k)
		{
			cout<<"Case #"<<case_num++<<": "<<"0 0"<<"\n";
			continue;
		}
		map<ull , ull> m;
		ull level = log((double) k)/log(2.0);
		ull temp = pow(2,(double) level) - 1;
		temp = k - temp;
		recursion(num  , 0, level , m );

		map<ull,ull> ::  reverse_iterator it ;
		ull answer = 0;
		for(it = m.rbegin() ; it != m.rend() ; ++it)
		{
			ull x = it->second;
			if(temp <= x)
			{
				answer = it->first;
				break;
			}
			temp -= x;
		}

		ull l,r;
		if(answer%2 == 0)
		{
			l = answer/2-1;
		}
		else
		{
			l = answer/2;
		}
		r=answer/2;
		if(l<r)
		{
			swap(l,r);
		}
		cout<<"Case #"<<case_num++<<": "<<l<<" "<<r<<"\n";
	}
	return 0;
}