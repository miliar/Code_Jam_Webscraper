#include <bits/stdc++.h>

using namespace std;

struct data
{
	int vl;
	string c;
}A[5];

string tmpres[2000];

bool cmp(data a, data b) {return a.vl<b.vl;}

int main()
{
	//freopen("testB1.inp","r",stdin);
	//freopen("testB1.out","w",stdout);
	int T;
	cin >> T;
	int test=0;
	while (T--)
	{
		test++;
		int cnt=0;
		int R,O,Y,G,B,V,N;
		string res="";
		cin >> N;
		cin >> R >> O >> Y >> G >> B >> V;
		bool xet=true;
		if (G>=R && G!=0) xet=false;
		if (O>=B && O!=0) xet=false;
		if (V>=Y && V!=0) xet=false;
		if (G==R && G==N/2 && N%2==0)
		{
			for (int i=1; i<=N/2; ++i) res+='G', res+='R';
			cout << "Case #" << test << ": " << res << '\n';
			continue;
		}
		if (O==B && O==N/2 && N%2==0)
		{
			for (int i=1; i<=N/2; ++i) res+='O', res+='B';
			cout << "Case #" << test << ": " << res << '\n';
			continue;
		}
		if (V==Y && V==N/2 && N%2==0)
		{
			for (int i=1; i<=N/2; ++i) res+='V', res+='Y';
			cout << "Case #" << test << ": " << res << '\n';
			continue;
		}
		if (!xet)
		{
			printf("Case #%d: IMPOSSIBLE\n",test);
			continue;
		}
		R-=G, B-=O, Y-=V;
		if (R>B+Y || B>R+Y || Y>R+B)
		{
			printf("Case #%d: IMPOSSIBLE\n",test);
			continue;
		}
		A[1].vl=R; A[1].c="R"; A[2].vl=B; A[2].c="B"; A[3].vl=Y; A[3].c="Y";
		sort(A+1,A+4,cmp);
		while (A[2].vl>A[1].vl)
		{
			tmpres[++cnt]=A[3].c;
			tmpres[++cnt]=A[2].c;
			A[3].vl--; A[2].vl--;
		}
		while (A[3].vl>A[2].vl)
		{
			tmpres[++cnt]=A[3].c;
			tmpres[++cnt]=A[2].c;
			tmpres[++cnt]=A[3].c;
			tmpres[++cnt]=A[1].c;
			A[3].vl-=2; A[2].vl--; A[1].vl--;
		}
		while (A[3].vl>0)
		{
			tmpres[++cnt]=A[3].c;
			tmpres[++cnt]=A[2].c;
			tmpres[++cnt]=A[1].c;
			A[3].vl--; A[2].vl--; A[1].vl--;
		}
		bool xetR,xetB,xetY;
		xetR=xetB=xetY=true;
		for (int i=1; i<=cnt; ++i)
		{
			res+=tmpres[i];
			if (xetR && tmpres[i]=="R")
			{
				for (int j=1; j<=G; ++j) res+='G', res+='R';
				xetR=false;
			}
			if (xetB && tmpres[i]=="B")
			{
				for (int j=1; j<=O; ++j) res+='O', res+='B';
				xetB=false;
			}
			if (xetY && tmpres[i]=="Y")
			{
				for (int j=1; j<=V; ++j) res+='V', res+='Y';
				xetY=false;
			}
		}
		cout << "Case #" << test << ": " << res << '\n';
	}
}
