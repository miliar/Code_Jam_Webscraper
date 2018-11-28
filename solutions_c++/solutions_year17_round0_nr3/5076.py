#include<bits/stdc++.h>

using namespace std;

typedef long long int lli;

struct st{
	lli min;
	lli max;
	lli in;
	lli prev;
};

struct mycompare{
	bool operator()(const st &t1, const st &t2) const
	{
       if(t1.min<t2.min)
       return 1;
       else
       if(t1.min>t2.min)
       return 0;
       else
       if(t1.max<t2.max)
       return 1;
       if(t1.max>t2.max)
       return 0;
       else 
       return 0;
	}
};

int main()
{
	freopen("C-small-2-attempt0.in","r",stdin);
    freopen("C-small-2-attempt0.out","w",stdout);
	int t;
	lli n,k,l,r,id,c,n1,n2,previd;
	st st1;
	vector< pair<int,int> > v;
	priority_queue<st,vector<st>,mycompare> pq;
	scanf("%d",&t);
	for(int i=1;i<=t;i++){
		c=0;
		scanf("%lli%lli",&n,&k);
		v.resize(n+1);
	    if(n%2==0){
	    	id=(n/2)-1;
	    	
		}
		else{
			id=((n+1)/2)-1;
		}
		l=id-0;
	    r=(n-1)-id;
	    st1.in=id;
	    st1.min=min(l,r);
	    st1.max=max(l,r);
	    st1.prev=n;
	    pq.push(st1);
	    previd=n;
	    v[previd]=make_pair(-1,previd);
	    while(c!=k){
	    	st1=pq.top();
	    	pq.pop();
	    	c++;
	    	if(c==k){
	    		cout<<"Case #"<<i<<": "<<st1.max<<" "<<st1.min<<endl;
	    		break;
			}
	    	id=st1.in;
	    	if(id<st1.prev)
	    	v[id]=make_pair(v[st1.prev].first,st1.prev);
	    	if(id>st1.prev)
	    	v[id]=make_pair(st1.prev,v[st1.prev].second);
	    	n1=id-v[id].first-1;
	    	n2=v[id].second-id-1;
	    	previd=id;
	    	if(n1%2==0){
	    		id=(n1/2);
			}
			else{
				id=((n1+1)/2);
			}
			id=previd-id;
			l=id-v[previd].first-1;
			r=previd-id-1;
			st1.in=id;
			st1.max=max(l,r);
			st1.min=min(l,r);
			st1.prev=previd;
			if(n1!=0)
			pq.push(st1);
			
			if(n2%2==0){
	    		id=(n2/2);
			}
			else{
				id=((n2+1)/2);
			}
			id=previd+id;
			l=id-previd-1;
			r=v[previd].second-id-1;
			st1.in=id;
			st1.max=max(l,r);
			st1.min=min(l,r);
			st1.prev=previd;
			if(n2!=0)
			pq.push(st1);
	    	
		}
	    
	    
		v.clear();
		while(!pq.empty()){
			pq.pop();
		}
	}
	return 0;
}
