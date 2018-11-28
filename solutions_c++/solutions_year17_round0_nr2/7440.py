#include<bits/stdc++.h>
#define INPUT
using namespace std;
int main()
{
    #ifdef INPUT
        freopen("input.cpp", "r", stdin);
        freopen("output.cpp", "w", stdout);
    #endif // INPUT
    int t,i,j,temp;
    cin>>t;
    for(i=0;i<t;i++)
    {
        int n,c,m,k,f;
        cin>>n;
        if(n==1000)
        {
            cout<<"Case #"<<(i+1)<<": "<<n-1<<endl;
            continue;
        }
        else if(n==1||n==2||n==3||n==4||n==5||n==6||n==7||n==8||n==9)
        {
            cout<<"Case #"<<(i+1)<<": "<<n<<endl;
            continue;
        }
        for(j=n;j>9;j--)
        {
            c=0;
            temp = j;
            while(temp!=0)
            {
                temp = temp/10;
                c++;
            }
            m = c;
            int a[m];
            temp = j;
            while(c!=0)
            {
                a[c-1] = temp%10;
                temp = temp/10;
                c--;
            }
            f = 0;
            for(k=0;k<m-1;k++)
            {
                if(a[k]<=a[k+1])
                {
                    f++;
                    continue;
                }
                else
                    break;
            }
            if(f==m-1)
            {
                cout<<"Case #"<<(i+1)<<": "<<j<<endl;
                break;
            }
            else
                continue;
        }
        if(j==9)
            cout<<"Case #"<<(i+1)<<": "<<j<<endl;
        else
            continue;
    }
    return 0;
}
