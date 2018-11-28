#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <set>
#include <algorithm>
#include <string>
#include <queue>
#include <climits>
#include <map>
#include <bitset>
using namespace std;

int main() {
	int t,i,l,k,counter=1;
	scanf("%d",&t);
	while(t--)
	{
	    string s;
	    cin >> s;
	    l=s.size();
	    cin >> k;
	    printf("Case #%d: ",counter);
	    counter++;
	    int pos=l,flag=1,ans=0,j;
	    for(i=0;i<l;i++)
	    {
	        if(s[i]=='-')
	        {
	            pos=i;
	            break;
	        }
	    }
	   // cout << pos;
	    for(i=pos;i<l-k+1;)
	    {
	        for(j=i;j<k+i;j++)
	        {
	            if(s[j]=='+')
	            s[j]='-';
	            else
	            s[j]='+';
	        }
	        for(j=i+1;j<l;j++)
	        {
	            if(s[j]=='-')
	            {
	                pos=j;
	                break;
	            }
	        }
	        //cout << pos << endl;
	        ans+=1;
	        if(pos==i)break;
	        i=pos;
	        
	        //i=pos;
	    }
	    for(i=0;i<l;i++)
	    {
	        if(s[i]=='-')
	        {
	            flag=0;
	            break;
	        }
	    }
	    if(flag)
	    printf("%d\n",ans);
	    else
	    printf("IMPOSSIBLE\n");
	}
	
	return 0;
}
