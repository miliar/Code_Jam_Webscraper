#include<iostream>
#include<fstream>
#include<stdlib.h>
#include<vector>
#include<algorithm>
#include<queue>

#define PI 3.14159265359

using namespace std;

int main()
{
	ifstream in;
	ofstream out;
	in.open("inputLarge.txt");
	out.open("outputLarge.txt");
	int t,cases=0;
	in>>t;
	while(t--)
	{
		cases++;
		long long int n,k;
		vector<pair<long long int,long long int> > v;
		long long int r,h;
		double a=0,b=0,area=0;
		in>>n>>k;
		for(int i=0;i<n;i++)
		{
			in>>r>>h;
			v.push_back(make_pair(r,2*r*h));
		}
		sort(v.begin(),v.end(),greater<pair<long long int,long long int> >());
		for(int i=0;i<=n-k;i++)
        {
            r = v[i].first;
            a = r*r;
            b = v[i].second;
            priority_queue<long long int,vector<long long int> > pq;
            for(int j=0;j<n;j++)
            {
                if(i!=j && v[j].first<=r) pq.push(v[j].second);
            }
            if(!pq.empty())
			{
				for(int j=0;j<k-1;j++)
				{
					b = b + pq.top();
					pq.pop();
				}
			}
			if(area < (a+b)) area = a+b;
        }
		area = area * PI;
		out<<"Case #"<<cases<<": "<<fixed<<area<<endl;
	}
	return 0;
}
