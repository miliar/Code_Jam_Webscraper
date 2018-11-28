#include<iostream>
#include<algorithm>
#include<stdio.h>
using namespace std;
int y[109][109];
long long a,b;
int an=0;

int main()
{
    //freopen("d:\\in.txt","w",stdout);
    for(int aaa=1; aaa<=20; aaa++)
    {
        for(int bbb=aaa; bbb<=20; bbb++)
        {
            a=aaa;
            b=bbb;
            int ans1=0,ans2=0,ans110=0,ans15=0,ans12=0,ans11=0,ans210=0,ans25=0,ans22=0,ans21=0;
            if(a>b)
                swap(a,b);
            long long aa=a,bb=b;
            ans110+=a/10;
            a%=10;
            ans15+=a/5;
            a%=5;
            ans12+=a/2;
            a%=2;
            ans11+=a;
            ans210+=b/10;
            b%=10;
            ans25+=b/5;
            b%=5;
            ans22+=b/2;
            b%=2;
            ans21+=b;
            ans1=max(ans110,ans210)+max(ans15,ans25)+max(ans12,ans22)+max(ans11,ans21);
            ans2=ans110+ans15+ans11+ans12;
            bb-=aa;
            ans2+=bb/10;
            bb%=10;
            ans2+=bb/5;
            bb%=5;
            ans2+=bb/2;
            bb%=2;
            ans2+=bb;
            y[aaa][bbb]=min(ans2,ans1);
        }
    }
    int dd[5]={1,2,5,10};
    for(int i=1;i<=100;i++)
    	for(int j=i;j<=100;j++)
    	{
			for(int k=0;dd[k]<i;k++)
			{
				if(y[i][j]>y[i-dd[k]][j-dd[k]]+1)
					cout<<i<<' '<<j<<' '<<dd[k]<<endl;
			}
		}
    return 0;
}
