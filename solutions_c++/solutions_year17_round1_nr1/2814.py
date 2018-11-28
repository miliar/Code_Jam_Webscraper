#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <algorithm>
#include <queue>
#include <climits>
#include <map>
#include <set>
#include <bitset>
#define lli long long int
using namespace std;
struct node
{
    string s;
};
int main()
{
    int counter=0,t,i,r,c,k,j;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d %d",&r,&c);
        node ch[r];
        for(i=0;i<r;i++)
        {
            cin >> ch[i].s;
            //printf("%s",ch[i]);
        }
        counter++;
        printf("Case #%d:\n",counter);
        int count=0,pos=0;
        for(i=0;i<r;i++)
        {
            pos=0;
            count=0;
            int arr[50];
            for(j=0;j<c;j++)
            {
                if(ch[i].s[j]=='?')
                {
                    count++;
                }
                else
                {
                    arr[pos]=j;
                   // cout << ch[i].s[j] << " " << j << " " <<i <<endl;
                    pos++;
                }
            }
            //cout << count << endl;
            if(count!=0)
            {
                for(j=1;j<pos;j++)
                {
                    for(k=arr[j-1]+1;k<arr[j];k++)
                    {
                        ch[i].s[k]=ch[i].s[arr[j-1]];
                    }
                }
                if(arr[0]!=0)
                {
                    for(j=0;j<arr[0];j++)
                    {
                        ch[i].s[j]=ch[i].s[arr[0]];
                        //cout << j<<" " <<i <<" ";
                    }                    
                    //cout << endl;
                }
                if(arr[pos-1]!=c-1)
                {
                    for(j=arr[pos-1]+1;j<c;j++)
                    {
                        ch[i].s[j]=ch[i].s[arr[pos-1]];
                        //cout << j<<" " <<i <<" ";
                    }
                   // cout << endl;
                }
            }
        }
        pos=0;
        int arr[50];
        for(i=0;i<r;i++)
        {
            count =1;
            for(j=0;j<c;j++)
            {
                if(ch[i].s[j]!='?')
                {
                    count=0;
                    break;
                }
                
            }
            if(count==0)
            {
                arr[pos]=i;
                pos++;
               // cout << arr[pos-1] << endl;
            }
        }
        //for(i=0;i<pos;i++)
        //cout << arr[i] << endl;
        if(pos!=0)
        {
        for(i=1;i<pos;i++)
        {
            
            for(j=arr[i-1]+1;j<arr[i];j++)
            {
               // cout << arr[i] << endl;
                ch[j].s=ch[arr[i-1]].s;
            }
        }
        if(arr[0]!=0)
        {
            for(i=0;i<arr[0];i++)
            ch[i].s=ch[arr[0]].s;
        }
        if(arr[pos-1]!=r-1)
        {
            for(i=arr[pos-1]+1;i<r;i++)
            ch[i].s=ch[arr[pos-1]].s;
        }}
        for(i=0;i<r;i++)
        cout << ch[i].s << endl;
    }
    
    return 0;
    
}