#include <stdio.h>
#include<bits/stdc++.h>using namespace std;
int main(void) {
    freopen("input3.txt","r",stdin);
	 freopen("output3.txt","w",stdout);
    char str[1001]; int i,l,j,k,lc,test,u,y;
	scanf("%d",&test);
	for(u=0;u<=test-1;u++)
	{
	scanf("%s",&str);
    scanf("%d",&k);
    l=strlen(str);
    lc=0;
	for(i=0;i<=l-k;i++)
	{
	    if(str[i]=='+')
	    {
	        continue;
	    }
	    else if(str[i]=='-')
	    {
	        for(j=i;j<=i+k-1;j++)
	        {
	            if(str[j]=='+')
	            str[j]='-';
	            else if(str[j]=='-')
	            str[j]='+';
	        }
	        //	for(y=0;y<=l-1;y++)
//	printf("%c",str[y]);
//	printf("\n");
	        lc++;

	    }

	}
	for(i=0;i<=l-1;i++)
	{
	    if(str[i]=='-')
	    {  printf("Case #%d: ",u+1);
	        printf("IMPOSSIBLE\n");
	        goto end;
	    }
	}

	printf("Case #%d: ",u+1);
	printf("%d\n",lc);

	    end: continue;
	}
	return 0;
}

