#include "iostream"
#include "cstdio"
#include "cstring"
#include "vector"
#include "algorithm"
#include "queue"
using namespace std;
string s;
int main()
{
	freopen("A-large.in.txt", "r", stdin);  
    freopen("out.txt", "w", stdout);
    int t; 
    scanf("%d",&t);
    for(int cas=1;cas<=t;cas++)
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
        	printf("Case #%d: %d\n",cas,ans);
        else
        	printf("Case #%d: IMPOSSIBLE\n",cas);
    }
    return 0;
}
