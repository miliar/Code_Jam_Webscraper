#include <bits/stdc++.h>
using namespace std;

#define min(a,b) ((a<b) ? (a) : (b))
#define max(a,b) ((a>b) ? (a) : (b))
#define ll long long
#define FOR(i,n) for(int i=0;i<n;i++)
#define FORL(i,n) for(long long i=0;i<n;i++)
#define MOD 1000000007
#define PI 3.141592653589
#define fastio ios_base::sync_with_stdio(false); cin.tie(0);
ll log2(ll n)
{
	ll ans=0;
	while(n!=0)
	{
		n/=2;
		ans++;
	}
	return ans;
}
int main()
{
    fastio
    freopen("input_3.txt", "r", stdin);
    freopen("output_3.txt", "w", stdout);

    int test;
   	int ans=0;
   	string s;
   	int i,j,k,n;
    cin>>test;
    bool check;
    for(int t=1;t<=test;t++)
    {
       

       	ll n,k;
       	cin>>n>>k;
       	ll x=0;
       	int n1=log2(n),k1=log2(k);
       	//cout<<n1<<" "<<k1<<endl;
       	ll p1=n,p2=0,f1=1,f2=0;
       	ll _p1,_p2,_f1,_f2;
       	for(int i=1;i<k1;i++)
       	{
       		_p1 = (p1-1)/2;
       		_p2 = (p1/2);
       		_f1=_f2=f1;
       		if(_p1==_p2)
       		{
       			_f1+=_f2;
       			_p2=0;
       			_f2=0;
       		}

       		if(f2!=0)
       		{
       			if(_p1 == ((p2-1)/2))
       				_f1+=f2;
       			else
       			{
       				_p2 = (p2-1)/2;
       				_f2+=f2;
       			}


       			if(_p1 == (p2/2))
       				_f1+=f2;
       			else
       			{
       				_p2 = (p2/2);
       				_f2+=f2;
       			}
       		}

       		p1=_p1;
       		p2=_p2;
       		f1=_f1;
       		f2=_f2;

       		x*=2;
       		x++;

       	}

       	ll e = k-x;
       	e--;
       	if(p1<p2)
       	{	
       		//cout<<p1<<" "<<p2<< " swap " ;
       		swap(p1,p2);
       		swap(f1,f2);
       		//cout<<p1<<" "<<p2;
       	}

       	f1-=min(f1,e);
       	if(f1==0)
        	cout<<"Case #"<<t<<": "<<p2/2<<" "<<(p2-1)/2<<endl;
        else
        	cout<<"Case #"<<t<<": "<<p1/2<<" "<<(p1-1)/2<<endl;
    }
    return 0;
}

