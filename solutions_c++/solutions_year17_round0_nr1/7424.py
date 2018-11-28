#include<iostream>
#include<stdio.h>
#include<stdlib.h>
using namespace std;

int main()
{   int arr[1010];
    int n,k;
    int t;
    string s;
    int sum_zero=0,sum_one=0;
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>t;
    for(int q=1;q<=t;q++)
    {
        sum_zero=0;
        sum_one=0;
        bool flag=true;
        int flip=0;
        cin>>s;
        n=s.size();
        for(int i=0;i<n;i++)
        {
            if(s[i]=='+')
                {arr[i]=1;
                sum_one++;
                }
            else {arr[i]=0;
            sum_zero++;
            }
        }
        cin>>k;
        if(sum_one==n) {cout<<"Case #"<<q<<": 0\n"; continue;}
        for(int i=0;i<n-k+1;i++)
        {
            if(arr[i]==0)
            {
                arr[i]=1;
                int j=i+1;
                while(j!=i+k)
                {
                    if(arr[j]==0) arr[j]=1;
                    else arr[j]=0;
                    j++;
                }
             flip++;
            }
        }
        for(int i=n-k+1;i<n;i++)
        {
            if(arr[i]==0)
            {
               flag=false;
               break;
            }
        }
        if(flag) cout<<"Case #"<<q<<": "<<flip<<endl;
        else cout<<"Case #"<<q<<": IMPOSSIBLE\n";

    }

    fclose(stdin);
    fclose(stdout);

    return 0;

}
