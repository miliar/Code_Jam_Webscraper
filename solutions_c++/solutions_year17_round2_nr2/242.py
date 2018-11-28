#include <cstdio>

int T,cas,n,r,y,b,ry,yb,br,cc,cbr,cry,cyb,w[4][4],st,lst,rst,ch[4],no,
	o[1011],fo[1011],nfo,i;

int u[1000], tbo[500][500];

int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
	scanf("%d", &T);
	for (cas=1; cas<=T; ++cas)
	{
		scanf("%d%d%d%d%d%d%d", &n, &r, &ry, &y, &yb, &b, &br);
		
		u['R']=r, u['O']=ry, u['Y']=y, u['G']=yb, u['B']=b, u['V']=br;
		
		tbo['R']['B'] = tbo['B']['R'] = 1;
		tbo['R']['Y'] = tbo['Y']['R'] = 1;
		tbo['B']['Y'] = tbo['Y']['B'] = 1;
		tbo['R']['G'] = tbo['G']['R'] = 1;
		tbo['Y']['V'] = tbo['V']['Y'] = 1;
		tbo['B']['O'] = tbo['O']['B'] = 1;

		
//		printf("%d %d %d %d %d %d %d", n, r, ry, y, yb, b, br);
		
		printf("Case #%d: ", cas);
		r -= yb;
		y -= br;
		b -= ry;
		if (r < 0 || y < 0 || b < 0)
		{
			printf("IMPOSSIBLE\n");
			continue;
		}
		cc = (r+y+b)&1;
		cbr = (b+r-y-cc)/2;
		cyb = (b-r+y-cc)/2;
		cry = (-b+r+y-cc)/2;
		
		if (cbr<0 || cyb<0 || cry<0)
		{
			printf("IMPOSSIBLE\n");
			continue;
		}
		
		
		ch[0] = 'R';
		ch[1] = 'B';
		ch[2] = 'Y';
		w[0][1] = w[1][0] = cbr;
		w[0][2] = w[2][0] = cry;
		w[1][2] = w[2][1] = cyb;
		st = -1;
		int mx = 0;
		if (w[0][1]+w[0][2]+cc+yb > mx) st = 0, mx=w[0][1]+w[0][2]+cc+yb;
		if (w[1][0]+w[1][2]+cc+ry > mx) st = 1, mx=w[1][0]+w[1][2]+cc+ry;
		if (w[2][0]+w[2][1]+cc+br > mx) st = 2, mx=w[2][0]+w[2][1]+cc+br;
		
//		printf("st=%d\n", st);
		
		if (st == -1)
		{
			printf("IMPOSSIBLE\n");
			continue;
		}
		lst = (st-1+3)%3;
		rst = (st+1)%3;
		
		
//		printf("lsr=%d %d %d\n", lst, st, rst);
//		printf("cc=%d cbr=%d cyb=%d cry=%d\n", cc, cbr, cyb, cry);
		
		no = 0;
		if (cc > 0)
		for (i=1; i<=cc; ++i)
		{
			o[++no] = ch[rst];
			if (w[rst][lst] > 0)
			{
				for (int j=1; j<=w[rst][lst]; ++j)
				{
					o[++no] = ch[lst];
					o[++no] = ch[rst];
				}
				w[rst][lst] = w[lst][rst] = 0;
			}
			o[++no] = ch[lst];
			o[++no] = ch[st];
//			printf("in\n");
		}
		if (w[st][rst] > 0)
		{
			o[++no] = ch[rst];
			if (w[rst][lst] > 0)
			{
				for (i=1; i<=w[rst][lst]; ++i)
				{
					o[++no] = ch[lst];
					o[++no] = ch[rst];
				}
				w[rst][lst] = w[lst][rst] = 0;
			}
			for (i=1; i<w[st][rst]; ++i)
			{
				o[++no] = ch[st];
				o[++no] = ch[rst];
			}
			o[++no] = ch[st];
		}
		if (w[st][lst] > 0)
		{
			o[++no] = ch[lst];
			if (w[rst][lst] > 0)
			{
				for (i=1; i<=w[rst][lst]; ++i)
				{
					o[++no] = ch[rst];
					o[++no] = ch[lst];
				}
				w[rst][lst] = w[lst][rst] = 0;
			}
			for (i=1; i<w[st][lst]; ++i)
			{
				o[++no] = ch[st];
				o[++no] = ch[lst];
			}
			o[++no] = ch[st];
		}

//		printf("no=%d\n", no);for (i=1; i<=no; ++i) printf("%c", o[i]); printf("\n");

		if (no == 0)
		{
			if (st==0 && yb>0) while (yb--) o[++no]='G',o[++no]='R';
			if (st==1 && ry>0) while (ry--) o[++no]='O',o[++no]='B';
			if (st==2 && br>0) while (br--) o[++no]='V',o[++no]='Y';
		}
		

		nfo = 0;
		for (i=1; i<=no; ++i)
		{
			fo[++nfo] = o[i];
			if (o[i]=='R' && yb>0)
			{
				while (yb--) fo[++nfo]='G',fo[++nfo]='R';
			}
			if (o[i]=='Y' && br>0)
			{
				while (br--) fo[++nfo]='V',fo[++nfo]='Y';
			}
			if (o[i]=='B' && ry>0)
			{
				while (ry--) fo[++nfo]='O',fo[++nfo]='B';
			}
		}
		if (nfo != n)
		{
			printf("IMPOSSIBLE\n");
			continue;
		}
		fo[n+1] = fo[1];
		for (i=1; i<=n; ++i)
		{
			printf("%c", fo[i]);
			u[fo[i]]--;
			if (!tbo[fo[i]][fo[i+1]]) printf("warning tbo\n");

		}
		printf("\n");
		
		if (u['R']!=0||u['O']!=0||u['Y']!=0||u['G']!=0||u['B']!=0||u['V']!=0) printf("warning\n");
		
//			printf("cas=%d T=%d  no=%d nfo=%d\n", cas, T, no, nfo);
	}
	
//	printf("cas=%d T=%d\n", cas, T);
	
	return 0;
}
		
		
