#include<bits/stdc++.h>

using namespace std;


#define fast    ios_base::sync_with_stdio(0)
#define ull unsigned long long int
#define pb  push_back
#define mp  make_pair
#define ll long long int
#define all(v)  v.begin(),v.end()
typedef pair<int,int> pii;


 
 void codejam(int x,int y,bool haa)
 {      if(!haa)
        {
            printf("Case #%d: IMPOSSIBLE\n",x);
            return;

        }
        printf("Case #%d: %d\n",x,y);
    

 }
 
 vector<int> data;
 
 void solve(int number,int sze,int prev)
 { 
    if(sze==3)
    {
        data.pb(number);
        return;

    }
    else
    {
        int start=prev;
        data.pb(number);

        if(number==0)start+=1;
        for(int i=start;i<=9;i++)
        {
            solve(number*10+i,sze+1,i);

        }
    }
 }
 int dp[20];
int testcase;
 void solve(ull n)
 {
    memset(dp,0,sizeof dp);
    int idx=0;
    while(n>0)
    {
        int rem=n%10;
        dp[idx++]=rem;
        n/=10;

    }
    int earlier=dp[idx-1];
    for(int i=0;i<idx-1;i++)
    {
            if(dp[i]<dp[i+1])
            {
                dp[i]=9;
                dp[i+1]-=1;
            }
    }
    
    if(earlier==dp[idx-1])
    {       
             cout<<"Case #"<<testcase++<<": ";
              for(int i=idx-1;i>=0;i--)cout<<dp[i];

    }
    else
    {        cout<<"Case #"<<testcase++<<": ";
            for(int i=0;i<idx-1;i++)dp[i]=9;
                for(int i=idx-1;i>=0;i--)
                    {
                        if(i==idx-1 and dp[i]==0)continue;
                        cout<<dp[i];
                    }


    }
   cout<<endl;

 }
 int main()
 {
    solve(0,0,0);
    sort(data.begin(),data.end());
   int t;
   cin>>t;
    testcase=1;
   while(t--)
   {
    ull n;
    cin>>n;
    if(n>1000)
    {
        solve(n);
        continue;

    }
    int N=(int)n;

    int idx=upper_bound(data.begin(),data.end(),N)-data.begin();
    codejam(testcase++,data[idx-1],true);

   }
 }