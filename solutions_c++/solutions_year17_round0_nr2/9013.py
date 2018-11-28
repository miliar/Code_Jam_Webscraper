
/*This Template is created by Nirmit Jain (github@nj7)*/

//Best header file for competitive programming
#include<bits/stdc++.h>

//Macro for Data Type
#define lli long long int
#define llu unsigned long long int
#define ld long double

//Macro for scanning basic input
#define si(n) scanf("%d",&n)
#define slli(n) scanf("%lld",&n);
#define ss(n) scanf("%s",n);

#define mod 1000000007;

using namespace std;

//Print loop for array element in new line
void print(int a[],int s,int e)
{
    for(int i=s; i<=e; i++)cout<<a[i]<<"\n";
}
void print(vector<int> &v,int s,int e)
{
    for(int i=s; i<=e; i++)cout<<v[i]<<"\n";
}
//this for loop only works with c++11 and higher
void print(vector<int> &v)
{
    for(int x:v)cout<<x<<"\n";
}

int main()
{
    //for taking input from "input.txt" and storing the output to "output.txt".
#ifndef ONLINE_JUDGE
    freopen("B-large.in","r",stdin);
    freopen("Nj.sol","w",stdout);
#endif
    int T,j=1;
    cin>>T;
    while(T--)
    {
        char N[20],ANS[18];
        int i;
        cin>>N;
        for(i = strlen(N)-2 ; i > -1 ; i--)
        {
            if(N[i] > N[i+1])
            {
                N[i] = N[i] - 1;
                N[i+1] = '9';
                for(int k = i+1;k<strlen(N)-1;k++)
                {
                    if(N[k] > N [k+1])
                        N[k+1] = N[k];
                }
            }
        }
        if(N[0] == '0')
        {
            for(i=0;i<strlen(N)-1;i++)
            {
                N[i]=N[i+1];
            }
            N[i] = '\0';
        }
        cout<<"Case #"<<j++<<": "<<N<<"\n";
    }
    return 0;
}
