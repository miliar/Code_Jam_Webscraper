#include<iostream>
#include <bits/stdc++.h>
using namespace std;


int main() {
	int t;
	long long int n,m,ele,h,remaining,size_q;
	pair<long long int,long long int> p;
	cin>>t;
	for(int k=0;k<t;k++){
	    cin>>n>>m;
	    priority_queue<long long int> q;
	    map<long long int,long long int>mappy;
	    q.push(n);
	    mappy[n]=1;
	    long long int prev_i=0;
	    for(long long int i=1;i<m;i=1+i*2){
	        //cout<<"i "<<i<<endl;
	        size_q=q.size();
	        while(size_q--){
	            ele=q.top();
    	        q.pop();
    	        h=ele/2;
    	        if(ele%2==0){
    	            if(mappy.find(h-1)==mappy.end()){
    	                mappy[h-1]=mappy[ele];
    	                q.push(h-1);
    	            }
    	            else mappy[h-1]+=mappy[ele];
    	            
    	            if(mappy.find(h)==mappy.end()){
    	                mappy[h]=mappy[ele];
    	                q.push(h);
    	            }
    	            else mappy[h]+=mappy[ele];
    	        }
    	        else{
    	            if(mappy.find(h)==mappy.end()){
    	                mappy[h]=2*mappy[ele];
    	                q.push(h);
    	            }
    	            else mappy[h]+=2*mappy[ele];
    	        }
	        }
	        prev_i=i;
	        //cout<<"pi "<<prev_i<<endl;
	    }
	    remaining=m-prev_i;
	    ele=q.top();
	    while(remaining>0){
	    	ele=q.top();
	    	remaining-=mappy[ele];
	    	q.pop();
		}
		remaining=0;
		if(ele%2==0){
            cout<<"Case #"<<k+1<<": "<<ele/2<<" "<<max(ele/2-1,remaining)<<endl;
        }
        else{
            cout<<"Case #"<<k+1<<": "<<ele/2<<" "<<ele/2<<endl;
        }
	}
	
	return 0;
}
