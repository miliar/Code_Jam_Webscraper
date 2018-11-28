#include<iostream>
#include<string>
#include<stdio.h>

using namespace std;

int main()
{
int c=0;

freopen("input_l1.in","r",stdin);
freopen("output_l1.out","w",stdout);
int t,k,i,l;

scanf("%d",&t);

for(int z=1;z<=t;z++)
{
    c=0;
    int n;
    string s;
cin>>s;

cin>>k;


int len=s.length();
int f=0;

for(i=0;i<len;i++)
{
f=0;
  if(s[i]=='+')continue;

  f=1;
  if(k>len-i)
  {
      f=2;
        cout<<"Case #"<<z<<": IMPOSSIBLE"<<endl;//<<
        break;
}

c++;
  for(l=i;l<i+k;l++)
  {

      if(s[l]=='+')
        s[l]='-';
      else
        s[l]='+';
  }
  i--;//=0;
}

if(f==0)
    cout<<"Case #"<<z<<": "<<c<<endl;

}

    return 0;
}
