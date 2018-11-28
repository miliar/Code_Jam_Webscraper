#include <bits/stdc++.h>
using namespace std;
double pi = 3.141592653589793238462643383279502884197169399375105820974944592307816406286;
bool myfun(const pair<double,double> &a, const pair<double,double> &b)
{
    return a.first > b.first;
}
double Find(vector<pair<double,double> > &A, int n,int k)
{
    double MaxArea = 0;
    for(int i=0;i<n;i++)
    {
        int count = 1;
        bool flag = false;
        double rb = A[i].second;
        double Area = pi * rb *rb + A[i].first;
        for(int j=0;j<n;j++)
        {
            double r = A[j].second;
            if(i!=j && count < k && r <= rb)
            {
                Area += A[j].first;
                count++;
            }
        }
        if(count==k && MaxArea < Area)
        {
            MaxArea = Area;
        }
    }
    return MaxArea;
}
int main() 
{
	int T,Case = 1;
	cin >> T;
	while(T--)
	{
	    int n,k;
	    cin>>n>>k;
	    vector<pair<double,double> > A;
	    for(int i=0;i<n;i++)
	    {
	        int r,h;
	        cin>>r>>h;
	        A.push_back(make_pair(2*pi*r*h,r));
	    }
	    sort(A.begin(),A.end(),myfun);
	    printf("Case #%d: %0.9lf\n",Case,Find(A,n,k));
	    
	    Case++;
	}
	return 0;
}
