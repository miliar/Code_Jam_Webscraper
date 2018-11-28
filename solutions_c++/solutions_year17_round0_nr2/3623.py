#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int tree[1005];
char ss[1005];
int len;
char ans[205];
void rest(int idx,char c)
{
    for(int i=idx;i<len;i++)
        ans[i]=c;
}
int main()
{
   freopen("B-large.in","r",stdin);
    freopen("outputB.txt","w",stdout);
    int t;
    int cnt=1;
    cin>>t;
    while(t--)
    {
        scanf("%s",ss);
          len=strlen(ss);
        ss[len]='9';
        int ok=0;
        int minn=ss[len-1];;
        for(int i=len-1;i>=0;i--)
        {
            if (minn<ss[i])
            {
                ans[i]=ss[i]-1;rest(i+1,'9');
                minn='9';
            }
            else ans[i]=ss[i];
            if (ans[i]<minn) minn=ans[i];
        }

        printf("Case #%d: ",cnt++);
        int st=0;
        while(st<len&&ans[st]=='0')st++;
        while(st<len) printf("%c",ans[st++]);
        printf("\n");
    }



    return 0;
}
//896521 183995
