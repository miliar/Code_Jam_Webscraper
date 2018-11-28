#include<bits/stdc++.h>
using namespace std;
#define sc scanint
#define sl scanlong
#define mi 100000007
#define getst(s) getline(cin>>ws,s)
#define MAXA 66457976
typedef long long int lol;
int main()
{
    int aka=1;
    int test;
    scanf("%d",&test);
    while(test--)
    {
        lol nun;
        cin>>nun;
        vector<int> con(19);
        for(int y=0;y<=18;y++)
            con[y]='$';
        int jun=0;
        while(nun!=0)
        {
            con[jun]=nun%10;
            nun=nun/10;
            jun++;
        }
        for(int p=1;p<jun;p++)
        {
            if(con[p]>con[p-1])
            {
            con[p]=con[p]-1;
            for(int ku=0;ku<=p-1;ku++)
        con[ku]=9;
            }
        }
        int gax=0;
        for(int i=jun-1;i>=0;i--)
        {
            if(con[i]==0)
            gax=gax+1;
            else break;
        }
        cout<<"Case #"<<aka<<": ";
        aka++;
        for(int i=jun-1-gax;i>=0;i--)
        {
          cout<<con[i];
        }
        cout<<endl;
    }
}
