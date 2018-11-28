#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <stdio.h>

using namespace std;

int K=0;
int N=0,P=0;

bool Find(vector<vector<int>>&Q, vector<pair<int,int>>&D,int r, int kMin, int kMax)
{
	if(r==N)
	{
		K++;
		return true;
	}

	for(int i=0;i<P;i++)
	{
		if(Q[r][i]>0)
		{
			int mi = Q[r][i]/D[r].second;
			int ma = Q[r][i]/D[r].first;
			
			if(Q[r][i]>D[r].second*mi){mi++;}
			if(Q[r][i]<D[r].first*ma){ma--;}

			if(ma>=mi)
			{
				int mii = mi>kMin ? mi:kMin;
				int maa = ma<kMax ? ma:kMax;

				if(mii<=maa)
				{
					if(Find(Q, D,r+1, mii, maa))
					{
						Q[r][i]=0;
						return true;
					}
				}
			}
		}
	}

	return false;
}

int main()
{
	char input[]="input.in";
	char output[]="outut.out";



	FILE * fin = fopen("input.in", "r+");
	FILE * fin2 = fopen("output.out", "w+");

	int t=0,QWERTY=1;
	fscanf(fin,"%d", &t);
		
	while(t-->0)
	{
		K=0;
		fscanf(fin,"%d%d", &N, &P);

		vector<int>R(N);
		vector<pair<int,int>>D(N);

		for(int i=0;i<N;i++)
		{
			fscanf(fin,"%d",&R[i]);
			D[i].first = R[i]*9;
			D[i].second = R[i]*11;
		}

		vector<vector<int>>Q(N,vector<int>(P));

		for(int i=0;i<N;i++)
		{
			for(int j=0;j<P;j++)
			{
				fscanf(fin,"%d",&Q[i][j]);
				Q[i][j]*=10;
			}
			sort(Q[i].begin(), Q[i].end());
		}
		
		for(int i=0;i<P;i++)
		{
			int mi = Q[0][i]/D[0].second;
			int ma = Q[0][i]/D[0].first;
			if(Q[0][i]>D[0].second*mi){mi++;}
			if(Q[0][i]<D[0].first*ma){ma--;}
			if(ma>=mi)
			{
				Find(Q, D,1, Q[0][i]/D[0].second, Q[0][i]/D[0].first);
			}
		}


		fprintf(fin2,"Case #%d: %d\n",QWERTY, K);QWERTY++;
	}

	return 0;
}