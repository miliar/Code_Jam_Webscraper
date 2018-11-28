#include<bits/stdc++.h>
using namespace std;
#define ll long long int
#define fillchar(a,x) memset(a,x,sizeof(a))
int main()
{
	ofstream myfile;
    myfile.open("1.txt");

	char arr[20];
	int num[20];
	int t,n;

	scanf("%d",&t);

	for(int l=1;l<=t;l++)
    {
        scanf("%s",&arr);

        n=strlen(arr);

        int flag=0;

        for(int i=0;i<n;i++)
        {
            num[i]=arr[i]-'0';
        }

        for(int i=1;i<n;i++)
        {
            if(num[i]<num[i-1])
            {
                for(int j=i;j<n;j++)
                {
                    num[j]=9;
                }

                if(num[i-1]>1)
                {
                    //num[i-1]--;
                    int flag1=0;

                    int temp=i-1;

                    for(int j=i-2;j>=0;j--)
                    {
                        if(num[j]!=num[j+1])
                        {
                            temp=j+1;
                            flag1=1;
                            break;
                        }
                    }

                    if(flag1==0)
                    temp=0;

                    num[temp]--;

                    for(int j=temp+1;j<=i-1;j++)
                    {
                        num[j]=9;
                    }

                    for(int j=i;j<n;j++)
                    {
                        num[j]=9;
                    }
                }

                else if(num[i-1]==1)
                {
                    num[0]=0;
                    for(int j=1;j<i;j++)
                    {
                        num[j]=9;
                    }

                    flag=1;

                    for(int i=0;i<n-1;i++)
                    {
                        num[i]=num[i+1];
                    }
                }
            }
        }

        if(flag==1)
        n--;

        myfile<<"Case #"<<l<<": ";

        for(int i=0;i<n;i++)
        {
            myfile<<num[i];
        }

        if(l!=t)
        myfile<<endl;
    }
	return 0;
}
