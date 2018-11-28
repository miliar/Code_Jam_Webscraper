#include<iostream>
#include<cstdio>
#include<math.h>
#include<algorithm>
#include<string>
#include<string.h>
#include<ctype.h>
#include<vector>

#define mod 1000000007 
#define ll long long 
#define ull unsigned long long 

using namespace std;

int main()
{
	
freopen("input2.in","r",stdin);
freopen("output2.txt","w",stdout);
    
    int t,n,k,i,cnt,l,r,flag[1000006];
    cin>>t;
    for(int j=0;j<t;j++)
    {   
        cin>>n>>k;
        if(k>(2*n)/3)
        {
            l=r=0;
            cout<<"Case #"<<j+1<<": "<<max(l,r)<<" "<<min(l,r)<<endl;
            continue;
        }
        fill(flag,flag+n+2,0);
        flag[n]=1;
        i=n;
        while(k--)
        {   while(flag[i]==0)
            {i--;}
            n=i;
            flag[n]--;
            l=(n)/2;
            r=(n-1)/2;
            flag[l]++;
            flag[r]++;
    		if(!(l || r))
    		break;
        }
        cout<<"Case #"<<j+1<<": "<<max(l,r)<<" "<<min(l,r)<<endl;
    }
    
    return 0;
}
