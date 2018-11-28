#include<iostream>
#include<algorithm>
#include<vector>
#include<set>
#include<stdlib.h>
#include<queue>
#include<math.h>
//#include<pair>

using namespace std;

bool comparator(pair<int,int> p1, pair<int,int> p2)
{
	int st1=p1.first, en1=p1.second;
	int st2=p2.first, en2= p2.second;
	if(en1-st1 != en2-st2)
	    	return en2-st2 > en1-st1;
	else
	    	return st2 < st1;
}

int main(){
  
    int testNo=1,loops,inserts;
    int n,k;
    
    //priority_queue< pair<int,int> , vector< pair<int,int> >, function<bool( pair<int,int> , pair<int,int> ) > > pq(comparator);
    
    pair<int,int> temp;
    int st,en,mid;
    
    cin>>loops;
    
    while(loops--) {
    
	cin>>n>>k;

	inserts=0;
    	priority_queue< pair<int,int> , vector< pair<int,int> >, function<bool( pair<int,int> , pair<int,int> ) > > pq(comparator);
	pq.push(make_pair(1,n));

	while(inserts < k) {
	
		temp = pq.top();
		st = temp.first;
		en = temp.second;
		mid = st + (en -st) /2;
		pq.pop();
		//cout<<"Found interval with st:"<<st<<" , en: "<<en<<" and mid: "<<mid<<endl;
		if(pq.top().first > pq.top().second)
			continue;

	//	cout<<"Inserting in position mid: "<<mid<<endl;
		
		if(mid -1 -st >=0)
			pq.push(make_pair(st,mid-1));
		
		if(en - mid-1 >=0)
			pq.push(make_pair(mid+1,en));
		inserts++;
	}


	cout<<"Case #"<<testNo<<": "<<max(mid-st,en-mid)<<" "<<min(mid-st,en-mid)<<endl;
    	testNo++;
    }
    return 0;
}
