#include<stdio.h>
#include<set>
#include<vector>

using namespace std;

set< vector<int> > S;
vector< int > V;
int N, M, T;
int index;

int main(void)
{
	int l0, l1;
	set< vector<int> >::iterator it;
	int length, left, right;
	
	V.resize(3);
	scanf("%d", &T);
	for(l0 = 1; l0 <= T; l0++)
	{
		scanf("%d %d", &N, &M);
		fprintf(stderr, "%d/%d\n", l0, T);
		
		S.clear();
		V[0] = -N;
		V[1] = 1;
		V[2] = N;
		S.insert(V);

		for(l1 = 0; l1 < M; l1++)
		{
			it = S.begin();

			length = -(*it)[0];
			left = (*it)[1];
			right = (*it)[2];

			S.erase(it);

			index = (left+right) >> 1;

			V[1] = left;
			V[2] = index-1;
			V[0] = -(V[2] - V[1] + 1);
			S.insert(V);

			V[1] = index+1;
			V[2] = right;
			V[0] = -(V[2] - V[1] + 1);
			S.insert(V);
		}

		printf("Case #%d: %d %d\n", l0, right-index, index-left);
	}
	return 0;
}
