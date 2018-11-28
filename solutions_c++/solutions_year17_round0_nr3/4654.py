#include <bits/stdc++.h>
#define mm 1000000

using namespace std;

int frq[mm]={0};

int main()
{
    ios::sync_with_stdio(false);
	//freopen("C-small-2-attempt0","r",stdin);
	freopen("C22.out","w",stdout);

	int t;
	cin>>t;
	for(int u=1;u<=t;u++){
		
		memset(frq,0,sizeof(frq));
		
		int n,k;
		cin>>n>>k;
		
		priority_queue<int,vector<int> > pq;
		
		int c;
		pq.push(n);
		
		while(1){
			
			if(k==1)
				break;
				
			int p=pq.top();
			if(p==n || frq[p]==1 )
				pq.pop();
			if(p<=1)
				break;
			
			if(p&1)
			{
				if(!frq[p/2])
					pq.push(p/2);
				frq[p/2]+=2;
			}
			else{
				
				if(!frq[p/2])
					pq.push(p/2);
				if(!frq[p/2-1])
					pq.push(p/2-1);
				
				frq[p/2]+=1;
				frq[p/2-1]+=1;
				
			}
			if(p!=n)	
				frq[p]--;
			k--;
			
		}
	
		int mx=0,mn=0;
		if(k==1){
			int p=pq.top();
		//	cout<<p<<"  ";
			mx=p/2;
			if(p%2==0)
				mn=p/2-1;
			else
				mn=p/2;
			
		}
		cout<<"Case #"<<u;
		cout<<": "<<mx<<" "<<mn<<"\n";
		
		
		
	}
	

	return 0;
}
