#include<iostream>
#include<string>
#include <limits>

using namespace std;

int main()
{

   int t;
   int j=1;
    cin>>t;
    while(t>0)
    {


    int n,k;
        cin>>n>>k;
        int A[n+2];
        int maximum;
        int minimum;
        int B[n+2];
        int L[n+2];
        int R[n+2];
        int G_left[n+2];
        int G_right[n+2];
        int i=0;
        for(i=0;i<n+2;i++)
        {
            B[i]=0;L[i]=0;
            R[i]=0;
            G_left[i]=0;
            G_right[i]=n+1;
        }

        B[0]=1;
        B[n+1]=1;
        int m;
        int l_index=0;
        int l_index1;
        int r_index1;
        int index=n+1;
        int r_index=n+1;int flag=0;
        for(m=0;m<k;m++)
        {
           minimum=0;
           maximum=0;



        for(i=1;i<n+1;i++)
        {       l_index=1;


            if(B[i]==0)
            {   L[i]=0;R[i]=0;


            if(flag==1)
            {


                if((G_left[i]<index)&&(i>index))
                {
                    G_left[i]=index;
                }
                if((G_right[i]>index)&&(i<index))
                {
                    G_right[i]=index;
                }


            }


            /*int  j;
            int flag=0;
            for(j=i-1;j>0;j--)
            {

                if(B[j]==0)
                {
                    flag++;
                }
                else
                {
                    break;
                }
            }
            L[i]=flag;




            flag=0;
            for(j=i+1;j<n+1;j++)
            {

                if(B[j]==0)
                {
                    flag++;
                }
                else
                {
                    break;
                }
            }

            R[i]=flag;
            */
            L[i]=i-G_left[i]-1;
            R[i]=G_right[i]-1-i;





            if(L[i]<R[i])
            {
                if(L[i]>minimum)
                {
                    minimum=L[i];
                }
            }
            else
            {   if(R[i]>minimum)
                {
                    minimum=R[i];
                }

            }








            }
        }


        flag=1;





        for(i=1;i<n+1;i++)
        {



            if(B[i]==0)
            {
                if(L[i]<R[i])
                {
                    if(L[i]==minimum)
                    {

                        if(R[i]>maximum)
                        {
                            maximum=R[i];
                            index=i;
                        }

                    }
                }
                else
                {

                    if(R[i]==minimum)
                    {
                        if(L[i]>maximum)
                        {

                            maximum=L[i];
                            index=i;

                        }
                    }

                }
            }
        }



        B[index]=1;



    }




        cout<<"Case #"<<j<<": "<<maximum<<" "<<minimum<<"\n";







        t--;j++;
    }













}
