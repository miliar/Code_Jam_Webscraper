#include<iostream>
#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;

int main()
{
freopen("C:/Users/Ayush Garg/Downloads/input.txt","r",stdin);

int t;
scanf("%d", &t);
int cs=0;
while (t--)
{
cs++;

int k;
char a[1005];

scanf("%s" , a);
scanf("%d", &k);

int len = strlen (a);

printf("Case #%d: ", cs);

if (len<k)
{
printf("IMPOSSIBLE\n");
continue;
}
int count = 0;

for (int i=0 ; i<len ; i++)
{
    if ( a[i]== '-' && i+k-1<len)
    {
        count ++;
        for (int j =i ; j<i+k; j++)
        {
            if (a[j]=='-')
                a[j]='+';
            else
                a[j]='-';
        }
    }
}

int flag=0 ;
for (int i=0; i<len ; i++)
{
    if (a[i]=='-')
    {
        printf("IMPOSSIBLE");
        flag=1;
        break;
    }
}

  if (flag==0)
cout<<count;
cout<<endl;
}
return 0;
}
