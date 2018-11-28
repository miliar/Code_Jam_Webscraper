#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main()
{
   int t,m=1;
   ofstream file;
    ifstream input;
    file.open("C-output1.txt");
    input.open("C-small-2-attempt3.in");
   input>>t;
   while(m<=t)
   {
       int n,k;
       input>>n>>k;
      // deque <int> q;
       priority_queue <int> q;
       int l,r;
       if(n%2==0&&n!=0)
       {
           l=n/2;
           r=(n/2)-1;
           q.push(n/2);
           q.push((n/2)-1);
       }
       else
       {
           l=n/2;
           r=(n/2);
           q.push(n/2);
           q.push(n/2);
       }
       k--;
       while(k>0)
       {
           int a=q.top();
           q.pop();
           if(a%2==0&&n!=0)
           {
            l=a/2;
            r=(a/2)-1;
            q.push(a/2);
            q.push((a/2)-1);
           }
           else
           {
            l=a/2;
           r=(a/2);
            q.push(a/2);
           q.push(a/2);
           }
           k--;
       }
      /* int b,c;
       b=q.back();
       q.pop_back();
       c=q.back();
       q.pop_back();*/
       file<<"Case #"<<m<<": "<<max(l,r)<<" "<<min(l,r)<<endl;
       while(!q.empty())
        q.pop();
       m++;
   }
    return 0;
}
