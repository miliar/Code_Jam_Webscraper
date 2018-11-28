#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<stdio.h>
using namespace std;

typedef struct element{
	long long R,L;
}element;

bool compare(element const &a, element const &b){
	if(a.R-a.L>b.R-b.L)
		return false;
	else if(b.R-b.L>a.R-a.L)
		return true;
	else if(a.L<b.L)
		return false;
	else if(a.L>b.L)
		return true;
	else if(a.R<b.R)
		return false;
	else
		return true;
}

int main(){
	long long t,T,ans;
	long long N,K,max,min;
	//int occupation[1005];
  cin >> T;
  for(t=1;t<=T;++t){
		cin >> N;
		cin >> K;
		//for(long long i=0;i<N+2;++i)occupation[i]=0;
		vector<element> q;
		
		element e;
		e.L=0;
		e.R=N-1;
	
		q.push_back(e);
		max=-1;
		min=N+2;
		while(!q.empty() && K>0){
			e = q.front();
			pop_heap(q.begin(),q.end(),compare);
			q.pop_back();
//			cout << "("<< e.L<<","<<e.R <<")"<<endl;
			if(e.R>=e.L){
				long long pos = e.L+ (e.R-e.L)/2;
				//occupation[pos]=1;
				element left_gap,right_gap;
				--K;
				long long LS = pos-(e.L-1)-1;
				long long RS = (e.R+1)-pos-1;
				if(LS>RS){
					max=LS;
					min=RS;
				}else{
					max=RS;
					min=LS;
				}
/*				if(pos-(e.L-1)>max)max=pos-(e.L-1);
				if((e.R+1)-pos>max)max=(e.R+1)-pos;

				if(pos-(e.L-1)<min)min=pos-(e.L-1);
				if((e.R+1)-pos<min)min=(e.R+1)-pos;*/

				left_gap.L=e.L;
				left_gap.R=pos-1;

				right_gap.L=pos+1;
				right_gap.R=e.R;

				q.push_back(left_gap);
				push_heap(q.begin(),q.end(),compare);

				q.push_back(right_gap);
				push_heap(q.begin(),q.end(),compare);
			}
		}
		/*long long prev=-1;
		occupation[N]=1;;
		for(long long i=0;i<N;++i){
			cout << occupation[i];
			if(occupation[i] && i-prev-1>max){
				//max = i-prev-1; 
			}
			if(occupation[i] && i-prev-1<min){
				//min = i-prev-1;
			}
			if(occupation[i]) prev = i;
		}
		cout << endl;*/
		cout << "Case #"<<t<<": "<<max<<" "<<min<<endl;
	}

}
