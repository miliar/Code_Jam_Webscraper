#include <iostream>
#include <queue>
#include <stdlib.h>
#include <bits/stdc++.h>

using namespace std;

int main() {
	// your code goes here
	int t;
	
	cin>>t;
	for(int it=1;it<=t;it++)
	{
	    double tim=0;
	    double timg=0;
	    int d,n;
	    cin>>d>>n;
	    std::priority_queue< pair<int, int > > q;
	    
	    for(int i=0;i<n;i++)
	    {
	        int a,b;
	        cin>>a>>b;
	        q.push(make_pair(a,b));
	        //cout<<q.top().first<<q.top().second;
	    }
	    while(!q.empty())
	    {
	        int dist1=0, dist2=0, speed1=0, speed2=0;
	        double x=0;
	        dist1= q.top().first;
	        speed1= q.top().second;
	        q.pop();
	        if(!q.empty())
	        {
	        dist2= q.top().first;
	        speed2= q.top().second;
	        if(speed2>speed1)
	        {
	            x= ((speed2*dist1)- (speed1*dist2))/(double)(speed2-speed1);
	            if(x>d)
	            {
	                tim= (d-dist2)/(double)speed2;
	                if(tim>timg)
	                    timg=tim;
	            }
	            else
	            {
	                tim= (d-dist1)/(double)speed1;
	                if(tim>timg)
	                    timg=tim;
	            }
	        }
	        else
	        {
	            tim= (d-dist2)/(double)speed2;
	            if(tim>timg)
	                    timg=tim;
	        }
	        }
	        else
	        {
	            tim= (d-dist1)/(double)speed1;
	            if(tim>timg)
	                    timg=tim;
	        }
	    }
	    double speed= d/(double)timg;
	    //cout<<"Case #"<<it<<": "<<speed<<endl;
	    printf("Case #%d: %.6f\n",it,speed);
	    
	}
	return 0;
}
