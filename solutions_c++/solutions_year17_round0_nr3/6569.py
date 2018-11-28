#include <bits/stdc++.h>

#define Rahul Vats jbmr_kkd

using namespace std;
int main() 
{
	int t;
	cin>>t;
	for (int i=1;i<=t;i++)
	{
	    int n,k,max;
	    cin>>n>>k;
	    vector<int> vec;
	    vec.push_back(n);
	    while(k>1)
	    {
	        vector<int>::iterator it=max_element(vec.begin(),vec.end());
	        int max=*it;
	        vec.erase(it);
	        vec.push_back((max-1)/2);
	        vec.push_back(max-1-(max-1)/2);
	        k--;
	    }
	    max=*max_element(vec.begin(),vec.end());
	    cout<<"Case #"<<i<<": "<<max-1-(max-1)/2<<" "<<(max-1)/2<<endl;
	}
	return 0;
}
