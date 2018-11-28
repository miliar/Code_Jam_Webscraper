#include<iostream>
using namespace std;
int main()
{
  int t;
  cin>>t;
  int testcases[t];
  for(int t2=0;t2<t;t2++)
    cin>>testcases[t2];
  for(int t1=0;t1<t;t1++)
  {
  int n;
  n=testcases[t1];
  for(int i=n;i>=1;i--)
  {
      int flag=0;
      int temp=i;
      int no_of_digits=0;
      while(temp!=0)
      {
          temp=temp/10;
          no_of_digits++;
      }
      temp=i;
      int tidy[no_of_digits];
      int t=(no_of_digits-1);
      while(temp!=0)
      {
          tidy[t]=temp%10;
          t--;
          temp=temp/10;
      }
      for(int j=0;j<no_of_digits;j++)
      {
        int temp1=tidy[j];
        for(int k=j+1;k<no_of_digits;k++)
        {
            if(tidy[k]<temp1)
            {
                flag=1;
            }
        }
      }
      if(flag==0)
      {
          cout<<"Case #"<<(t1+1)<<":"<<" ";
          for(int s=0;s<no_of_digits;s++)
          {
              cout<<tidy[s];
          }
          cout<<"\n";
          i=0;

      }

  }
}
return 0;
}
