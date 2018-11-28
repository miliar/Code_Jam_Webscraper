//Mitesh Agrawal
#include <bits/stdc++.h>
using namespace std;

#define ii pair<int,int>
#define ff first
#define ss second

ii at[5];
ii bt[5];

int main(){
	freopen ("B-small-attempt3.in","r",stdin); 
	freopen ("output.out","w",stdout); 
	int i,j,test,t,ans,a,b;
	scanf("%d",&t);
	for(test = 1; test <= t; test++){
		scanf("%d %d",&a,&b);
		for(i=0;i<a;i++)
			scanf("%d %d",&at[i].ff,&at[i].ss);
		sort(at,at+a);
		for(i=0;i<b;i++)
			scanf("%d %d",&bt[i].ff,&bt[i].ss);
		sort(bt,bt+b);
		if(a+b==1 || (a==1 && b==1))
			ans = 2;
		else if(a==2){
			if((1440 - at[1].ss + at[0].ff) < 720 && at[1].ff - at[0].ss < 720) ans = 4;
			else ans = 2;
		}
		else if(b==2){
			if((1440 - bt[1].ss + bt[0].ff) < 720 && bt[1].ff - bt[0].ss < 720) ans = 4;
			else ans = 2;
		}
		printf("Case #%d: %d\n",test,ans);
	}
    
    return 0;
}