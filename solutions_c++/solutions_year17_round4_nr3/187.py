#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    for(int tc=1;tc<=t;tc++)
    {
        bool flag=0;
        int n,m;
        cin>>n>>m;
        string arr[59];
        int arr1[59][59]={0};
        for(int f=0;f<n;f++)
            cin>>arr[f];
        for(int f=0;f<n;f++)
        {
            for(int f1=0;f1<m;f1++)
            {
                if(arr[f][f1]=='|'||arr[f][f1]=='-')
                {
                    bool hor=0,ver=0;
                    for(int f2=f1+1;f2<m&&arr[f][f2]!='#'&&!hor;f2++)
                    {
                        if(arr[f][f2]!='.')
                            hor=1;
                    }
                    for(int f2=f1-1;f2>=0&&arr[f][f2]!='#'&&!hor;f2--)
                    {
                        if(arr[f][f2]!='.')
                            hor=1;
                    }
                    for(int f2=f+1;f2<n&&arr[f2][f1]!='#'&&!ver;f2++)
                    {
                        if(arr[f2][f1]!='.')
                            ver=1;
                    }
                    for(int f2=f-1;f2>=0&&arr[f2][f1]!='#'&&!ver;f2--)
                    {
                        if(arr[f2][f1]!='.')
                            ver=1;
                    }
                    if(hor&&ver)
                        flag=1;
                    if(hor)
                        arr[f][f1]='v';
                    if(ver)
                        arr[f][f1]='h';
                }
            }
        }
        for(int f0=0;f0<=100;f0++)
        {
            memset(arr1,0,sizeof arr1);
            bool brk=0;
            for(int f=0;f<n&&!brk;f++)
            {
                for(int f1=0;f1<m&&!brk;f1++)
                {
                    if(arr[f][f1]!='.')
                        continue;
                    vector<int>v;
                    int f2=f1;
                    for(;f2<m&&arr[f][f2]=='.';f2++)
                        ;
                    if(f2<m&&arr[f][f1]=='.'&&(arr[f][f2]=='-'||arr[f][f2]=='|'||arr[f][f2]=='h'))
                        arr1[f][f1]++;
                    v.push_back(f2);
                    f2=f1;
                    for(;f2>=0&&arr[f][f2]=='.';f2--)
                        ;
                    if(f2>=0&&arr[f][f1]=='.'&&(arr[f][f2]=='-'||arr[f][f2]=='|'||arr[f][f2]=='h'))
                        arr1[f][f1]++;
                    v.push_back(f2);
                    f2=f;
                    for(;f2<n&&arr[f2][f1]=='.';f2++)
                        ;
                    if(f2<n&&arr[f][f1]=='.'&&(arr[f2][f1]=='-'||arr[f2][f1]=='|'||arr[f2][f1]=='v'))
                        arr1[f][f1]++;
                    v.push_back(f2);
                    f2=f;
                    for(;f2>=0&&arr[f2][f1]=='.';f2--)
                        ;
                    if(f2>=0&&arr[f][f1]=='.'&&(arr[f2][f1]=='-'||arr[f2][f1]=='|'||arr[f2][f1]=='v'))
                        arr1[f][f1]++;
                    v.push_back(f2);
                    if(arr1[f][f1]==0)
                    {
                        flag=1;
                    }
                    if(arr1[f][f1]==1)
                    {
                        f2=v[0];
                        if(f2>=0&&f2<m&&(arr[f][f2]=='-'||arr[f][f2]=='|')){
                            brk=1;
                            arr[f][f2]='h';
                        }
                        f2=v[1];
                        if(f2>=0&&f2<m&&(arr[f][f2]=='-'||arr[f][f2]=='|')){
                            brk=1;
                            arr[f][f2]='h';
                        }
                        f2=v[2];
                        if(f2>=0&&f2<n&&(arr[f2][f1]=='-'||arr[f2][f1]=='|')){
                            brk=1;
                            arr[f2][f1]='v';
                        }
                        f2=v[3];
                        if(f2>=0&&f2<n&&(arr[f2][f1]=='-'||arr[f2][f1]=='|')){
                            brk=1;
                            arr[f2][f1]='v';
                        }
                    }
                }
            }
        }
        cout<<"Case #"<<tc<<": ";
        if(flag)
            cout<<"IMPOSSIBLE\n";
        else
        {
            cout<<"POSSIBLE\n";
            for(int f=0;f<n;f++)
            {
                for(int f1=0;f1<m;f1++)
                {
                    if(arr[f][f1]=='|'||arr[f][f1]=='-')
                        arr[f][f1]='v';
                }
            }
            for(int f=0;f<n;f++)
            {
                for(int f1=0;f1<m;f1++)
                {
                    if(arr[f][f1]=='v')
                        arr[f][f1]='|';
                    if(arr[f][f1]=='h')
                        arr[f][f1]='-';
                }
            }
            for(int f=0;f<n;f++)
                cout<<arr[f]<<endl;
        }
    }
}
