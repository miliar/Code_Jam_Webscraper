#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t,k,i,j,x;
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        string arr;
        cin>>arr;
        cin>>k;
        long int count = 0;
        bool flag = true;
        for(j=0;j<arr.size();j++)
        {
            if(arr[j] =='-')
            {
                count++;
                for(x=j;x<j+k;x++)
                {
                    if(x>=arr.size())
                    {
                        flag = false;
                        break;
                    }
                    if(arr[x] == '+')
                        arr[x] = '-';
                    else
                        arr[x] = '+';
                }
            }
            if(flag == false)
                break;
        }

        if(flag == false){
            cout<<"Case "<<"#"<<i<<": "<<"IMPOSSIBLE";
        }
        else{
            cout<<"Case "<<"#"<<i<<": "<<count;

        }
        cout<<"\n";
    }
}
