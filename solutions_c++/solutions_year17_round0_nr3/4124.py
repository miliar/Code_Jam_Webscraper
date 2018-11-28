#include <bits/stdc++.h>
using namespace std;
void fun(long long n,long long k)
{
    priority_queue<long long> Q;
    Q.push(n);
    long long l,r,size;
    for(int i=0;i<k;i++)
    {
        size = Q.top();
        Q.pop();
        l = (size-1)/2;
        r = size - 1 - l;
        Q.push(l);
        Q.push(r);
    }
    cout<<max(l,r)<<" "<<min(l,r)<<endl;
}
int main() 
{
	int T,Case = 1;
	cin >> T;
	while(T--)
	{
	    long long n,k;
	    cin>>n>>k;
	    cout<<"Case #"<<Case<<": ";
	    fun(n,k);
	    
	    Case++;
	}
	return 0;
}
