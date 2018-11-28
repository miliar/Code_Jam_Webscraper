#include <bits/stdc++.h>
using namespace std;

int main() 
{
	int T,Case = 1;
	cin >> T;
	while(T--)
	{
	    double d,pos,speed,max = 0;
	    int n;
	    cin>>d>>n;
	    for(int i=0;i<n;i++)
	    {
	        cin>>pos>>speed;
	        double t = (d-pos)/speed;
	        if(max < t)
	        max = t;
	    }
	    
	    printf("Case #%d: %.6lf\n",Case,d/max);
	    
	    Case++;
	}
	return 0;
}
