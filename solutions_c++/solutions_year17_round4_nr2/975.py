#include <bits/stdc++.h>
#define D(x...) fprintf(stderr, x)
using namespace std;
int T;
int freq[3][1005];
int main()
{ 
	freopen("infile.txt", "r", stdin);
	scanf("%d ", &T);
	for(int t=1; t<=T; t++)
	{
		for(int a=0; a<=1000; a++)
		{
			freq[0][a] = 0;
			freq[1][a] = 0;
		}
		int N, C, M;
		scanf("%d %d %d", &N, &C, &M);
		assert(C==2);
		int filledones[2] = {0, 0};
		int numextra[2] = {0, 0};
		int freeones[2] = {0, 0};
		for(int m=0; m<M; m++)
		{
			int a, b;
			scanf("%d %d", &a, &b);
			b--;
			if(a==1)
			{
				filledones[b]++;
			}
			else
			{
				freq[b][a]++;
				numextra[b]++;
			}
		}
		//if(t==68) printf("%d %d %d %d\n", filledones[0], filledones[1], numextra[0], numextra[1]);
		if(filledones[0] <= numextra[1]) numextra[1]-=filledones[0];
		else numextra[1]=0;
		if(filledones[1] <= numextra[0]) numextra[0]-=filledones[1];
		else numextra[0]=0;
		//if(t==68) printf("%d %d %d %d\n", filledones[0], filledones[1], numextra[0], numextra[1]);
		int ext = min(numextra[0], numextra[1]); 
		int B = filledones[0] + filledones[1] + ext;
		numextra[0]-=ext;
		numextra[1]-=ext;
		B+= numextra[0] + numextra[1];

		priority_queue<pair<int, int> > PQ[2];
		for(int i=1; i<=N; i++)
		{
			if(freq[0][i]==0 && freq[1][i]) freeones[1]+= freq[1][i];
			else if(freq[1][i]==0 && freq[0][i]) freeones[0]+= freq[0][i];
			else {
				if(freq[0][i])PQ[0].push({freq[0][i], i});
				if(freq[1][i])PQ[1].push({freq[1][i], i});
			}
		}
		//if(t==68) printf("%d %d\n", freeones[0], freeones[1]);
		int e = 0;
		for(e=0; e<ext; e++)
		{
			if(PQ[0].size()==0 || PQ[1].size()==0) break;
			pair<int, int> p0 = PQ[0].top();
			PQ[0].pop();
			pair<int, int> p1 = PQ[1].top();
			PQ[1].pop();
			if(p0.second!= p1.second)
			{
				p0.first--;
				p1.first--;
				if(p0.first) PQ[0].push(p0);
				if(p1.first) PQ[1].push(p1);
			} 
			else
			{
				if(PQ[0].size()> PQ[1].size())
				{
					pair<int, int> p00 = PQ[0].top();
					PQ[0].pop();
					p00.first--;
					p1.first--;
					if(p00.first) PQ[0].push(p00);
					if(p1.first) PQ[1].push(p1);
					PQ[0].push(p0);
				}
				else if(PQ[1].size()!=0)
				{
					pair<int, int> p11 = PQ[1].top();
					PQ[1].pop();
					p0.first--;
					p11.first--;
					if(p0.first) PQ[0].push(p0);
					if(p11.first) PQ[1].push(p11);
					PQ[1].push(p1);
				}
				else
				{
					PQ[0].push(p0);
					PQ[1].push(p1);
					break;
				}
			}
		}
		assert(PQ[0].size()==0 || PQ[1].size()==0 || (PQ[0].size()==1 && PQ[1].size()==1));
		while(PQ[0].size())
		{
			pair<int, int> p0 = PQ[0].top();
			PQ[0].pop();
			if(freeones[1])
			{
				freeones[1]--;
				p0.first--;
				if(p0.first) PQ[0].push(p0);
				e++;
			}
			else break;
		}
		while(PQ[1].size())
		{
			pair<int, int> p0 = PQ[1].top();
			PQ[1].pop();
			if(freeones[0])
			{
				freeones[0]--;
				p0.first--;
				if(p0.first) PQ[1].push(p0);
				e++;
			}
			else break;
		}
		e+= min(freeones[0], freeones[1]);
		e = min(e, ext);
		int Z = ext-e;
		printf("Case #%d: %d %d\n", t, B, Z);
	}
}