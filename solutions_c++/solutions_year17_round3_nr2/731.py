
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

int C, J;
int a[1500];

struct node
{
	int l;
	int r;
	int ln;
	int rn;
};
typedef struct node node;


vector<pair<int, pair<pair<int, int>, pair<int, int> > > > seg;
vector<pair<int, int> > ts;

bool done[3000];

int main()
{
	ios_base::sync_with_stdio(0);
	int t;
	cin >> t;
	int nahoy = 1;
	while(t--)
	{
		cin >> C >> J;		
		ts.clear();
		seg.clear();
		SET(done, 0);

		int jt=0, ct=0;
		int sz;

		for(int i=0; i<C; i++)
		{
			int l, r;
			cin >> l >> r;
			ct += r-l;
			ts.PB(MP(l, 1));
			ts.PB(MP(r-1, 1));
		}
		for(int i=0; i<J; i++)
		{
			int l, r;
			cin >> l >> r;
			jt += r-l;
			ts.PB(MP(l, 2));
			ts.PB(MP(r-1, 2));
		}
		sort(ts.begin(), ts.end());
		sz = SZ(ts);
		
		/*
		printf("\ntimestamp\n");
		for(int i=0; i<sz; i++)
			printf("%d %d\n", ts[i].F, ts[i].S);
		printf("\n");
		*/

		for(int i=1; i<=sz; i+=2)
		{
			int c = i%sz;
			int n = (i+1)%sz;

			node temp;
			temp.l = ts[c].F+1;
			temp.r = ts[n].F-1;
			temp.ln = ts[c].S;
			temp.rn = ts[n].S;
			seg.PB(MP((temp.r - temp.l + 1 + 1440)%1440, MP(MP(temp.l, temp.r), MP(temp.ln, temp.rn) ) ));
		}
		sort(seg.begin(), seg.end());
		sz = SZ(seg);
		
		/*
		printf("\nseg\n");
		for(int i=0; i<sz; i++)
			printf("%d %d %d %d %d\n", seg[i].F, seg[i].S.F.F, seg[i].S.F.S, seg[i].S.S.F, seg[i].S.S.S);
		printf("\n");
		*/
		
		int ans = sz + C + J;
		//printf("ct = %d\njt = %d\n\n", ct, jt);
		for(int i=0; i<sz; i++)
		{
			if(seg[i].S.S.F == seg[i].S.S.S)
			{
				if(seg[i].S.S.F == 1)
				{
					if(720-ct >= seg[i].F)
					{
						ct += seg[i].F;
						ans -= 2;
						done[i] = true;
					}
					else
					{
						ans -= 0;
						done[i] = true;
					}
				}
				else if(seg[i].S.S.F == 2)
				{
					if(720-jt >= seg[i].F)
					{
						jt += seg[i].F;
						ans -= 2;
						done[i] = true;
					}	
					else
					{
						ans -= 0;
						done[i] = true;
					}
				}
				else
				{
					cout << "problem\n\n";
					exit(-1);
				}
			}
			else
			{
				ans -= 1;
				done[i] = true;
			}
		}
		printf("Case #%d: %d\n", nahoy, ans);
		nahoy++;
	}
	return 0;
}
