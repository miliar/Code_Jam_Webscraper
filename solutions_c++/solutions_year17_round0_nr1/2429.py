#include<iostream> 
#include<cstdio>
#include<cstring>
#include<vector>
#include<algorithm>
#include<queue>
#define clr(x) memset(x,0,sizeof(x))
using namespace std;
string s;
int main()
{
	freopen("A-large.in", "r", stdin);  
    freopen("out.txt", "w", stdout);
    int kp; 
    scanf("%d",&kp);
    for(int kase=1;kase<=kp;kase++)
    {
        int k; 
        cin>>s;
        scanf("%d",&k);
        int len1= s.length();
        string str="";
        for(int i=0;i<len1;i++)
        {
        	if(s[i]=='-')
        	 str+='1';
        	else
        	 str+='0';
        }
        int len=str.length();
        queue<int> Q;
        bool flag = true;
        int ans = 0, top = 0;
        for(int i = 0; i < len; i++)
        {
            if(!Q.empty() && Q.front() < i)
                Q.pop();
            int op = str[i] - '0' + Q.size();
            if(op & 1)
            {
                ans++;
                if(i + k - 1 >= len)
                {
                    flag = false;
                    break;
                }
                Q.push(i+k-1);
            }
        }
        if(flag)
        	printf("Case #%d: %d\n",kase,ans);
        else
        	printf("Case #%d: IMPOSSIBLE\n",kase);
    }
    return 0;
}
