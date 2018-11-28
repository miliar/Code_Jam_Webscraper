#include<iostream>
#include<algorithm>
#include<string.h>

using namespace std;

int t,i,a[100],m,n,b,k,j;
char s[100][1000];

void change(char *a,int i)
{
int j;
for(j=0;j<i;j++)
{
    if(*a=='-')
    {
         *a='+';
    }
    else if(*a=='+')
    {
        *a='-';
    }
a++;
}
}

int main()
{
	freopen("A-small-attempt1.in","r",stdin);
	freopen("panSout1.txt","w",stdout);

    cin>>t;
    for(i=0;i<t;i++)
    {
        cin>>s[i];
        cin>>a[i];
    }
int flag=0;
    for(i=0;i<t;i++)
    {
        k=0;
        n=0;
        b=0;
        m=strlen(s[i]);
        while(k<m)
        {
            if(s[i][k]=='-')
            {
//                n=k;
                j=0;
                flag=0;
                if(k<m-a[i]+1)
                {
                    change(&s[i][k],a[i]);
                    //k++;
                    flag=1;
                    //j++;
                }
                else
                {
                    goto c;
                }
                if(flag==1)
                    b++;
//                k=n+1;
            }
            k++;
//cout<<"\n"<<s[i];
        }
c:
        cout<<"Case #"<<i+1<<": ";
        if(s[i][m-1]=='-' || k<m)
            cout<<"IMPOSSIBLE\n";
        else
            cout<<b<<"\n";
    }
return 0;
}
