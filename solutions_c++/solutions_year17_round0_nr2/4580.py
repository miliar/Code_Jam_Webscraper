#include<bits/stdc++.h>
using namespace std;
int main()
{
    ifstream cin("codein.txt");
    ofstream cout("codeout.txt");
     int t,i;
     cin>>t;
     i=0;
     while(i<t)
     {
         vector<int> A;
         string ch;
         cin>>ch;
         int n,g;
         bool flag=0;
         n=ch.size();
         for(int j=0;j<n;j++)
         {
             g=int(ch[j])-48;
             A.push_back(g);
         }
         for(int j=ch.size()-1;j>0;j--)
         {
             if(A[j]==A[j-1] && A[j]==0)
                A[j]=9;
             else if(A[j]<A[j-1])
             {
                 A[j]=9;
                 A[j-1]-=1;
             }
         }
             n--;
         do
         {
         for(int j=ch.size()-1;j>0;j--)
         {
            if(A[j]<A[j-1])
             {
                 A[j]=9;
             }
         }
         }while(n--);
         cout<<"case #"<<i+1<<": ";
         for(int j=0;j<ch.size();j++)
         {
             if(A[j])
             cout<<A[j];
         }
         cout<<endl;
         i++;
     }
    return 0;
}
