#include <iostream>
#include <algorithm>

#define x first
#define y second

using namespace std;

typedef pair<int,int> pii;
int n,nt,r,o,y,g,b,v,res[1010];
pii p[4];

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin >> nt;
	for (int _=1;_<=nt;_++)
	{
		cin >> n >> r >> o >> y >> g >> b >> v;
		for (int i=0;i<3;i++)
			p[i].y=i;
		p[0].x=r;
		p[1].x=y;
		p[2].x=b;
		sort(p,p+3);
		for (int i=1;i<=n;i+=2)
		{
			if (p[2].x>0) p[2].x--,res[i]=p[2].y;
			else if (p[1].x>0) p[1].x--,res[i]=p[1].y;
			else p[0].x--,res[i]=p[0].y;
		}
		for (int i=2;i<=n;i+=2)
		{
			if (p[2].x>0) p[2].x--,res[i]=p[2].y;
			else if (p[1].x>0) p[1].x--,res[i]=p[1].y;
			else p[0].x--,res[i]=p[0].y;
		}
		int tru=0;
		for (int i=1;i<n;i++)
			if (res[i]==res[i+1])
			{
				cout << "Case #" << _ << ": IMPOSSIBLE\n";
				tru=1;
				break;
			}
		if (!tru and res[n]==res[1])
		{
			cout << "Case #" << _ << ": IMPOSSIBLE\n";
			tru=1;
		}
		if (tru) continue;
		cout << "Case #" << _ <<": ";
		for (int i=1;i<=n;i++)
		{
			if (res[i]==0) cout << "R";
			if (res[i]==1) cout << "Y";
			if (res[i]==2) cout << "B";
		}
		cout << "\n";
	}
}