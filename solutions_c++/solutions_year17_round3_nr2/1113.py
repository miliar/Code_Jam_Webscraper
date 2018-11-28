
#include <bits/stdc++.h>
#define mp make_pair
#define pb push_back
//const double PI = 3.141592653589793238462643383279502884; 
using namespace std;

typedef vector<int> vi;
typedef long long int lli;
typedef vector<lli> vli;
typedef pair<int, int> pii;

void foo()
{
    int aj , ac;
    cin>>aj>>ac;

    int x[aj][2];
    int y[ac][2];

    int i;

    for(i=0;i<aj;i++)
      cin>>x[i][0]>>x[i][1];


    for(i=0;i<ac;i++)
      cin>>y[i][0]>>y[i][1];    
    

    if(aj<2 && ac<2)
    {
      cout<<"2\n";
      return;
    }

    int t0, t1;
    int g1, g2;
    if(aj==2)
    {
        if(x[0][0]>x[1][0])
        {
          t0 = x[0][0];
          x[0][0] = x[1][0];
          x[1][0] = t0;

          t1 = x[0][1];
          x[0][1] = x[1][1];
          x[1][1] = t1;          

        }

        g1 = x[0][1] + (1440 - x[1][0]);
        g2 = x[1][1] - x[0][0];

        if((g1<=720) || (g2<=720))
        {
          cout<<"2\n";
          return;
        }

        cout<<"4\n";
        return;
    }
    if(ac==2)
    {
      if(y[0][0]>y[1][0])
        {
          t0 = y[0][0];
          y[0][0] = y[1][0];
          y[1][0] = t0;

          t1 = y[0][1];
          y[0][1] = y[1][1];
          y[1][1] = t1;    
           
        }

        g1 = y[0][1] + (1440 - y[1][0]);
        g2 = y[1][1] - y[0][0];

        if((g1<=720) || (g2<=720))
        {
          cout<<"2\n";
          return;
        }

        cout<<"4\n";
        return;
    }





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
