#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <string>
#include <time.h>

#define SQR(_x) ((_x)*(_x))
#define MAX(_a,_b) _a>_b? _a:_b
#define MIN(_a,_b) _a<_b? _a:_b
#define NL printf("\n")
#define LL long long
#define DB double
#define PB push_back
#define INF 1000000000

using namespace std;

int t;
int T;
int k;
int len;
char initial_pancake[10000];
struct pancake{
	string seq;
	pancake(char* S)
	{
		seq = S;
	}
	pancake(string S)
	{
		seq = S;
	}
};

void pancake_flipping()
{
	queue <pancake> q;
	set<string> check;
	// printf("ENTERING FLIPING FUCNTION\n");
	string temp;
	string adding;
	int count = 0,nenq = 0,nroot = 1;
	q.push(pancake(initial_pancake));
	check.insert(q.front().seq);
	while(not q.empty())
	{
		count++;
		// printf("ROUND:%d\n",count);
		for(int i=0;i<nroot;i++)
		{
			//ใส่ทุก state ที่กูจะฟลิป :)
			temp = q.front().seq;
			q.pop();
			// cout << "temp = " << temp;
			adding = temp;
			for(int i=0;i<len-k+1;i++)
			{
				//flip k bit
				for(int j=i;j<i+k;j++)
				{
					adding[j] = adding[j]=='+'? '-':'+';
				}
				//adding to q
				// cout << "adding: " << adding << "\n";
				if(check.find(adding) == check.end())
				{
					bool isall_1 = true;
					// cout << "que_adding: " << adding << "\n";
					for(int i=0;i<len;i++)
					{
						if(adding[i] != '+')
						{
							isall_1 = false;
							break;
						}
					}
					if(isall_1)
					{
						printf("Case #%d: %d\n",t,count);
						return ;
					}
					check.insert(adding);
					q.push(adding);
					nenq++;
				}
				adding = temp;
			}
		}
		nroot = nenq;
		nenq = 0;
		// printf("End loop %d\n",count);
	}
printf("Case #%d: IMPOSSIBLE\n",t);
return ;
}


int main()
{
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		scanf("%s",initial_pancake);
		scanf("%d",&k);
		len = strlen(initial_pancake);
		bool isall_1 = true;
		for(int i=0;i<len;i++)
		{
			if(initial_pancake[i] != '+')
			{
				isall_1 = false;
				break;
			}
		}
		if(isall_1) printf("Case #%d: 0\n",t);
		else if(len<k) printf("Case #%d: IMPOSSIBLE\n",t);
		else pancake_flipping();
	}
	return 0;
}