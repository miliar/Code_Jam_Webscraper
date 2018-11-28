
#include<vector>
#include<algorithm>
#include<iostream>
#include<cstdio>
#include<stdio.h>
#include<cstdlib>
#include<stdlib.h>
#include<cstring>
#include<map>
#include<set>
#include<queue>

using namespace std;
#define lli long long int 
#define fr(a,b,c) for(a=b;a<c;a++)	
#define vi vector<int> 
#define pb push_back
#define pii pair<int,int>
#define mp make_pair
#define f first
#define s second
int main()
{
	int t;
	cin>>t;
	int q1=1;

	while(t--)
	{
		int n,k;
		cin>>n>>k;
		priority_queue< pii,vector<pii> > q;

		int low=1;
		int high=n;
		q.push(mp(high-low,-1));
		int i;

		for(i=1;i<=k;i++)
		{
			pii p=q.top();
			//cout<<p.f<<" "<<-p.s<<endl;
			q.pop();

			low=-p.s;
			high=p.f+(-1*p.s);
			int mid=(low+high)/2;
			//mark[mid]=1;
			//cout<<"low "<<low<<" "<<mid<<" "<<high<<" "<<endl; 
			
			q.push(mp(mid-low-1,-low));
			q.push(mp(high-mid-1,-(mid+1)));
			//cout<<"low "<<low<<" "<<mid<<" "<<high<<" "<<endl; 
			if(i==k)
			{
				//cout<<"low "<<low<<" "<<mid<<" "<<high<<" "<<endl; 
				
				cout<<"Case #"<<q1<<": "<<high-mid<<" "<<mid-low<<endl;
			}
		}
		q1++;

	}

}



