#include<bits/stdc++.h>
using namespace std;

#define ld long double



ld eps=1e-6;

bool ok(ld speed,vector<pair<ld,ld> >X)
{
	int i;

//	cout<<X.size()<<endl;	
	for (i=0;i<X.size();i++)
	{
		ld t1=speed*X[i].second;
		ld t2=X[i].first;
	//	cout<<t1<<" "<<t2<<endl;
		if(t1>=t2)
		{
	//		cout<<"Galat "<<speed<<endl;
			return false;
		}
	}
	
	return true;
}

int main()
{
	freopen("A-small-attempt7.in","r",stdin);
	freopen("Out1.txt","w",stdout);
	int T;
	scanf("%d",&T);
	int tt=0;
	while(T--)
	{
		tt++;
		int D,N;
		scanf("%d%d",&D,&N);
		
		int i,j;
		
		vector<pair<ld,ld> >X;
		vector<pair<int,int> >V;
		for (i=1;i<=N;i++)
		{
			int x,y;
			cin>>x>>y;
			V.push_back(make_pair(x,y));
		}
		
		sort(V.begin(),V.end());
		

		int cur=0;
		
		ld time=0;
		
		while(1)
		{
			ld dis=1e10;
			int indx=-1;
			
			for (i=cur+1;i<N;i++)
			{
				if(i==cur)
				continue;
				
				ld tmp=(ld)(V[i].first-V[cur].first)/(V[cur].second-V[i].second);	
				
				if(tmp<0)
				continue;
				
				ld d=V[i].first+V[i].second*tmp;
				
				if(d<dis)
				{
					dis=d;
					indx=i;
				}
			}
			
			if(indx==-1)
			break;
			
			if(dis>D)
			break;
			
			double tm=(double)(dis-V[cur].first)/V[cur].second;
			X.push_back(make_pair(dis,tm));
			cur=indx;
		}
		
			double tm=(double)(D-V[cur].first)/V[cur].second;
		X.push_back(make_pair(D,tm));
		
		/*for (i=0;i<X.size();i++)
		{
			cout<<X[i].first<<" "<<X[i].second<<endl;
		}*/
		
		//cout<<"Done\n";
		
		
		
		ld l=0,r=1e15+1,best=0;
		
		while(r-l>=eps)
		{
			
			ld mid=(l+r)/2;
		//	cout<<mid<<endl;
			
			if(ok(mid,X))
			{
			//	cout<<"Haha\n";
			//	cout<<mid<<endl;
				best=max(best,mid);
				l=mid+eps;
			}
			
			else r=mid-eps;
		}
		cout.precision(7);
		cout<<"Case #"<<tt<<": "<<fixed<<best<<endl;
	}
}
