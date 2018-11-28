#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <iostream>

#define LLI unsigned long long int

using namespace std;

struct piece {
	bool status[1000];
	int fCount;
};

piece memo[1001];
int N;

bool flip(bool status[1000], int fpos, int fsize);

int main()
{
	ios_base::sync_with_stdio();
	int T;
	cin >> T;
	char c;
	for(int aa = 0;aa < T;++aa)
	{
		piece start;
		N = 0;
		while(scanf("%c", &c))
		{
			if(c == '\n')
				continue;
			else if(c == ' ')
				break;
			start.status[N] = ((c == '-') ? false : true);
			memo[0].status[N] = ((c == '-') ? false : true);
			++N;
		}
		
		int K;
		cin >> K;
		
		int position = 0;
		memo[0].fCount = 0;
		for(int i=1;i<=N && memo[0].status[i-1] == true;++i)
		{
			for(int j=0;j<N;++j)
				memo[i].status[j] = memo[0].status[j];
			memo[i].fCount = 0;
			position = i;
		}
		
		bool *cstatus;
		bool nstatus[1000];
		while(position < N)
		{
			// right now, position = last position where it is still all +
			memcpy(nstatus, memo[position].status, sizeof(bool)*N);
			if(!flip(nstatus, position+1, K))
				break;
			// okay, we're good
			int foundAt = -1;
			for(int i=position;i<N;++i)
			{
				if(nstatus[i] == true)
				{
					memcpy(memo[i+1].status, nstatus, sizeof(bool)*N);
					memo[i+1].fCount = memo[position].fCount +1;
				}
				else
				{
					foundAt = i;
					break;
				}
			}
			if(foundAt == -1)
			{
				position = N;
				break;
			}
			else
			{
				position = foundAt;
			}
		}
		
		cout << "Case #" << aa+1 << ": ";
		if(position != N)
			cout << "IMPOSSIBLE";
		else
			cout << memo[N].fCount;
		cout << endl;
	}
	return 0;
}

bool flip(bool status[1000], int fpos, int fsize)
{ // fpos is 1-indexed!!
	if(fpos+fsize-1 > N)
		return false;
	for(int i=fpos-1;i<fpos+fsize-1;++i)
		status[i] = !status[i];
	return true;
}
