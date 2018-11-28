#include <iostream>
#include<bits/stdc++.h>
using namespace std;
vector<int> r;
vector<int> l;
   ifstream fin("C-small-1-attempt3.in");
    ofstream fout("output_file.out");
void putt(int q)
{
   int  o=q;
   o--;
   int pp=0;
    for(int i=o;i>=0;i--)
    {
        if(r[i]==-1)
        break;
        r[i]=pp;
pp++;

    }
    o=o+2;
    pp=0;
     for(int i=o;i<l.size();i++)
    {
        if(l[i]==-1)
        break;
        l[i]=pp;
pp++;

    }}

int main()
{
int i;
fin>>i;
int cc=1;
while(i--)
{
   r.clear();
   l.clear();
   int n,k;
   fin>>n;
   fin>>k;

   r.push_back(-1);
   l.push_back(-1);
   int u=n,s=0;
   while(u--)
   {  r.push_back(n-s-1);
      l.push_back(s++);

   }
   l.push_back(-1);
   r.push_back(-1);
   int maxxa=-100,maxxb=-100,a,b;
   while(k--)
   {maxxa=-100;
   maxxb=-100;
int aa;
       for( aa=1;aa<=n;aa++)
       {
          if(l[aa]<0||r[aa]<0)
           continue;
           a=min(l[aa],r[aa]);
           if(a>maxxa)
           {
               maxxa=min(l[aa],r[aa]);
               maxxb=max(l[aa],r[aa]);
               b=aa;

           }
         else  if(a==maxxa)
           {
               if(max(l[aa],r[aa])>maxxb)
               {
                   maxxb=max(l[aa],r[aa]);
                   b=aa;
               }

           }
       }
       l[b]=-1;
       r[b]=-1;
putt(b);
   }
   fout<<"Case #"<<cc <<": " <<maxxb << " "<<maxxa<<"\n";
   cc++;
}
return 0;

    }
