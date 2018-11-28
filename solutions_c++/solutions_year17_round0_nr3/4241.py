#include <cstdio>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <queue>
#include <fstream>

typedef long long ll;

#define REP(i,a) for(int i=0;i<a;++i)

using namespace std;

string s;
ifstream cinf;
ofstream coutf;

void createS(ll n, ll k)
{
	if(k==1)
	{
		if (n%2==1)
		    coutf << n/2 << " " << n/2 << endl;
		else
			coutf << n/2 << " " << ((n/2-1)>=0 ? (n/2-1) : 0)  << endl;
		return;
	}
	priority_queue<int> q;
	int top;
	if(n%2==1)
	{
		q.push(n/2);
	    q.push(n/2);
	}
	else
	{
		q.push(n/2);
		q.push(n/2-1);
	}
    k--;
	while(k-1>0)
	{
		top = q.top();
		q.pop();
		if(top%2==1)
		{
			q.push(top/2);
			q.push(top/2);
		}
		else
		{
			q.push(top/2);
			q.push(top/2-1);
		}
		k--;
	}
	int op = q.top();
	if (op%2==1)
		coutf << op/2 << " " << op/2 << endl;
	else
		coutf << op/2 << " " << ((op/2-1)>=0 ? (op/2-1) : 0)  << endl;
}



int main() {
	int T;
	ll N, K;

    cinf.open("A-small.in.txt");
	coutf.open("A-small.out.txt");

	cinf >> T;
	for (int ri = 1; ri <= T; ++ri) {
		cinf >> N >> K;
        coutf << "Case #" << ri << ": ";
        createS(N, K);
	}
	return 0;
}

