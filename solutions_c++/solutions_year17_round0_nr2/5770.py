#include<iostream>
#include<vector>
#include<cstdio>
#include<algorithm>
#include<utility>
#include<set>
#include<map>
#include<cstring>
#include<cmath>
#include<string>
#include<cstdlib>

using namespace std;

string tostring(long long n)
{
   string s;
   while(n!=0)
  {
      s+=(n%10LL)+'0';
      n/=10LL;
   }
    reverse(s.begin(), s.end());
    return s;
}

long long dp[20][2][11]; //dp[index][smaller][remainder]

//For integers, the sum of digits can't be greater than 82

long long k;

string s;

long long dp_solve(string & s,int index,bool smaller,int mod1)
{
 if(index==s.length())
 {
 	return 1;
 }
  if(dp[index][smaller][mod1]!=-1)
      {
       return dp[index][smaller][mod1];

      }
    else
    {
        int limit=9;

        if(smaller)
        {
            limit=s[index]-'0';
        }
        long long init_count=0;

        for(int i=mod1;i<=limit;i++)
        {
            bool ns;
            if(i<s[index]-'0')
            {   
                ns=0;
            }
            else
            {
                ns=smaller;
            }

            init_count+=dp_solve(s, index+1, ns,i);

        }


        dp[index][smaller][mod1]=init_count;
        return init_count;

    }

}


int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
int t;
int k=1;
scanf("%d",&t);
while(t--){
      long long a,b; //Find numbers between A and B whose sum of digits is divisible by K
      cin>>a;
		string s=tostring(a);


        memset(dp,-1,sizeof(dp));
        long long a1=dp_solve(s,0,1,0); //Solving for a-1
      //If A and B are ints, then the sum of the digits can't be greater than 82
long long low=1;
long long high=a; 
long long mid;
long long answ=a;
while(low<=high){
	mid=(low+high)/2;       
        string s=tostring(mid);
		//printf("%lld\n",mid);
		
        memset(dp,-1,sizeof(dp));
        long long a2=dp_solve(s,0,1,0); //Solving for a-1
        if(a2<a1)
        {
        	low=mid+1;
		}
		else if(a2==a1)
		{
			answ=min(answ,mid);
			high=mid-1;
		}
	}
	printf("Case #%d: %lld\n",k++,answ);
}
    return 0;
}
