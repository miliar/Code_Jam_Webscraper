#include<bits/stdc++.h>
typedef long long ll;
using namespace std;
vector<ll>num;
int gao()
{
  int flag=1;
  if(num.size()==1) return 1;
  for(int i=num.size()-1;i>0;--i)
  {
  	if(num[i]>num[i-1]){
  		flag=0;return 0;
	  }
  }
  return 1; 
}
int solve(ll n)
{
  if(n%10==0) return 0;
  ll tmp=0;
  while(n)
  {
    tmp = n%10;
    num.push_back(tmp);
    n/=10;
  }
  int flag=gao();
  return flag;
}
int main()
{
	//freopen("B-small.in","r",stdin);
	//freopen("B-small.out","w",stdout);
//	freopen("B-large.in","r",stdin);
//	freopen("B-large.out","w",stdout);
	
   // ios::sync_with_stdio(false);
    int t;
	int cas, flag;
    char s[100];
    scanf("%d",&t);
    cas = 1;
    while(t--)
	{
        scanf("%s",&s);
        int len=strlen(s);

        for (int i=1; i<len; i++)
		{
            if (s[i] < s[i-1])
			{
                for (int j=i; j<len; j++)
				{
                	s[j] = '9';
				}
                s[i-1] -= 1;
                i = 0;
            }
        }
		printf("Case #%d: ",cas);
       
        flag=0;
        for (int i=0; i<len;i++)
		{
            if (flag==0&&s[i] != '0')
			{
                flag=1;
            }

            if (flag){
                cout<<s[i];
            }
        }
        cout<<endl;
        cas++;
    }
  	return 0;
}

