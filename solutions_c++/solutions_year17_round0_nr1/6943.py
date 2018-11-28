#include<bits/stdc++.h>
using namespace std;

int  main()
{
	int t,t1,k;
//	freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	string s;
	scanf("%d",&t1);
	for(int t=1;t<=t1;t++){
		cin>>s>>k;
		int cnt=0;
		
		for(int i=0;i<=s.length()-k;i++){
		
			if(s[i]=='-')
			{
				int flip=k;
				
				for(int j=i;;j++){
					
					if(!flip)
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
	    
	    for(int i=s.length()-1;i>=0;i--){
	    
	    	if(s[i]=='-'){
	    		flag=1;
	    		break;
	    	}
	    }
	    (flag==0)?printf("Case #%d: %d\n",t,cnt):printf("Case #%d: IMPOSSIBLE\n",t);
	    
	}
return 0;
}

