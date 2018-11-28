#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <fstream>


using namespace std;

int rep[50];
int a[50][50];
double b[50][50];
int point[50];
int T;
int N,P,sum;

bool check(){
   int bot=0,top=0;
   top=floor(b[0][point[0]]/0.9);
   bot=ceil(b[0][point[0]]/1.1);
   for (int i=1;i<N;i++)
   {
       //cout<<"top:"<<top<<" bot:"<<bot<<endl;
       top=min(top,(int)floor(b[i][point[i]]/0.9));
       bot=max(bot,(int)ceil(b[i][point[i]]/1.1));
       //cout<<"top:"<<top<<" bot:"<<bot<<endl;
       if (bot>top) return false;
   }
   if (bot>top) return false;
     else return true;
}

int findmin(){
   int index=0;
   //cout<<"!!!"<<endl;
   for (int i=0;i<N;i++)
   {
     if (b[i][point[i]]<b[index][point[index]])
        index=i;
     //cout<<point[i];
   }
   //cout<<endl;
   return index;
}


int main()
{
     ifstream filei;
     ofstream fileo;
     filei.open("2.in");
     fileo.open("2.out");
     filei>>T;
     //cin>>T;
     for (int i=0;i<T;i++)
     {
         filei>>N>>P;
         //cin>>N>>P;
         sum=0;
         memset(a,0,sizeof(a));
         for (int j=0;j<N;j++)
            //cin>>rep[j];
            filei>>rep[j];
         for (int j=0;j<N;j++)
         {
            for (int k=0;k<P;k++)
              {
                  //cin>>a[j][k];
                  filei>>a[j][k];
              }
            sort((int*)a+j*50,(int*)a+j*50+P);
            point[j]=0;
            for (int k=0;k<P;k++)
              b[j][k]=1.0*a[j][k]/rep[j];
         }
         while (1){
            if (check()){
                //cout<<"!!!"<<endl;
                sum++;bool flag=false;
                for (int i=0;i<N;i++)
                {
                    point[i]++;
                    if (point[i]>=P) {flag=true;break;}
                }
                if (flag) break;
            }
            else
            {
                //cout<<"???"<<endl;
                int index=findmin();
                point[index]++;if (point[index]>=P) break;
            }

         }
         fileo<<"Case #"<<i+1<<": "<<sum<<endl;
     }
}
