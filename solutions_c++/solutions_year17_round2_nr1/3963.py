#include <bits/stdc++.h>
#include <iomanip>
using namespace std;

int compare(const void *a,const void *b) {
    return ((const int *)a)[0] - ((const int *)b)[0];
}

int main() {
	std::ios::sync_with_stdio(false);
	long long int t, n, d, i, j;
	cin>>t;
	for(i=1; i<=t; i++)
	{
	    cin>>d>>n;
	    long long int a[2][n];
	    double b[n];
	    double v;
	    v = 100000.0;
	    for(j=0; j<n; j++)
	    {
	        cin>>a[0][j]>>a[1][j];
	        b[j] = 1.0*(d - a[0][j])/a[1][j];
	        //cout<<b[j]<<"\n";
	    }
	    qsort(a, n, sizeof(a), compare);
	    for(j=n-2; j>=0; j--)
	    {
	        if(b[j]<b[j+1])
	            b[j] = b[j+1];
	    }
	    v = d/b[0];
	    cout<<"Case #"<<i<<": "<<fixed<<setprecision(6)<<v<<"\n";
	}
	return 0;
}
