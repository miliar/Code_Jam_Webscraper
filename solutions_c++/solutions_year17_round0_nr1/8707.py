#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;
const int INF = 20000000;


int flips(int a[], int M, int N, int want) {
  int s[M]; for(int i=0,_n=M; i<_n; ++i) s[i] = 0;
  int sum=0, ans=0;
  for(int i=0,_n=M; i<_n; ++i)
    {
    s[i] = (a[i]+sum)%2 != want;
    sum += s[i] - (i>=N-1?s[i-N+1]:0);
    ans += s[i];
    if(i>M-N and s[i]!=0) return INF;
  }
  return ans;
}

int main()
{
    int t=0,i=0,k=0,l=0,a[10000];
    char str[10000];
    cin>>t;
    for(int i=0;i<t;i++)
    {

        cin>>str;
        cin>>k;
        l=strlen(str);
        for(int j=0;j<l;j++)
        {
            if(str[j]=='+')
            a[j]=1;
            else
             a[j]=0;
        }
        if(flips(a, l, k, 1)==20000000)
            cout<<"Case #"<<i+1<<": "<<"IMPOSSIBLE"<<"\n";
        else

            cout<<"Case #"<<i+1<<": "<<flips(a, l, k, 1)<<"\n";

    }
    return 0;
}
