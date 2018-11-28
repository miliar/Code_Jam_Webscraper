/**RootAccess IIT Madras*/
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <map>
#include <set>
#include <list>
#include <queue>
#include <stack>

using namespace std;

#define INF 1000000007


int main()
{
	int t;
	cin>>t;
	for(int cas = 1; cas<=t; cas++)
	{
		
		int n,k;
		cin>>n>>k;
		priority_queue<int> q;
		q.push(n);
		int temp, l, r;
		while(k--)
		{
			temp = q.top();
			q.pop();
			if(temp%2==0)
			{
				l = temp/2;
				r = temp/2 -1;
				q.push(temp/2);
				q.push(temp/2-1);
			}
			else
			{
				l = temp/2;
				r = temp/2;
				q.push(temp/2);
				q.push(temp/2);
			}
		}

		cout<<"Case #"<<cas<<": "<<l<<" "<<r<<endl;
	}
}