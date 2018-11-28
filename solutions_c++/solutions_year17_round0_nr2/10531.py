//Pogram for tidy number
#include<iostream>
//#include<conio>
using namespace std;
int main()
{
  //clrscr();
  int T,i,flag=1,a,b;
  unsigned long long N,n1;
  unsigned long long ans[100]={0};
  cout<<"Please enter the number of terms: \n";
  cin>>T;
  for(i=0;i<T;i++)
  {
    cin>>N;
    do
    {
      n1=N;
      b=n1%10;
      n1=n1/10;
      do
      {
	a=n1%10;
	n1=n1/10;
	if(b<a)
	{
	  flag=0;
	  break;
	}
	b=a;
      } while(n1>0);
      n1=N;
      if(flag==1)
      {
	ans[i]=N;
	break;
      }
      else
      {
	flag=1;
	N=n1-1;
      }
    } while(N>0 || flag==1);
  }
  //clrscr();
  for (i=0;i<T;i++)
    cout<<"Case #"<<i+1<<": "<<ans[i]<<endl;
  //getch();
  return (0);
}


