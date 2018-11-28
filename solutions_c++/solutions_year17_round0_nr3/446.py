#include <bits/stdc++.h>
using namespace std;
#define rep(a,b,c) for(int a=b;a<c;++a)
#define repeq(a,b,c) for(int a=b;a<=c;++a)
#define debug(x) cerr<<(#x)<<": "<<x<<endl
typedef long long ll;

int main()
{
	ios::sync_with_stdio(false);
    cin.tie(NULL);
	int T;
	cin >> T;
	repeq(t,1,T)
	{
		ll n, k;
		cin >> n >> k;

		ll a = n, x=1, y=0;
		while(k>x+y)
		{
			k-=x+y;
			if(a%2==0)
				y = 2*y+x;
			else
				x = 2*x+y;
			a = (a-1)/2;
		}
		ll fin;
		if(k<=y)
			fin = a+1;
		else
			fin = a;
		
		cout << "Case #" << t << ": " << (fin-1)-(fin-1)/2 << " "<< (fin-1)/2 << endl;
	}
	return 0;
}
