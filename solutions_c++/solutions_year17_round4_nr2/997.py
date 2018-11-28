#include<iostream>
#include<vector>
#include<algorithm>
#include<stdio.h>

using namespace std;

void addColumn(vector<vector<int> >field, int n)
{
	for(int i=0;i<n;i++)
	{
		field[i].push_back(-1);
	}
}

int main()
{
	int t=0,T=0;
	
	FILE * fin=fopen("input.in","r");
	FILE * fin2=fopen("output.out","w");

	fscanf(fin,"%d",&T);

	while(t++<T)
	{
		int n=0, m=0, c=0;
		fscanf(fin,"%d%d%d",&n, &c, &m);

		vector<pair<int,int> >person(c);
		vector<int>places(n,0);

		for(int i=0;i<c;i++)
		{
			person[i].first=0;
			person[i].second=i;
		}

		vector<pair<int, int> >data(m);

		//vector<bool hasPersonInTrain

		for(int i=0;i<m;i++)
		{
			fscanf(fin,"%d%d",&data[i].first, &data[i].second);

			person[data[i].second-1].first++;
			places[data[i].first-1]++;
		}

		sort(person.begin(),person.end());

		int k=person[c-1].first;

		int ma1=0;
		for(int i=0;i<n;i++)
		{
			ma1+=places[i];

			if(ma1>(i+1)*k)
			{
				k=(ma1%k > 0) ?(ma1/k+1):(ma1/k); 
			}
		}

		int l=0;

		for(int i=0;i<n;i++)
		{
			ma1+=places[i];

			if(places[i]>k)
			{
				l+=places[i]-k; 
			}
		}


		fprintf(fin2, "Case #%d: %d %d\n", t, k, l);
	}

	return 0;
}