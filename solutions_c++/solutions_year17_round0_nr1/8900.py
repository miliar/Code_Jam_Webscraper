#include<bits/stdc++.h>
using namespace std;
int main()
{ long long int t,i,k,j,p,y;
  char c[1001];
  cin>>t;
  for(j=1;j<=t;j++)
    { cin>>c;
      unsigned int d=strlen(c);
      cin>>k;
      int m=0,count=0,blank=0,x=0;
      cout<<"Case #"<<j<<": ";
      int a[d]={0};
      for(i=0;i<d;i++)
        { if(c[i]=='+')
            a[i]=1;
          else if(c[i]=='-') {a[i]=0;blank++;}
        }
      if(blank==0)
            {cout<<"0"<<endl;continue;}
      else
      {for(i=0;i<d;i++)
        { if(a[i]==0 && (i+k-1)>(d-1))
              {cout<<"IMPOSSIBLE"<<endl;x=1;break;}
          else if(a[i]==0 && (i+k-1)<=(d-1))
              {
                    for(p=i;p<=(i+k-1);p++)
                       { if(a[p]==1)
                          a[p]=0;
                         else if(a[p]==0) a[p]=1;

                       }
                     count++;
              }
        }
       for(i=0;i<d;i++)
         { if(a[i]==0 && x!=1)
            {cout<<"IMPOSSIBLE"<<endl;m=1;break;}
            else if(a[i]==0 && x==1)
                break;
         }
       if(m==0 && x!=1)
           cout<<count<<endl;
      }
    }
  return 0;

}
