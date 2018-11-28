#include <iostream>
#include <queue>

using namespace std;

struct Interval
{
	int x,y;
};

bool operator<(Interval a,Interval b)
{
	if (a.y-a.x < b.y-b.x) return true;
	if (a.y-a.x == b.y-b.x && a.x>b.x) return true;
	return false;
}



int t,n,k;

void solve(int c)
{
	priority_queue<Interval> q;
	q.push({0,n+1});
	Interval p;
	int x,y,m;
	for (;k>0; k--)
	{
		p=q.top();
        q.pop();
		m=(p.y+p.x)/2;
		q.push({p.x,m}); q.push({m,p.y});
//		cout << p.x << " " << m << " " << p.y << endl;
	}
	cout << "Case #" << c << ": " << max(m-p.x,p.y-m)-1 << " " << min(m-p.x,p.y-m)-1 << endl;
}

int main()
{
	cin >> t;

	for (int i=1; i<=t; i++)
	{
		cin >> n >> k;
		solve(i);
	}

//	Interval p1={1,4};
//	q.push(p1);
//	q.push((Interval){1,4});
//	q.push((Interval){4,7});

/*
	while (!q.empty())
	{
		cout << q.top().x << " " << q.top().y << endl;
		q.pop();
	}
*/


}
