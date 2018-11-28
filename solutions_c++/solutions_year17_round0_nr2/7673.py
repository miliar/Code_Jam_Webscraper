#include<iostream>
#include<math.h>
using namespace std;
int tidy(long long int n)
{
  int prev_digit=n%10;
  int power=1;
  if(prev_digit==0) return false;
  n=n/10;
  while(n)
  {
      long long int next_digit=n%10;
      if(next_digit<=prev_digit)
      {
        n=n/10;
        prev_digit=next_digit;
        power++;
      }
      else
      {
        return power;
      }
  }
  return -1;
}
int main()
{
  long long int t,n,i,res[100],pos=0;
  cin>>t;
  while(t--)
  {
    cin>>n;
    for(i=n;i>=1;i--)
    {
      int temp=tidy(i);
      if(temp==-1) //if the number is tidy
      {
        res[pos]=i;
        pos++;
        break;
      }
      else //if the numbe is not tidy
      {
        i-=i%(long long int)pow(10,temp);
      }
    }

    if(i<=0){ res[pos]=1; pos++;}
  }
  for(i=0;i<pos;i++)
  {
    cout<<"Case #"<<i+1<<": "<<res[i]<<endl;
  }
  return 0;
}
