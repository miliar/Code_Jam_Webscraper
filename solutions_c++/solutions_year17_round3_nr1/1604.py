#include <bits/stdc++.h>
using namespace std;

#define pi 3.141592653589793238462643383279502884197169399375105820974944592307816406286

bool mycomapre(const pair<double,double> &l,const pair<double,double> &r)
{
    return l.first > r.first ;
}

int main() {
	int T;
	cin>>T;
	
	for(int j = 1;j<=T;j++)
	{
	    int N,K;
	    cin>>N>>K;
	    vector<pair<double,double> > A(N);
	    for(int i=0;i<N;i++)
	    {
	        double r,h;
	        cin>>r>>h;
	        A[i] = make_pair(2*pi*r*h,r);
	    }
	    
	    sort(A.begin(),A.end(),mycomapre);
	     double area = 0,ans = 0;
	     
	    for(int i=0;i<N;i++)
	    {
	        int j =0,count = 1;
	        area = A[i].first + pi * A[i].second * A[i].second;
	        while(j < N && count < K)
	        {
	            if(i != j)
	            {
	                if(A[j].second <= A[i].second)
	                {
	                    count++ ;
	                    area += A[j].first;
	                }
	            }
	            j++ ;
	        }
	        if(ans < area && count == K)
	        {
	            ans = area;
	        }
	    }
	    
	    
	    cout<<"Case #"<<j<<": ";
	    printf("%.9lf\n",ans);
	}
	return 0;
}
