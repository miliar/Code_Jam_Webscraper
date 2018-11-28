#include <bits/stdc++.h>
using namespace std;
 
#define N 100005
#define fi first
#define se second
#define MOD 1000000007
 
#define pb push_back
 
#define ll long long
 
#define eps 1.0e-7
#define inf 1e9 + 5
#define double long double

#define pp pair<int,int>

void solve(int a[] , int n)
{
	for(int i = 1;i<n;i++)
	{
		if(a[i]<a[i-1])
		{
			for(int j=i;j<n;j++)
				a[j] = 9;
			a[i-1]--;
			solve(a,n);
		}
	}
}


int main()
{
  freopen("input.txt","r",stdin);
  freopen("output.txt","w",stdout);
  int t,i,n,m,k;
  string s ;

  cin>>t ;
  for(int i = 1; i <= t; i++)
  {
  	cin >> s;
  	int n = s.size();
  	int a[n+1];

  	for(int j = 0; j < n; j++){
  		a[j] = s[j] - '0';
  	}

  	solve(a,n);

  
    cout << "Case #" << i << ": ";
    bool f = false;

    for(int j = 0;j<n;j++)
    {

  		if(f==false && a[j]==0) continue;
  		if(a[j]>0) f = true;
  		cout<<a[j];	

  	}

  	cout<<"\n";
    

    }



}