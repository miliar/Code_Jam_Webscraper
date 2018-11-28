#include <bits/stdc++.h>
#define lli long long int
#define pb push_back
#define mp make_pair
#define cases lli testcases;cin>>testcases; while(testcases--)
#define down '-'
#define up '+'
using namespace std;
char flip(char s)
{
    if(s==up)return down;
    else return up;
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int k,i,j;int cnt,impos,t;cin>>t;
	for(int testcase=1;testcase<=t;testcase++)
	{
	   string s;//    ---+-++-
	   cin>>s>>k;
	   int len=s.length();
	   // 3
	   
	    cnt=0;impos=0;
	   for(i=0;i<len;i++)
	   {
	    if(s[i]==up)continue;
		//DOWN
		if(i+k>len){impos=1;break;}
		cnt++;
		for(j=i;j<i+k;j++)
		{
		 s[j]=flip(s[j]);
		}
	   }
	   if(impos==1){cout<<"Case #"<<testcase<<": "<<"IMPOSSIBLE\n";}
	   else{cout<<"Case #"<<testcase<<": "<<cnt<<endl;}
	}//end of cases
    return 0;
}