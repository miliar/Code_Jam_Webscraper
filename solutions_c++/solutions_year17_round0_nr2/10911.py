#include <iostream>
using namespace std;

#include <stdio.h>

#include <algorithm>
#include <string.h>
#include <stack>




int conv (long long k)
{
    int h=1;
    char s[100];
    lltoa(k,s,10);
    for(int j=1;s[j];j++)
    {
        if(s[j-1]>s[j]) return 0;

    }

    return 1;
}

int main()
{
    freopen("B-small-attempt1.in","r",stdin);
    freopen("output_file_name1.out","w",stdout);
   int t,h=0;
   cin>>t;
   for(int i=0;i<t;i++)
   {
       h=0;
       long long n;
       cin>>n ;
       long long k,c;
       for(k=n;h==0;k--) if(conv(k)) { h=1; c=k; break; }
       cout<<"Case #"<<i+1<<": "<<c<<endl;

   }

   return 0;
}

/*
#include <iostream>
using namespace std;

#include <stdio.h>

#include <algorithm>
#include <string.h>
#include <stack>

int compare (const void * a, const void * b)
{
  return ( *(int*)b - *(int*)a );
}

int main()
{
   int t;
   cin>>t;
   for(int i=0;i<t;i++)
   {
       int h,m,h1,m1;
       scanf("%d:%d %d:%d",&h,&m,&h1,&m1);

       int a=((h*60)+m);
       int b=(h1*60)+m1;

       //cout<<a<<" "<<b<<endl;

       int c= b-a;

       int j=1440-b+a;

       if(c-j) cout<<"W\n"; else cout<<"S\n";




   }
   return 0;
}

*/
