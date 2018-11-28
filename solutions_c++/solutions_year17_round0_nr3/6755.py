#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(0);cin.tie(NULL);cout.tie(NULL);
    freopen("C-small-1-attempt2.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,t1=1;
    long long int zz=0;
    cin>>t;
    long long int a[100]={};
    a[0]=1;
    for(int i=1;i<64;i++)
    {
        a[i]=a[i-1]*2;
    }
    while(t--)
    {
        long long int n,k,i,j,l;
        cin>>n>>k;
        multiset<long long int >s;
        multiset<long long int >::iterator itr,itr1;
        
        s.insert(n);
        
        for(i=0;i<k;i++)
        {
        	itr=s.end();
	        itr--;
	        s.insert((*itr-1)/2);
	        s.insert((*itr)/2);
	        s.erase(s.find(*itr));
	        if(i==k-1)
	        {
	        	cout<<"Case #"<<t1<<": ";
	        	t1++;
	        	cout<<max((*itr)/2,(*itr-1)/2)<<" "<<min((*itr)/2,(*itr-1)/2)<<"\n";
			}
		}
    }
    
	return 0;
}

