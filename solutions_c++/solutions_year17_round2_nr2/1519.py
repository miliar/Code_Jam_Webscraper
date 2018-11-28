#include <iostream>
#include <bits/stdc++.h>

using namespace std;

char c[2000];
char q[10]={"ROYGBV"};
int main()
{
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    int a[10];
    int T;
    cin>>T;
    for(int t=1;t<=T;t++)
    {
        //printf("Case #%d: ",t);
        int n;
        memset(c,'\0',sizeof(c));
        scanf("%d",&n);
        scanf("%d %d %d %d %d %d",&a[0],&a[1],&a[2],&a[3],&a[4],&a[5]);
        int flag=0;
        for(int i=0;i<6;i++)
        {
            if(a[i]>0){
                c[0]=q[i];
                a[i]--;
                break;
            }
        }
        for(int i=1;i<n;i++)
        {
            if(c[i-1]=='R')
            {
                if(a[3]>0){
                    c[i]=q[3];
                    a[3]--;
                }
                else if(a[4]>0&&a[4]>a[2]){
                    c[i]=q[4];
                    a[4]--;
                }
                else if(a[2]>0)
                {
                    c[i]=q[2];
                    a[2]--;
                }
                else
                {
                    flag=1;
                    break;
                }
            }
            else if(c[i-1]=='O')
            {
                if(a[4]>0)
                {
                    c[i]=q[4];
                    a[4]--;
                }
                else
                {
                    flag=1;
                    break;
                }
            }
            else if(c[i-1]=='Y')
            {
                if(a[5]>0){
                    c[i]=q[5];
                    a[5]--;
                }
                else if(a[4]>0&&a[4]>a[0]){
                    c[i]=q[4];
                    a[4]--;
                }
                else if(a[0]>0)
                {
                    c[i]=q[0];
                    a[0]--;
                }
                else
                {
                    flag=1;
                    break;
                }
            }
            else if(c[i-1]=='G')
            {
                if(a[0]>0)
                {
                    c[i]=q[0];
                    a[0]--;
                }
                else
                {
                    flag=1;
                    break;
                }
            }
            else if(c[i-1]=='B')
            {
                if(a[1]>0){
                    c[i]=q[1];
                    a[1]--;
                }
                else if(a[2]>0&&a[2]>a[0]){
                    c[i]=q[2];
                    a[2]--;
                }
                else if(a[0]>0)
                {
                    c[i]=q[0];
                    a[0]--;
                }
                else
                {
                    flag=1;
                    break;
                }
            }
            else
            {
                if(a[2]>0)
                {
                    c[i]=q[2];
                    a[2]--;
                }
                else
                {
                    flag=1;
                    break;
                }
            }
        }
        //cout<<flag<<endl;
        if(c[n-1]=='R'&&(c[0]=='R'||c[0]=='O'||c[0]=='V'))
            flag=1;
        if(c[n-1]=='O'&&(c[0]=='R'||c[0]=='Y'||c[0]=='O'))
            flag=1;
        if(c[n-1]=='Y'&&(c[0]=='Y'||c[0]=='O'&&c[0]=='G'))
            flag=1;
        if(c[n-1]=='G'&&(c[0]=='G'||c[0]=='B'||c[0]=='Y'))
            flag=1;
        if(c[n-1]=='B'&&(c[0]=='B'||c[0]=='G'||c[0]=='V'))
            flag=1;
        if(c[n-1]=='V'&&(c[0]=='B'||c[0]=='V'||c[0]=='R'))
            flag=1;
        if(flag)
            printf("Case #%d: IMPOSSIBLE\n",t);
        else
           printf("Case #%d: %s\n",t,c);
    }
    //cout << "Hello world!" << endl;
    return 0;
}
