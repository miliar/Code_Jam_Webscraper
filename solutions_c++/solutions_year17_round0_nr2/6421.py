#include<iostream>
using namespace std;
int main(void)
{
int t,i;
cin>>t;
for(i=0;i<t;i++)
  {
  long long int n,n1,n2,n3,val,n4,cal,tmp;
  cin>>n;
  n1=n,n2=n,n3=n/10,n4=n;
  int c=0;
  val=0,cal=10,tmp=0;
  while(n4>0)
    {

    if(c==-1)
    {
    val=n1%(cal);
    n1=n1/(cal);
    if(n1%10==0)
    {n1=(n1/10)*10+9;//continue;
    }
    else
    {
    tmp=n1%10;
    n1=(n1/10)*10+tmp;
    }
    n1=n1*(cal)+val;
    c=0;
    }

    if(n2%10<n3%10)
      {
      n1=n1/(cal*10);
      if(n3%10==0)
          {
          c=-1;
          n1=n1*10+9;
          }
      else
          n1=n1*10+(n3%10)-1;
      n1=n1*cal+cal-1;

      }

      n4=n4/10;
      n2=n1/cal;
      n3=n3/10;
      cal=cal*10;
    }
    cout<<"Case #"<<i+1<<": "<<n1<<endl;
  }
return 0;
}
