#include <bits/stdc++.h>
using namespace std;


int main()
{
     int i,j,p[1000][2],t,mee,maa;
     cin>>t;
     for(i=0;i<t;i++)
     {
         int n,k,a[1003]={0},l,m;
         cin>>n>>k;
         set <int>s;
         set<int>::iterator it;
         s.insert(0);
         s.insert(n+1);
         for(l=0;l<k;l++)
         {
             int mi=-1,ma=-1,m1,m2,m3,m4,m5=-2,m6=-2,in=-1;
             for(m=1;m<=n;m++)
             {
                 if(s.count(m)==0)
                 {
                     it=upper_bound(s.begin(),s.end(),m);
                     it--;
                     m1=(*it);
                     m2=m-m1-1;
                     it++;
                     m3=(*it);
                     m4=m3-m-1;
                     m5=min(m2,m4);
                     m6=max(m2,m4);
                 }
                 if(m5>=mi)
                 {
                     if(m5==mi)
                     {
                         if(m6>ma)
                         {
                            mi=m5;
                            ma=m6;
                            in=m;
                            mee=mi;
                            maa=ma;
                          }
                     }
                     else
                     {
                        mi=m5;
                        ma=m6;
                        in=m;
                        mee=mi;
                        maa=ma;
                     }

                 }
             }
             s.insert(in);
         }
         p[i][0]=maa;
         p[i][1]=mee;
    //  cout<<"ss";
     }
     for(i=0;i<t;i++)
     {
         cout<<"Case #"<<i+1<<": "<<p[i][0]<<" "<<p[i][1]<<endl;
     }

     return 0;
}


