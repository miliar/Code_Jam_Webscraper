#include<iostream>
#include<fstream>
using namespace std;

bool compute(int num)
  {
    int j=0,a[20];

    while(num>0)
    {
      a[j]=num%10;
      num=num/10;
      j++;
    }
  for(int k=0;k<j-1;k++)
   {
     if(a[k]<a[k+1])
       return false;
   }
   return true;
}
int main()
{
    ifstream fin("tiny_number.in");
    ofstream fout("tiny_number.out");
    int t,n;
    int tidy_no;

    fin>>t;

  for(int x=1;x<=t;x++)
  {
    fin>>n;
    for(int i=n;i>0;i--)
    {
       if(compute(i))
       {
           fout<<"Case #"<<x<<": "<<i<<endl;
           break;
       }
    }
  }
return 0;
}
