#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <math.h>
#include <memory.h>
#include <sstream>
#include <deque>
const int pi=acos(-1);
typedef long long ll;
using namespace std;
int t,j=1;
int main(){
	#ifndef ONLINE_JUDGE
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	#endif
	cin>>t;
	while(t--)
	{
		int n,k,temp;
		cin>>n>>k;
		priority_queue<int>q;
		q.push(n);
		for(int i=0;i<k;i++)
		{
			int x=q.top();
			q.pop();
			if(x%2)
			{
				q.push(x/2);
				q.push(x/2);
			}
			else
			{
				q.push(x/2);
				q.push(x/2-1);
			}
			temp=x;
		}
		if(temp%2)
			cout<<"Case #"<<j++<<": "<<temp/2<<" "<<temp/2<<endl;
		else
			cout<<"Case #"<<j++<<": "<<temp/2<<" "<<temp/2-1<<endl;
	}
	return 0;
}