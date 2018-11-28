#include<bits/stdc++.h>
using namespace std;
#define ll long long int
#define fillchar(a,x) memset(a,x,sizeof(a))
int main()
{
	//freopen("./in.txt", "r", stdin);
	freopen("./1.txt", "w", stdout);

	int t,n,p;
	int arr[105];

	scanf("%d", &t);

    for(int l=1;l<=t;l++)
	{
        scanf("%d %d",&n,&p);

        for(int i=0;i<n;i++)
        {
            scanf("%d",&arr[i]);
        }

        int ctr=0,ctr1=0,ctr2=0,ctr3=0;

        if(p==2)
        {
            for(int i=0;i<n;i++)
            {
                if(arr[i]%p==0)
                ctr++;

                else
                ctr1++;
            }

            int ans=ctr+(ctr1+1)/2;

            printf("Case #%d: %d\n",l,ans);
        }

        else if(p==3)
        {
            for(int i=0;i<n;i++)
            {
                if(arr[i]%p==0)
                ctr++;

                else if(arr[i]%p==1)
                ctr1++;

                else
                ctr2++;
            }

            int ans;

            //printf("%d %d %d\n",ctr,ctr1,ctr2);

            if(ctr1>ctr2)
            {
                ans=ctr+ctr2+((ctr1-ctr2)/3);

                if((ctr1-ctr2)%3!=0)
                ans++;
            }

            else
            {
                ans=ctr+ctr1+((ctr2-ctr1)/3);

                if((ctr2-ctr1)%3!=0)
                ans++;
            }

            printf("Case #%d: %d\n",l,ans);
        }
	}
	return 0;
}
