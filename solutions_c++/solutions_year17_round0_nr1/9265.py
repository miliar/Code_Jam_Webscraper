#include<bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp> 
#include <ext/pb_ds/tree_policy.hpp>

using namespace std;
using namespace __gnu_pbds;

#define	fast	ios_base::sync_with_stdio(0)
#define	ull	unsigned long long int
#define	pb	push_back
#define	mp	make_pair
#define	ll long long int
#define	all(v)	v.begin(),v.end()
typedef pair<int,int> pii;
typedef tree<int,null_type,less<int>,rb_tree_tag,tree_order_statistics_node_update> BTREE;

 
 void codejam(int x,int y,bool haa)
 {      if(!haa)
        {
            printf("Case #%d: IMPOSSIBLE\n",x);
            return;

        }
        printf("Case #%d: %d\n",x,y);
    

 }
 const int N=1e3+3;

int pre[N];
char str[1002];
int k;

 int main()
 {  int t;
    scanf("%d",&t);
    int testcase=1;
    while(t--)
    {
        memset(pre,0,sizeof pre);
        scanf("%s",str+1);
        cin>>k;
        int n=strlen(str+1);
        int ans=0;

        for(int i=1;i<=n;i++)
        {   if(i<=(n-k+1)){
            pre[i]+=pre[i-1];

            if(pre[i]%2==1)
            {
                if(str[i]=='+')str[i]='-';
                else    str[i]='+';
               // cout<<"I m at"<< i<<endl;

            }
            if(str[i]=='-')
            {
                str[i]='+';
               pre[i]=pre[i]+1;
               pre[i+k]=pre[i+k]-1;
                ans++;
              //  cout<<pre[i]<<" "<<"I m at down"<< i<<endl;


            }}
            else
            {
                pre[i]+=pre[i-1];
                if(pre[i]%2==1)
            {
                if(str[i]=='+')str[i]='-';
                else    str[i]='+';
               // cout<<"I m at"<< i<<endl;

            }
            }
          // cout<<i<<" "<<str+1<<" "<<ans<<endl;

        }
        int i;
        for( i=1;i<=n;i++)
        {
            if(str[i]=='-')
            {
            codejam(testcase++,0,false);
            break;

            }
        }
        if(i>n)codejam(testcase++,ans,true);


       

    }
}
