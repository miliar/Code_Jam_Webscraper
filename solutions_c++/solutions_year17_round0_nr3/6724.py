#include <iostream>
#include <stdlib.h>
#include <stdio.h>

using namespace std;


int main()
{
    int T,i,min1,min2,minx,j,k,z,p,n,l;
    int *flag,*LS,*RS,*ar1,*ar2;
    scanf("%d",&T);
    for(j=1;j<=T;j++)
    {
      scanf("%d %d",&n,&z);
      flag=(int*)malloc((n+2)*sizeof(int));
      LS=(int*)malloc((n+2)*sizeof(int));
      RS=(int*)malloc((n+2)*sizeof(int));
      ar1=(int*)malloc((n+2)*sizeof(int));
      ar2=(int*)malloc((n+2)*sizeof(int));
      for(p=0;p<n+2;p++)
      {
          LS[p]=0;
          RS[p]=0;
          flag[p]=0;
      }
      LS[0]=-5;
      RS[0]=-5;
      LS[n+1]=-5;
      RS[n+1]=-5;
      flag[0]=1;
      flag[n+1]=1;

      for(p=0;p<z;p++)
    {

          for(l=1;l<n+1;l++)
      {
          LS[l]=0;
          RS[l]=0;



      }
      min1=-1;
          min2=-1;
          minx=1;

          for(i=1;i<n+1;i++)
      {
          if(flag[i]==1)
            {   LS[i]=-1;
            RS[i]=-1;
            ar1[i]=-1;
            ar2[i]=-1;
                continue;
            }
          else
          {
              k=i;
              while(flag[k-1]==0)
              {
                k--;
                LS[i]++;
              }
              k=i;
              while(flag[k+1]==0)
              {
                  k++;
                  RS[i]++;
              }
              if(LS[i]<RS[i])
                {ar1[i]=LS[i];
                ar2[i]=RS[i];
                }
              else
                {ar1[i]=RS[i];
                ar2[i]=LS[i];
                }

          }
      }

      for(i=1;i<n+1;i++)
      {   if(flag[i]==1)
      continue;
      else
          {
              if(ar1[i]>min1)
          {
              min1=ar1[i];
              minx=i;
          }
          else if(ar1[i]==min1)
          {
              if(ar2[i]>min2)
              {
                  min2=ar2[i];
                  minx=i;
              }
          }
      }
      }
      flag[minx]=1;




    }
    printf("Case #%d: %d %d\n",j,ar2[minx],ar1[minx]);


    }
}


