#include<bits/stdc++.h>
using namespace std;       // Author @MD.Chand Alam

bool digit(unsigned long long int n)
{
   unsigned long long int l=n;
   unsigned long long int c=0,comp1,comp2;
   comp1=l%10;
   bool ans=true;
   while(l!=0)
   {
       c++;
       unsigned long long int a=l%10;
       if(c==1)
       {
           if(a==0)
            {
                ans=false;
                break;
            }

       }
       else
       {
           comp1=l%10;
           unsigned long long int f=l;
           f=f/10;
           comp2=f%10;
           if(comp2>comp1)
           {
               ans=false;
               break;
           }
        l=l/10;
       }
   }
  if(ans==false)
    return false;
  else
    return true;
}


int main()
{
    freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );

    int t;
    cin>>t;

    for(int cs=1;cs<=t;cs++)
    {

        unsigned long long int n,an;
        cin>>n;
        unsigned long long int s=n;
        if(n<10)
            cout<<"Case #"<<cs<<": "<<n<<endl;
        else
        {
        while(s>0)
        {
           if(digit(s))
           {
            an=s;
            break;
           }
          s--;
        }
            cout<<"Case #"<<cs<<": "<<an<<endl;
        }
    }
    return 0;
}

