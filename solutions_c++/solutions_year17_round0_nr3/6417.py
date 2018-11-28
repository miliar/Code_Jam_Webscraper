#include <iostream>
#include<stdio.h>
#include<algorithm>
#include<vector>
using namespace std;

int main() {
	// your code goes here
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;i++)
	{
	    int n,k;
	    scanf("%d %d",&n,&k);
	    int pos=0,flag=0;
	    vector<int>v;
	    v.push_back(n/2);
	    v.push_back(n-n/2-1);
	    if(k!=1)
	    sort(v.begin(),v.end());
	    int x=1;
	    while(x!=k)
	    {
	        int temp=v[v.size()-1];
	        //cout<<x<<" "<<temp<<"\n";
	        v.erase(v.begin()+v.size()-1);
	        v.push_back(temp/2);
	        v.push_back(temp-temp/2-1);
	        if(x!=k-1)
	        sort(v.begin(),v.end());
	        x++;
	    }
	    printf("Case #%d: %d %d\n",i+1,v[v.size()-2],v[v.size()-1]);
	}
	return 0;
}
