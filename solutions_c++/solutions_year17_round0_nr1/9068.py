#include<iostream>
#include<cstring>
#include<algorithm>

#define fre freopen("0.in","r",stdin),freopen("0.out","w",stdout)
using namespace std;

int solution(char ar[],int n,int size)
{
    int count=0;
    for(int i=0;i<size;i++)
    {
        int k=0;
        if(ar[i]=='-')
        {
            for(int j=i;k<n && (i+n-1<size);j++,k++)
            {
                if(ar[j]=='-')
                {   
                    ar[j]='+';
                }
                else
                ar[j]='-';
            }
            count+=1;   
        }
    }
    
    for(int i=0;i<size;i++)
    {
        if(ar[i]=='-')
        return -1;
    }
    return count;
}

int main()
{
    
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    
    int t;
    cin>>t;
    int i=0;
    while(i<t)
    {
        char s[1024];
        int k;

        cin>>s>>k;
        int length=strlen(s);
        int ans=solution(s,k,length);
        
        
        if(ans==-1){
            cout << "Case #" <<++i << ": " << "IMPOSSIBLE" << "\n";
        }else
        {
            cout << "Case #" <<++i << ": " << ans << "\n";
        }
        
        }
}
