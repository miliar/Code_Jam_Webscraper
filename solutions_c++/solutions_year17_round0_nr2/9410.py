#include<bits/stdc++.h>

using namespace std;

int getans(int n)
{
  int next_digit=n%10;

  n=n/10;

 while(n)
 {
   int digit=n%10;

     n=n/10;
   if(digit>next_digit)

       return 0;
   else
        next_digit=digit;

 }

 return 1;

}

int main()
{
 freopen("B-small-attempt0.in","r",stdin);
 freopen("rakesh1.txt","w",stdout);
 int t,i,j;

  cin>>t;

for(i=1;i<=t;i++)
 {
    int n;

    cin>>n;

 for(j=n;j>=1;j--)
    {

      if(getans(j))
      {
        cout<<"case #"<<i<<":"<<" "<<j<<"\n";

         break;
      }

    }
 }
return 0;
}
