#include<bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin>>t;
	for(int j=1;j<=t;j++)
	{
	    unsigned long long n,n1;
	    cin>>n;
	    vector<int> v;
	    n1=n;
	    cout<<"Case #"<<j<<": ";
	    if(n<10) cout<<n<<endl;
	    else
	    {
	        while(n1>0)
	        {
	            v.push_back(n1%10);
	            n1/=10;
	        }
	        for(int i=v.size()-1;i>0;i--)
	        {
	            if(v[i]>v[i-1])
	            {
	                v[i]--;
	                for(int l=i-1;l>=0;l--) v[l]=9;
	                i+=2;
	            }
	        }
	        for(int k=v.size()-1;k>=0;k--)
	        {
	            if(k==v.size()-1&&v[k]==0) continue;
	            cout<<v[k];
	        }
	        cout<<endl;
	    }
	}
	return 0;
}

