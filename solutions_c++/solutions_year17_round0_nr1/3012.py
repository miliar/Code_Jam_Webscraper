#include <bits/stdc++.h>

using namespace std;

int changeposition(string &st, int position, int K)
{
	int len = st.size(),s=0;
	for(int i = position; i < len-K+1 ;)
	    {
	        for(int j = i; j < K+i; j++)
	        {
	            if(st[j] == '+')
	            	st[j] = '-';
	            else
	            	st[j] = '+';
	        }
	        for(int j = i+1 ; j < len ; j++)
	        {
	            if(st[j] == '-')
	            {
	                position = j;
	                break;
	            }
	        }
	        s++;
	        if(position == i)
	        	break;
	        i = position;
	    }
	    return s;
}
int main()
{
	int t,Case= 1;
	scanf("%d",&t);
	while(t--)
	{
	    string st;
	    cin >> st;
	    int K,i,len;
	    scanf("%d", &K);
	    printf("Case #%d: ",Case);Case++;
	    len = st.size();
	    int position = len;
	    for(int i=0 ; i < len ; i++)
	    {
	        if(st[i] == '-')
	        {
	            position = i;
	            break;
	        }
	    }
	    int s = changeposition(st,position,K),f;f=1;
	    for(int i = 0;i < len; i++)
	    {
	        if(st[i] == '-')
	        {   f=0;break;}
	    }
	    if(f)
	    	printf("%d\n",s);
	    else
	    	printf("IMPOSSIBLE\n");
	}
	
	return 0;
}