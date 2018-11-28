
#include <bits/stdc++.h>
#define mp make_pair
#define pb push_back
using namespace std;

typedef vector<int> vi;
typedef long long int lli;
typedef vector<lli> vli;
typedef pair<int, int> pii;

void foo()
{

   double d;
   int n;
   double x ,rem, t , tmax=0 , speed;
   cin>>d>>n;
   while(n--)
   {
   		cin>>x>>speed;
   		rem = (d-x);
   		if(rem<0) rem=0;

   		t= rem/speed;

   		if(t>tmax)
   			tmax = t;
   }

   speed = d/tmax;

   printf("%.6f\n", speed);
}


int main()
{
    int t;
    cin>>t;
    int i;
    for(i=1;i<=t;i++)
    {
        cout<<"Case #"<<i<<": ";
        foo();
    }

}
