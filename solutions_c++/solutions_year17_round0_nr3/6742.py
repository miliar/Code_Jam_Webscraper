#include <iostream>
#define ull unsigned long long
#include <vector>
#include <algorithm>
using namespace std;
vector<ull> v;
void gen(ull n)
{
    if(n==0)
    return;
    else
    {
        v.push_back(n);
        ull l=(n-1)/2;
        ull r=(n-1-l);
        gen(r);
        gen(l);
    }
}
int main() 
{
	ull t;
	cin>>t;
	for (ull test=1;test<=t;test++)
	{
	    ull n,k;
	    cin>>n>>k;
	    gen(n);
	    sort(v.begin(),v.end());
	    reverse(v.begin(),v.end());
	    ull l=(v[k-1]-1)/2;
	    ull r=v[k-1]-1-l;
	    cout<<"Case #"<<test<<": "<<r<<" "<<l<<endl;
	    v.clear();
	}
	return 0;
}
