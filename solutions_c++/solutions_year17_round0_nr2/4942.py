//
#include<iostream>
#include<cmath>
#include<algorithm>
#include<vector>
#include<cstring>
#include<string>
#include<map>
#include<set>
#include<climits>
#include<fstream>
#include<iomanip>
#include<queue>
#include<stack>
#define lli long long

using namespace std;

string s;
int rec(int k)
{
    int p=0;

    if(k==s.size())return -1;

    while(p!=-1)
    {
        if(k==0 || s[k]>=s[k-1])p=rec(k+1);
        else {s[k]='9';return 1;}

        if(p==1)
        {
            if(s[k]=='0'){s[k]='9';return 1;}
            else{s[k]--;}
        }
    }
    return -1;
}

bool check(int k)
{
    if(k<=9)return 1;
    if(k<=99 && k%10>=k/10)return 1;
    if(k%10>=k/10%10 && k/10%10>=k/100)return 1;
    return 0;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    ifstream cin("input.in");
    ofstream cout("output.out");



    long long T,n=0,n1=0,n2=0,n9=0,k,ans=0;
    cin>>T;

    for(int t1=1;t1<=T;t1++)
    {
        cout<<"Case #"<<t1<<": ";



        n=0; n1=0; n2=0; n9=0;
        cin>>s;
        //cout<<s<<" - ";
        for(int i=0;i<s.size();i++)
        {
            n=n*10+(s[i]-'0');

            if(i==0)n1=1;
            else n1*=10;

            n2=n2*10+1;

            if(i==0)n9=0;
            else n9=n9*10+9;
        }

       // for(int i=n;i>=1;i--)
        //{
        //    if(check(i)){ans=i;cout<<i<<" - ";break;}
        //}

        //cout<<n1<<" "<<n<<" "<<n2<<"\n";
        if(n<=9){cout<<n<<"\n";continue;}
        if(n>=n1 && n<=n2){cout<<n9<<"\n";continue;}

        bool l=0;
        for(int i=1;i<s.size();i++)
        {
            if(l==1){s[i]='9';continue;}
            if(s[i]<s[i-1])
            {
                k=i;
                while(k-2>=0 && s[k-1]==s[k-2])
                {
                    s[k-1]='9';
                    k--;
                }

                if(k!=0)s[k-1]--;
                else s[0]--;

                s[i]='9';
                l=1;
            }
        }

        //rec(0);
        cout<<s<<"\n";







    }

    return 0;
}


/*
5
56546515
1321654
513216
549846
5321
*/
