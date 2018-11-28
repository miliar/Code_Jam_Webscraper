#include <bits/stdc++.h>

#define MAX(a,b) ((a>b)?a:b)
#define MIN(a,b) ((a<b)?a:b)
#define loop(n) for(int i=0;i<n;++i)
#define floop(n) for(int i=1;i<=n;++i)
#define pf(x) printf(x);
#define ll long long int
#define pb push_back

using namespace std;


int main()
{
    unsigned long long int x,t,a,b,i,temp;

    int cas=1,n;

    freopen("B-small-attempt1.in","r",stdin);

    freopen("B-small-attempt","w",stdout);

    cin>>n;

    while(n--)
    {

        scanf("%llu",&x);

      //  printf("%llu",x);

        for(i=x;i>=1;i--)
        {
           // cout<<i<<endl;
            temp=i;
            int flag=0;
            int prev=9;
            while(temp>0)
            {
                int last=temp%10;

                if(last<=prev)
                {
                    prev=last;
                    temp=temp/10;
                }
                else
                {
                    flag=1;
                break;

                }


            }
            if(flag==0)
            {
            printf("Case #%d: %llu\n",cas,i);
            cas++;
            break;
            }



         }


    }

    fclose(stdin);
    fclose(stdout);

	return 0;
}

