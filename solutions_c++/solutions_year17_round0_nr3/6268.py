#include<bits/stdc++.h>
#define f first
#define s second
using namespace std;

typedef pair<int,int> par;
typedef pair<par,int> para;
priority_queue<para, vector<para>, less<para> > q;

ifstream goo;
ofstream gle;

void solve()
{
	int n,k,a,b,c,d;
	para p;
	goo>>n>>k;
	while(!q.empty()) q.pop();
	a=(n+1)/2;
	q.push(para(par(a,n-a+1), a));
	for(int i=1; i<k; i++)
	{
		p=q.top();
		q.pop();
		a=p.s;
		b=a-p.f.f;
		c=a+p.f.s;
		d=(a+b)/2;
		q.push(para(par(d-b,a-d), d));
		d=(a+c)/2;
		q.push(para(par(d-a,c-d), d));
	}
	p=q.top();
	gle<<p.f.s-1<<" "<<p.f.f-1<<"\n";
	return;
}

int main()
{
	goo.open("C:\\Users\\Mateusz\\Desktop\\Testy\\C-small-2-attempt1.in");
	gle.open("C:\\Users\\Mateusz\\Desktop\\Testy\\tak.out");
	int t;
	goo>>t;
	for(int i=1; i<=t; i++)
	{
		gle<<"Case #"<<i<<": ";
		solve();
	}
	goo.close();
	gle.close();
	return 0;
}
