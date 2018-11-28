#include<bits/stdc++.h>
using namespace std;

main()
{
    freopen("C-small-2-attempt0.in","r",stdin);
    freopen("C-small-2-attempt0.out","w",stdout);
//    freopen("in_case.txt","w",stdout);

    int t,n,k,ls,rs;
    scanf("%d",&t);
//    t=3;n=1000;k=4;

    for(int i=1;i<=t;i++)
    {
        scanf("%d %d",&n,&k);

 float last_partition=pow(2.0,floor(log2(k)));

 int no_of_person_before_new_partition=last_partition-1;


 float max_partition=ceil((n-no_of_person_before_new_partition)/last_partition);
 float no_of_max_partition=n-(floor((n-no_of_person_before_new_partition)/last_partition)*last_partition + no_of_person_before_new_partition);

//             printf("last_partition :%f\n",last_partition);
//             printf(" no_of_person_before_new_partition :%f \n",no_of_person_before_new_partition);
//           printf("value of max partition: %f\n no of max partition %f\n k-q=%d\n ",max_partition,no_of_max_partition,k-no_of_person_before_new_partition);

          if ((k-no_of_person_before_new_partition)<=no_of_max_partition ||no_of_person_before_new_partition==0||no_of_max_partition==0)
              {
//           printf("\nInside minimum\n");
           rs=max_partition/2;
           ls=max_partition-1-rs<0?0:max_partition-1-rs;
          }
          else

          {
//              printf("\nInside maximum\n");
              rs=(max_partition-1)/2;
              ls=max_partition-2-rs<0?0:max_partition-2-rs;
             }
//      printf("Case #%d : %d %d\n",i,n,k)       ;
        printf("Case #%d: %d %d\n",i,rs,ls);
    }

}
