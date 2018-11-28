#include <bits/stdc++.h>
using namespace std;
struct horse{
	long long k,s;
};
int main(void){
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    long long T;
    cin>>T;
    for(int t=1;t<=T;t++){
    	long long d,n;
    	cin>>d>>n;
    	struct horse h[n];
    	double time[n];
    	for (long long i = 0; i < n; ++i)
    	{
    		cin>>h[i].k>>h[i].s;
    		/* code */
    	}
    	for (int i = 0; i < n; ++i)
    	{
    		h[i].k = d - h[i].k;
    		time[i] = (double)h[i].k/h[i].s;
    		//cout<<time[i]<<endl;
    		/* code */
    	}
    	double max = time[0];
    	//cout<<" time "<<time[0];
    	for(int i=1;i<n;i++){
    		max = max < time[i] ? time[i] : max; 
    	}
    	double ans = d/max;
    	printf("Case #%d: %f\n",t,ans);
    }
}