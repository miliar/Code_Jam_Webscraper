#include <bits/stdc++.h>
#define mod 1000000007
#define mp make_pair
#define pb push_back
#define ll long long
#define rep(i,n) for(i=0;i<n;i++)
#define repd(i,n) for(i=1;i<=n;i++)
#define gc getchar_unlocked
#define pc putchar_unlocked
#define pi 3.14159265358979323846264
using namespace std;



int main() {
	freopen("abc.in","r",stdin);
freopen("outputC.txt","w",stdout);

int t,i;;

cin>>t;
	repd(i,t)
	{
	    long long int n,k,x,sub,div,q,sz,pos;
	    cin>>n>>k;
	    x = log2(k);
	    sub = pow(2,x)-1;
	    n = n - sub;
	    pos = k - pow(2,x)+1;
	    div = pow(2,x);
	    q = n - (n/div)*div;
	 //   cout<<x<<" "<<sub<<" "<<n<<" "<<pos<<" "<<div<<" "<<q<<endl;
	    if(q>=pos)
            sz = n/div +1 ;
        else
            sz = n/div;
        if(sz%2==0)
	        cout<<"Case #"<<i<<": "<<sz/2<<" "<<sz/2-1<<endl;
        else
             cout<<"Case #"<<i<<": "<<sz/2<<" "<<sz/2<<endl;

	}
	// your code goes here
	return 0;
}
