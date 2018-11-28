#include<bits/stdc++.h>
using namespace std;
#define ll long long
struct stall
{
    int left;
    int right;
    bool mark;
};
int max(int a,int b)
{
    return (a>b)?a:b;
}
int min(int a,int b)
{
    return (a<b)?a:b;
}
int main()
{
    int t;
    cin>>t;
    for(int f=1;f<=t;f++)
    {
       int n,k,pos;
       cin>>n>>k;
       stall ar[n];
       for(int i=0;i<n;i++)
        {
           ar[i]={i,n-i-1,false};
        }
        for(int i=1;i<=k;i++)
        {
            int e;
            for(e=0;e<n;e++)
            {
               if(ar[e].mark==false)
               break;
            }
            pos=e;
            for(int j=e+1;j<n;j++)
            {
                if(ar[j].mark==false)
                {
                    if(min(ar[j].left,ar[j].right)>min(ar[pos].left,ar[pos].right))
                    pos=j;
                    else if(min(ar[j].left,ar[j].right)==min(ar[pos].left,ar[pos].right))
                    {
                        if(max(ar[j].left,ar[j].right)>max(ar[pos].left,ar[pos].right))
                        pos=j;
                    }
                }
            }
            ar[pos].mark=true;
            int pos1=pos-1,c=0;
            while(pos1>=0 && ar[pos1].mark==false)
            {
                ar[pos1].right=c;
                c++;
                pos1--;
            }
            pos1=pos+1;
            c=0;
            while(pos1<n && ar[pos1].mark==false)
            {
                ar[pos1].left=c;
                c++;
                pos1++;
            }
        }
        cout<<"Case #"<<f<<": "<<max(ar[pos].left,ar[pos].right)<<" "<<min(ar[pos].left,ar[pos].right)<<endl;
    }
    return 0;
}
