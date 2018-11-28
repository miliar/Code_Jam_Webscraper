#include <stdio.h>
#include <map>
void solve();
std::map< std::pair<char,char> , int> cmp;
int main()
{
	freopen("smallB2.in","r",stdin);
	freopen("output.txt","w",stdout);
	cmp[std::make_pair('R','G')] = 1;
	cmp[std::make_pair('G','R')] = 1;
	cmp[std::make_pair('B','O')] = 1;
	cmp[std::make_pair('O','B')] = 1;
	cmp[std::make_pair('Y','V')] = 1;
	cmp[std::make_pair('V','Y')] = 1;
	cmp[std::make_pair('R','B')] = 1;
	cmp[std::make_pair('B','R')] = 1;
	cmp[std::make_pair('R','Y')] = 1;
	cmp[std::make_pair('Y','R')] = 1;
	cmp[std::make_pair('Y','B')] = 1;
	cmp[std::make_pair('B','Y')] = 1;
	int T;
	scanf("%d",&T);
	for(int i=1;i<=T;i++)
	{
		printf("Case #%d: ",i);
		solve();
	}
}

char x[1010];
void solve()
{
	int N;
	int R,O,Y,G,B,V;
	scanf("%d%d%d%d%d%d%d",&N,&R,&O,&Y,&G,&B,&V);
	
	char state;
	if(R>0) state = 'R';
	if(Y>0) state = 'Y';
	if(B>0) state = 'B';
	
	char fState = state;
	for(int i=1;i<N;i++)
	{
		x[i] = state;
		if(state=='R')
		{
			R--;
			if(G>0) state = 'G';
			else if(B<Y) state = 'Y';
			else if(Y<B) state = 'B';
			else
			{
				if(fState=='B') state = 'B';
				else state = 'Y';
			}
		}
		else if(state=='Y')
		{
			Y--;
			if(V>0) state = 'V';
			else if(B<R) state = 'R';
			else if(R<B) state = 'B';
			else
			{
				if(fState=='B') state = 'B';
				else state = 'R';
			}
		}
		else if(state=='B')
		{
			B--;
			if(O>0) state = 'O';
			else if(R<Y) state = 'Y';
			else if(Y<R) state = 'R';
			else
			{
				if(fState=='R') state = 'R';
				else state = 'Y';
			}
		}
		else if(state=='G') G--,state = 'R';
		else if(state=='V') V--,state = 'Y';
		else if(state=='O') O--,state = 'B';
	}
	
	x[N] = state;
	if(state=='R') R--;
	else if(state=='Y') Y--;
	else if(state=='B') B--;
	else if(state=='G') G--;
	else if(state=='V') V--;
	else if(state=='O') O--;
	
	if(cmp[std::make_pair(fState,state)]==0) printf("IMPOSSIBLE\n");
	else if(R==0&&Y==0&&B==0&&G==0&&V==0&&O==0)
	{
		for(int i=1;i<=N;i++) printf("%c",x[i]);
		printf("\n");
	}
	else printf("IMPOSSIBLE\n");
}
