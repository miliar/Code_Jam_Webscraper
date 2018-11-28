using namespace std;
#include<iostream>
#include<stdio.h>
 int  fun(int n)
    { int a,b;
     if(n<10)
     { return 1; }
     else
     {  while(n>0)
          {
            a=n%10;
            n=n/10;
            b=n%10;
              if(a<b)
                {  return 0; break; }
          }
      }
return 1;
    }
int main()

{freopen("input.in","r",stdin);
freopen("tidynumbers.out","w",stdout);

    int i,t,a,b,n,r;
  cin>>t;
  for(int z=1;z<=t;z++){

    cin>>i;
  for(int j=0;j<i;j++)
  {
      r=fun(i); i--;
      if(r==1)
      {
          cout<<"Case #"<<z<<": "<<i+1<<endl; break;
      }
     // else{cout<<"nomatch"<<endl;}
  }
//return 0;
}
}
