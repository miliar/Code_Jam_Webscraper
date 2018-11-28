
/* 
Take yourself as work in progress.
-Bhai
*/

#include<bits/stdc++.h>
using namespace std;

#define M 1000000007
#define LL long long
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define VI vector<int>
#define SZ(a) int(a.size())
#define TR(c, it) for(typeof((c).begin()) it=(c).begin(); it!=(c).end(); it++ )
#define SET(a, b) memset(a, b, sizeof(a))


bool ok(LL n)
{
	LL p = -1;
	while(n)
	{
		LL x = n%10;
		if(p==-1)
			p = x;
		else if(x>p) return false;
		p = x;
		n = n/10;
	}
	return true;
}

LL repair(LL n)
{
	LL d[20];
	LL l=0;
	LL nn = 0;

	while(n)
	{
		d[l++] = n%10;
		n = n/10;		
	}

	for(int i=0; i<l/2; i++)
	{
		LL temp = d[i];
		d[i] = d[l-1-i];
		d[l-1-i] = temp;
	}

	for(int i=1; i<l; i++)
	{
		if(d[i-1] > d[i])
		{
			d[i-1] -= 1;
			for(int j=i; j<l; j++)
				d[j] = 9;
			break;
		}
	}

	LL po = 1;
	for(int i=l-1; i>=0; i--)
	{	
		nn += d[i]*po;
		po = po*10;
	}
	return nn;
}

int main()
{
	ios_base::sync_with_stdio(0);

	int t;
	cin >> t;
	int nahoy = 1;
	while(t--)
	{
		LL n;
		cin >> n;
		while(!ok(n))
			n = repair(n);
		cout << "Case #" << nahoy << ": " <<  n << endl;
		nahoy++;
	}

	return 0;
}
