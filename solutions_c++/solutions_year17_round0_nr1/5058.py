#include<bits/stdc++.h>
using namespace std;
#define ll long long int
#define fillchar(a,x) memset(a,x,sizeof(a))
int main()
{
    ofstream myfile;
    myfile.open("1.txt");

    char arr[1005];
    int t,n,k;

    scanf("%d",&t);

    for(int l=1;l<=t;l++)
    {
        scanf("%s %d",&arr,&k);

        n=strlen(arr);

        int flag=0,ans=0;

        if(n<k)
        {
            myfile<<"Case #"<<l<<": "<<"IMPOSSIBLE"<<endl;
            continue;
        }

        for(int i=0;i<=n-k;i++)
        {
            if(arr[i]=='-')
            {
                for(int j=i;j<i+k;j++)
                {
                    if(arr[j]=='-')
                    arr[j]='+';

                    else
                    arr[j]='-';
                }

                ans++;

                //printf("%s\n",arr);
                //printf("ans is %d\n",ans);
            }
        }

        int ctr=0;

        for(int i=0;i<n;i++)
        {
            if(arr[i]=='+')
            ctr++;
        }

        //printf("%s\n",arr);

        if(flag==0)
        {
            if(ctr==n)
            myfile<<"Case #"<<l<<": "<<ans<<endl;

            else
            myfile<<"Case #"<<l<<": "<<"IMPOSSIBLE"<<endl;
        }
    }
	return 0;
}
