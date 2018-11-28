#include<bits/stdc++.h>
#include <string>
using namespace std;


int main(){
	
	ifstream input("C-small-1-attempt0.in");//C-small-2-attempt0
	ofstream output;
	output.open("output_C.out");
	string line;
	getline( input, line );
	long long int t,m=0;
	stringstream ss;
    ss<<line;
    ss>>t; 
	while( getline( input, line ))
	{
		m++;
		stringstream s;
		s<<line;
		long long int i,l,r,j,n,k,max1,max2,index1,index2;
     	
     	s>>n>>k;
     	
     	set<long long int> num;
   	num.insert(0);
   	num.insert(n+1);
   	set<long long int> :: iterator left,right;
   	left=num.begin();
   	right=left;
   	right++;
    	     	
    for(i=0;i<k;i++){
    	j=1;
    	left=num.begin();
   		right=left;
   		right++;
    	while(*right==j){
    		left++;
    		right++;
    		j++;
		}
		l=j-1-*left;
    	r=*right-1-j;
    	index1=j;
    	index2=j;
    	max1=min(l,r);
    	max2=max(l,r);
    	for(;j<=n;j++){
    		
    		if(*right==j){
    			left++;
    			right++;
    			continue;
			}
    		
			l=j-1-*left;
	    	r=*right-1-j;
	    	//cout<<l<<" "<<r<<endl;
    		if(min(l,r)==max1){
    			if(max(l,r)>max2){
   	 			max2=max(l,r);
    				index2=j;
				}
			}
    	 	else if(min(l,r)>max1){
     			max1=min(l,r);
     			index1=j;
	     		max2=max(l,r);
    	 		index2=j;
			}
				 
		}
     	num.insert(index2);
	}
     	
    left=num.begin();
   	while(*left<index2){
		left++;
	}
   	right=left;
   	right++;
   	left--;
   	l=index2-1-*left;
   	r=*right-index2-1;
   	cout<<"max is "<<max(l,r)<<endl;
   	cout<<"min is "<<min(l,r)<<endl;
   	cout<<"index is "<<index2<<endl;
     	
	output<<"Case #";
		output<<m;
		output<<": ";
		output<<max(l,r);
		output<<" ";
		output<<min(l,r);
		output<<"\n";
	
	}				
	input.close();
	output.close();
	return 0;
}
