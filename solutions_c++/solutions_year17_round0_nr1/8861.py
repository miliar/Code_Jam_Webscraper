#include<bits/stdc++.h>
using namespace std;

int  main()
{
	int t,t1,k;
	char s[1000];
	cin>>t1;
	for(int t=1;t<=t1;t++){
		cin>>s>>k;
		int cnt=0;
		
		for(int i=strlen(s)-1;i>=k-1;i--){
		
			if(s[i]=='-')
			{
				int flip=k;
				for(int j=i;;j--){
					
					if(flip==0)
						break;
					else{
						if(s[j]=='-')
							s[j]='+';
						else if(s[j]=='+')
							s[j]='-';
					}
				flip--;
				}
			cnt++;
			
			}
	    }
	    int flag=0;
	    
	    for(int i=0;i<strlen(s);i++)
	    	if(s[i]=='-'){
	    		flag=1;break;}
	    	
	    if(flag==0)
	    printf("Case #%d: %d\n",t,cnt);
		else  printf("Case #%d: IMPOSSIBLE\n",t);
	}
return 0;
}
