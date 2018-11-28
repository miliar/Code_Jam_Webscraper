#include<iostream>
#include<algorithm>

using namespace std;

int main()
{
    unsigned long long t,tt,n,k;
    cin>>t;
    for(tt=1;tt<=t;tt++)
    {
        cin>>n>>k;
        unsigned long long b[n+2][3],tmp[n],cnt,l,mx,m,r,i,j;
        for(b[0][0]=b[n+1][0]=i=1;i<=n;i++)
            b[i][0]=0;
        while(k--)
        {
            for(i=1;i<=n;i++)//Getting Each Stall for K
                if(!b[i][0])//Got Empty Stall
                {
                    for(j=i-1,cnt=0;j>0;j--)//Counting Ls
                        if(b[j][0])
                            break;
                        else
                            cnt++;
                    b[i][1]=cnt;
                    for(j=i+1,cnt=0;j<=n;j++)//Counting Rs
                        if(b[j][0])
                            break;
                        else
                            cnt++;
                    b[i][2]=cnt;
                }

            for(mx=l=0,j=1;j<=n;j++)//Get Min
                if(!b[j][0])
                {
                    m=min(b[j][1],b[j][2]);
                    if(m>mx)
                    {
                        mx=m;
                        tmp[0]=j;
                        l=1;
                    }
                    else if(m==mx)
                    {
                        tmp[l]=j;
                        l++;
                    }
                }
            if(l==1)
                b[tmp[0]][0]=1;
            else
            {
                for(mx=j=r=0;j<l;j++)//Get Max
                {
                    m=max(b[tmp[j]][1],b[tmp[j]][2]);
                    if(m>mx)
                    {
                        mx=m;
                        tmp[0]=tmp[j];
                        r=1;
                    }
                    else if(m==mx)
                    {
                        tmp[r]=tmp[j];
                        r++;
                    }
                }
                b[tmp[0]][0]=1;
            }
        }
        l=max(b[tmp[0]][1],b[tmp[0]][2]);
        r=min(b[tmp[0]][1],b[tmp[0]][2]);
        cout<<"Case #"<<tt<<": "<<l<<" "<<r<<endl;
    }
    return 0;
}
