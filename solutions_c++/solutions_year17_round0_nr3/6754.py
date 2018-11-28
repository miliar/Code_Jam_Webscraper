#include <iostream>
#include <cstring>
#include <fstream>
using namespace std;
int main()
{
    int t,j;
    cin>>t;
        ofstream myfile;
        myfile.open("out.txt");

    for(j=1;j<=t;j++)
    {
        int a[1010],n,k,i,l,r;
        cin>>n>>k;
        for(i=1;i<=n;i++)
            a[i]=0;
        for(i=1;i<=k;i++)
        {
            int p,q,z,x,lc,rc,minc,maxc,temp,maxic;
            int minco[1010],maxco[1010],co=1,index[1010];
            for(z=1;z<=n;z++)
            {
                if(a[z]==0)
                {
                    lc=rc=0;
                    for(x=z-1;x>=1;x--)
                        if(a[x]==0)
                            lc++;
                        else
                            break;
                    for(x=z+1;x<=n;x++)
                        if(a[x]==0)
                            rc++;
                        else
                            break;
                    minc=lc<rc?lc:rc;
                    maxc=lc>rc?lc:rc;
                    minco[co]=minc;
                    maxco[co]=maxc;
                    index[co]=z;
                    co++;
                }
            }
            for(p=1;p<co;p++)
            {
                for(q=p+1;q<co;q++)
                {
                    if( (minco[p]>minco[q]) || (minco[p]==minco[q] && maxco[p]>maxco[q]) || (minco[p]==minco[q] && maxco[p]==maxco[q] && index[p]>index[q]) )
                    {
                        temp=minco[p];
                        minco[p]=minco[q];
                        minco[q]=temp;

                        temp=maxco[p];
                        maxco[p]=maxco[q];
                        maxco[q]=temp;

                        temp=index[p];
                        index[p]=index[q];
                        index[q]=temp;
                    }
                }
            }
            maxic=-1;
            for(p=1;p<co;p++)
                if(minco[p]==minco[co-1] && maxco[co-1]==maxco[p])
                    break;
            a[index[p]]=1;
            l=maxco[p];
            r=minco[p];
        }
        myfile<<"Case #"<<j<<": "<<l<<" "<<r<<endl;
    }
    myfile.close();
    return 0;
}



