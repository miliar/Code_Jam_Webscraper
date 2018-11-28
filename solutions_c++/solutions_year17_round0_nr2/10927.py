#include<bits/stdc++.h>
using namespace std;
int check(int n)
{
    if(n<10) return n;
    int x,y,i,ret,c =0,c1 =0 ;
    for( i = n; i>=1;i--)
    {
        c = 0;
        c1 = 0;
        y =-1;
        ret = i;
        while(ret!= 0){
            x = ret%10;
            if(x<=y ) {
                c++;
            }
            y = x;
            ret/=10;
            c1++;
        }
         if(c == c1-1) return i;
    }
}

int main()
{
    int t,i=0,n;
    freopen("B-small-attempt5.in","r",stdin);
    freopen("B-small-attempt12.txt","w",stdout);
    cin>>t;
    while(i<t){
        cin>>n;
        int x =check(n);
        printf("Case #%d: %d\n",i+1,x);
        i++;
    }
}

