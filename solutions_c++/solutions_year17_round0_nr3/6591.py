#include <bits/stdc++.h>
using namespace std;
int main() {
    int t,T,flag;
    long long int i,j,n,k,max,ans1,ans2;
    cin>>T;
	for(t=1;t<=T;t++)
	{
	    cin>>n>>k;
	    vector<long long int> space;
	    space.push_back(n);
	    i=1;
	    flag=0;
	    while(i<=k){
	        if(space.empty()){flag=1;break;}
	        max=space.front();
	        for(j=0;j<space.size();j++){
	            if(space[j]>max)max=space[j];
	        }
	        for(j=0;j<space.size();j++){
	            if(space[j]==max){
	                space.erase(space.begin()+j);
	                if(max%2==0){ans1=max/2;ans2=ans1-1;}
	                else{ans1=ans2=max/2;}
	                if(ans1!=1 || ans1!=0)space.push_back(ans1);
	                if(ans2!=1 || ans2!=0)space.push_back(ans2);
	                break;
	            }
	        }
	        i++;
	    }
	    if(i<k){
	        printf("Case #%d: 0 0\n",t);
	    }
	    else{
	        printf("Case #%d: %lld %lld\n",t,ans1,ans2);
	    }
	    
	}
	return 0;
}
