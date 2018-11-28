#include<bits/stdc++.h>

using namespace std;
int count1;
void solve()
{
  cout << "Case #" << count1 <<":" << '\n';
  count1++;
   int r,c;
   cin >> r >> c;
   string a[r];
   for(int i=0;i<r;i++)
   {
      cin >> a[i];
   }
   for(int i=0;i<r;i++)
   {
       for(int j=0;j<c;j++)
       {
           if(a[i][j]!='?')
           {
               for(int k=i-1;k>=0;k--)
               {
                   if(a[k][j]!='?')
                   break;
                   else
                   a[k][j] = a[i][j];
               }
               for(int k = i+1;k<r;k++)
               {
                   if(a[k][j]!='?')
                   break;
                   else
                   a[k][j] = a[i][j]; 
               }
           }
       }
   }
   for(int i=0;i<r;i++)
   {
       for(int j=0;j<c;j++)
       {
           if(a[i][j] != '?')
           {
                for(int k=j-1;k>=0;k--)
               {
                   if(a[i][k]!='?')
                   break;
                   else
                   a[i][k] = a[i][j];
               }
               for(int k =j+1;k<c;k++)
               {
                   if(a[i][k]!='?')
                   break;
                   else
                   a[i][k] = a[i][j]; 
               }     
           }
       }
   }
   for(int i=0;i<r;i++)
   {
       cout << a[i] << '\n';
   }
}

int main()
{   count1 = 1;
    ios :: sync_with_stdio(false);
    int t;
    cin >> t;
    while(t--)
    solve();
}