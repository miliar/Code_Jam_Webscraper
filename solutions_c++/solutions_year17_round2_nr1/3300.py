#include<bits/stdc++.h>
using namespace std;

#define f0(i,n) for(int i=0;i<n;i++)
#define f1(i,n) for(int i=1;i<=n;i++)

int main()
{
 freopen("A-large.in","r",stdin);
 freopen("A-large.out","w",stdout);
 int t,n;
 double max_time=0.0,time,speed,position,final_speed,d;

 scanf("%d",&t);
 int horse[1000][2];
 f1(i,t)
 {  printf("Case #%d: ",i);
     scanf("%lf %d",&d,&n);
     max_time=0.0;
     f0(j,n)
     {
         scanf("%lf %lf",&position,&speed);
//         cout<<position<<" "<<speed<<endl;
         time=(d-position)/speed;
//         cout<<"time:"<<time<<" ";
         if (time>max_time) {max_time=time;}
//         cout<<"max_time "<<max_time<<" ";
     }
//     cout<<"max_time "<<max_time<<" "<<d<<" ";
     final_speed=d/max_time;
//     cout<<final_speed<<endl;
     printf("%.6lf\n",final_speed);
//     sort(horse,horse+n);
//     printf("printing horses\n");
//     f0(k,n) printf("%d %d\n",horse[k][0],horse[k][1]);

//   printf("\n");
 }



}
