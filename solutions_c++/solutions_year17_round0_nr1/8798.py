#include <iostream>
#include <deque>
#include <set>
#include <string>
#include <stdlib.h>

using namespace std;

class node
{
public:
	string s;
	int d;

	node(string ss, int dd)
	{
		this->s = ss;
		this->d = dd;
	}
};

bool checkHappy(string s)
{
	for(int i=0; i<s.size(); i++)
	{
		if(s[i] == '-')
			return false;
	}
	return true;
}

void flip(string &s, int k, int pos)
{
	for(int i = pos; i < pos + k; i++)
	{
		if(s[i] == '+')
			s[i] = '-';
		else
			s[i] = '+';
	}
}

int calcMin(string s, int k)
{
	deque<node> q;
	set<string> visited;
	node n(s, 0);
	q.push_back(n);
	visited.insert(s);
	// cout<< n.s << " " << n.d << endl;
	while(q.size() > 0)
	{
		n.s = q[0].s;
		n.d = q[0].d;
		q.pop_front();
		if(checkHappy(n.s))
		{
			return n.d;
		}
		int i;
		int len = s.size();
		for(i = 0; i <= len-k; i++)
		{
			node np(n.s, n.d+1);
			flip(np.s, k, i);
			if(visited.count(np.s) == 0)
			{
				q.push_back(np);
				visited.insert(np.s);
				// cout<< np.s << " " << np.d << endl;
			}
		}
	}
	return -1;
}

int main()
{
	int T;
	string S;
	int K;
	cin >> T;
	for(int t = 0; t < T; t++)
	{
		cin >> S >> K;
		int min = calcMin(S, K);
		if(min < 0)
		{
			cout<< "Case #" << t+1 << ": IMPOSSIBLE"<< endl;
		}
		else
		{
			cout<< "Case #" << t+1 << ": " << min << endl;
		}
	}
	return 0;
}