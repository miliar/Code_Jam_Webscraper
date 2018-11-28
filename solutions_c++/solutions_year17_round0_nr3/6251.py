#include<iostream>
#include<algorithm>
#include<vector>
#include<stdlib.h>
#include<queue>

using namespace std;

bool compareFunc(const pair<int,int> &p1,const  pair<int,int> &p2)
{
	int st1=p1.first, en1=p1.second;
	int st2=p2.first, en2= p2.second;

	if(en1-st1 != en2-st2)
	    	return en2-st2 > en1-st1;
	else
	    	return st2 < st1;
}

int main(){
  
    int loopCount=1,loopsLeft,elementsAdded;

    int n;
    int k;
    int st;
    int en;
    int mid;
    
    cin>>loopsLeft;
    
    while(loopsLeft--) {
    
	elementsAdded=0;
    	priority_queue< pair<int,int> , vector< pair<int,int> >, function<bool( const pair<int,int>& , const pair<int,int>& ) > > pq(compareFunc);
	
	cin>>n;
	cin>>k;
	
	pq.push(make_pair(0,n-1));

	while(elementsAdded < k) {
	
		st = pq.top().first;
		en = pq.top().second;
		mid = (st +en) /2;
		pq.pop();
		
		if(st > en)
			continue;

		if( (mid -1) -st >=0)
			pq.push(make_pair(st,mid-1));
		
		if (en - (mid+1) >=0)
			pq.push(make_pair(mid+1,en));
		
		elementsAdded++;
	}


	cout<<"Case #"<<loopCount<<": "<<max(mid-st,en-mid)<<" "<<min(mid-st,en-mid)<<endl;
    	loopCount++;
    }
    return 0;
}
