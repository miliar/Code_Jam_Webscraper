#include <bits/stdc++.h>
using namespace std;
#define mod 1000000007
#define INF 1000000000
#define LINF 1000000000000000000  
typedef long long 		ll;
typedef vector<int>		vi;
typedef pair<int, int>		ii;
typedef vector<ii>		vii;
typedef set<int>		si;
typedef map<string, int>	msi;
#define REP(i, a, b)  for (int i = int(a); i <= int(b); i++)
#define TRvi(c, it)  for (vi::iterator it = (c).begin(); it != (c).end(); it++)
#define TRvii(c, it)  for (vii::iterator it = (c).begin(); it != (c).end(); it++)
#define TRmsi(c, it)  for (msi::iterator it = (c).begin(); it != (c).end(); it++)
#define pb push_back
#define mk make_pair
int main()
{
	ios_base::sync_with_stdio(false);
	int t,t_case;
	cin>>t;
	REP(t_case,1,t)
	{
		ll l,r,temp=1,rem,q,n,king,extra,block;
		cin>>l>>r;
		if(r==1)
		 n=l-1;
		else{
		while(r>=(2*temp))
		temp*=2;
		block=(l+1-temp)/temp;
		extra=(l+1-temp)-(block*temp);
		rem=r+1-temp;
		q=r/(temp-1);
		if(rem<=extra)
		{
			n=block+1;
		}
		else
		n=block;
		n--;}
		cout<<"Case #"<<t_case<<": "<<(n/2)+(n%2)<<" "<<n/2<<"\n";
		
	}
	return 0;
}
