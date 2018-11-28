#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <cstring>

using namespace std;
long long int maxof2(long long int x,long long int y)
{
    if(x>y)
        return x;
    return y;
}
long long int minof2(long long int x,long long int y)
{
    if(x>y)
        return y;
    return x;
}
long long int findmax(long long int D[][2],long long int dd)
{
    //cout<<"dd="<<dd<<endl;
    //for(int ttt=0;ttt<=dd;ttt++)
    //    cout<<D[ttt][0]<<" "<<D[ttt][1]<<endl;
    long long int ii,maxi,index;
    maxi=abs(D[0][0]-D[0][1])+1;
    index=0;
    for(ii=1;ii<=dd;ii++)
    {
        if(maxi<(abs(D[ii][0]-D[ii][1])+1))
        {
            index=ii;
            maxi = abs(D[ii][0]-D[ii][1])+1;
        }
    }
    return index;
}
void cascadedown(long long int D[][2],long long int dd,long long int cc)
{
    //cout<<"cascade called";
     long long int ii;
     for(ii=cc;ii<dd;ii++)
     {
         D[ii][0]=D[ii+1][0];
         D[ii][1]=D[ii+1][1];
     }
     //for(int ttt=0;ttt<=dd;ttt++)
      //  cout<<D[ttt][0]<<" "<<D[ttt][1]<<endl;
}
int main()
{
    FILE *fp;
    fp=fopen("C-small-1-attempt1.in","r");
    FILE *fpa;
    fpa=fopen("C-small-1.txt","w");
    int T,t;
    long long int y,z,m1,m2,m,K,N,t1,t2,i,j,k,D[100000][2],d,ls,rs,ls2,rs2,y1,y2,z1,z2,m3,ttt;
    fscanf(fp,"%d",&T);
    for(t=1;t<=T;t++)
    {
        fscanf(fp,"%lld %lld",&N,&K);
        if(N==K)
        {
            y=0;
            z=0;
        }
        else
        {
            d=0;
            D[d][0]=0;
            D[d][1]=N-1;
            for(i=0;i<K;i++)
            {

                k=findmax(D,d);
                //cout<<"k="<<k<<endl;
                m=(D[k][1]-D[k][0])+1;
               // cout<<"m="<<m<<endl;

               /*if(i==231)
               {
                   cout<<"k="<<k<<endl;
                   cout<<"m="<<m<<endl;
                   for(int ttt=0;ttt<=d;ttt++)
                    cout<<"ttt="<<ttt<<" "<<D[ttt][0]<<" "<<D[ttt][1]<<endl;
               }*/

                if(m%2==0)
                {
                    d++;
                    m1=(D[k][1]+D[k][0])/2;
                    m2=m1+1;
                    t1=D[k][0];
                    t2=D[k][1];
                    ls=m1-t1;
                    rs=t2-m1;
                    /*if(i==230)
                    {
                     cout<<"ls= "<<ls<<" rs="<<rs<<endl;
                     cout<<"t2= "<<t2<<" m1="<<m1<<endl;
                    }*/
                    y1=maxof2(ls,rs);
                    z1=minof2(ls,rs);
                    ls2=m2-t1;
                    rs2=t2-m2;
                    y2=maxof2(ls2,rs2);
                    z2=minof2(ls2,rs2);
                    /*if(i==230)
                    {
                   cout<<"m1="<<m1<<" m2="<<m2<<endl;
                   cout<<"y1="<<y1<<"y2="<<y2<<endl;
                   cout<<"z1="<<z1<<"z2="<<z2<<endl;
                    }*/
                   // cout<<"m1="<<m1<<" m2="<<m2<<endl;
                   // cout<<"y1="<<y1<<"y2="<<y2<<endl;
                 //   cout<<"z1="<<z1<<"z2="<<z2<<endl;
                    if(z1>z2)
                    {
                        m3=1;
                    }
                    else if(z1<z2)
                    {
                        m3=2;
                    }
                    else
                    {
                        if(y1>y2)
                        {
                            m3=1;
                        }
                        else if(y1<y2)
                        {
                            m3=2;
                        }
                        else
                        {
                            if(m1<m2)
                                m3=1;
                            else
                                m3=2;
                        }
                    }
                   // cout<<"m3="<<m3<<endl;
                    if(m3==1)
                    {
                        if(t2-t1==1)
                        {
                            d--;
                            D[k][0]=m1+1;
                            D[k][1]=t2;
                        }
                        else
                        {
                            D[k][0]=t1;
                            D[k][1]=m1-1;
                            D[d][0]=m1+1;
                            D[d][1]=t2;
                        }

                        y=y1;
                        z=z1;
                    }
                    else
                    {
                        if(t2-t1==1)
                        {
                            d--;
                            D[k][0]=m2+1;
                            D[k][1]=t2;
                        }
                        else
                        {
                            D[k][0]=t1;
                            D[k][1]=m2-1;
                            D[d][0]=m2+1;
                            D[d][1]=t2;
                        }
                        y=y2;
                        z=z2;
                    }
                    //cout<<"i="<<i<<endl;
                   /* if(y==-1 && z==-1)
                    {
                        cout<<"i="<<i<<endl;
                        break;
                    }*/

                }
                else
                {
                    //cout<<"i="<<i<<" k="<<k<<endl;
                    m1=(D[k][1]+D[k][0])/2;
                    //cout<<D[k][1]<<" "<<D[k][0]<<endl;
                    if(D[k][1]==D[k][0])
                    {
                        cascadedown(D,d,k);
                        d--;
                        ls=0;
                        rs=0;
                        y=0;
                        z=0;
                    }
                    else
                    {
                        d++;
                        t1=D[k][0];
                        t2=D[k][1];
                        ls=m1-t1;
                        rs=t2-m1;
                        y=maxof2(ls,rs);
                        z=minof2(ls,rs);
                        D[k][0]=t1;
                        D[k][1]=m1-1;
                        D[d][0]=m1+1;
                        D[d][1]=t2;
                    }
                    /*if(y==-1 && z==-1)
                    {
                        cout<<"i="<<i<<endl;
                        break;
                    }*/
                }
                //for(ttt=0;ttt<=d;ttt++)
                    /*if(D[d][0]==-1 || D[d][1]==-1)
                    {
                        cout<<"CULPRIT :: i="<<i<<endl;
                    }*/


            }
        }
        //cout<<"T="<<t<<" y="<<y<<" z="<<z<<endl;
        fprintf(fpa,"Case #%d: %lld %lld\n",t,y,z);
    }

    fclose(fp);
    fclose(fpa);
    return 0;
}

