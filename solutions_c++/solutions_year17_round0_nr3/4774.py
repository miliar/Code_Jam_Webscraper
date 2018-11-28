#include <bits/stdc++.h>
using namespace std;
void Calculate(long long n,long long k,int testcase)
{
	priority_queue<long long> Queue;
	long long part1, part2, max, min;
	Queue.push(n);
	for(long long j=0;j<k;j++)
	{
		long long largest = Queue.top();
		Queue.pop();
		part1 = largest/2;
		part2 = largest - 1 - part1;
		Queue.push(part1);
		Queue.push(part2);
	}
	
	if(part1 > part2)
	{
		max = part1;
		min = part2;
	}
	else
	{
		max = part2;
		min = part1;
	}
	
	cout<<"Case #"<<testcase<<": "<<max<<" "<<min<<endl;

}
int main()
{
	int t,i = 0;
	cin>>t;
	while(i<t)
	{
		long long n,k;
		cin>>n>>k;
		Calculate(n,k,++i);
	}
	return 0;
}
