#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin>>t;
    for(int z=1;z<=t;z++)
    {
        int r,c;
        cin>>r>>c;
        char a[r][c];
        vector<int> v(r,0);
        for(int i=0;i<r;i++)
        {
            int count=0;
            for(int j=0;j<c;j++)
            {
                cin>>a[i][j];
                if(a[i][j]!='?')
                count++;
            }
            v[i]=count;
        }
        for(int i=0;i<r;i++)
        {
            if(v[i]>0)
            {
                for(int j=0;j<c;j++)
                {
                    if(a[i][j]!='?')
                    {int k=j-1;
                        while(k>=0&&(a[i][k]=='?'))
                        {
                            a[i][k]=a[i][j];k--;
                        }
                      k=j+1;
                        while(k<c&&(a[i][k]=='?'))
                        {
                            a[i][k]=a[i][j];k++;
                        }
                    }
                }
            }
        }
        for(int i=0;i<r;i++)
        {
            if(v[i]>0)
            {int k=i-1;
                while(k>=0&&(v[k]==0))
                {
                    for(int j=0;j<c;j++)
                    a[k][j]=a[i][j];
                    v[k]++;k--;
                }
                k=i+1;
                 while(k<r&&(v[k]==0))
                {
                    for(int j=0;j<c;j++)
                    a[k][j]=a[i][j];
                    v[k]++;k++;
                }
            }
        }
        cout<<"Case #"<<z<<":"<<endl;
        for(int i=0;i<r;i++)
        {
            for(int j=0;j<c;j++)
            cout<<a[i][j];
            cout<<endl;
        }
    }
    return 0;
}
