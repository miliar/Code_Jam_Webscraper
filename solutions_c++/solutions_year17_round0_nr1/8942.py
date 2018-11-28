#include <iostream>
#include <string>

using namespace std;

int flips(int a[], int M, int N)
{
  int s[M]; 
  for(int i=0;i<M;++i)
   s[i] = 0;
  int sum=0, ans=0;
  for(int i=0;i<M;++i)
  {
    s[i] = (a[i]+sum)%2 != 0;
    sum += s[i] - (i>=N-1?s[i-N+1]:0);
    ans += s[i];
    if(i>M-N and s[i]!=0) return -1;
  }
  return ans;
}


int main()
{
   int t,k,y,l;
   string s;
   cin>>t;
   for(int i=1;i<=t;++i)
   {
       cin>>s>>k;
       int l = s.length();
       int a[l];
       for(int j=0;j<l;++j)
       {
           if(s[j]=='-') a[j]=1;
           else
           a[j]=0;
       }
        y = flips(a,l,k);
        cout<<"Case #"<<i<<": ";
        if(y== -1)
        cout<<"IMPOSSIBLE"<<endl;
        else
        cout<<y<<endl;
   }
   return 0;
}



