#include<bits/stdc++.h>
using namespace std;
int main(){

    int t,n,i,j,ans,k,p,h,tmp;
    bool flag,flag2;
    string str;
    scanf("%d",&t);
    for(p=1 ; p<=t ;p++){
		cin>>str;
		scanf("%d",&k);
		n = str.length();
		i=0;
		while(i < n && str[i] == '+')
			i++;
		ans = 0;
		while(i < n){

			if(i+k-1 > n-1){
				j = i;					//>n
				while(j < n && str[j] != '+'){
					ans = -1;
					break;
					j++;
				}
				break;
			}
			else if(i+k-1 == n-1){              //n
				if(str[i] == '-'){
					for(j=i+1 ;j < n ;j++){
						if(str[j] != '-'){
							ans = -1;
							break;
						}
					}
					if(j == n)
						ans++;
				}
				else{
					for(j=i ; j < n ; j++){
						if(str[j] != '+'){
							ans = -1;
							break;
						}
					}
				}
				break;
			}
			else{                              //<n
 				ans++;
				flag = false;
				for(j=i ; j<=i+k-1 ; j++){
					str[j] = (str[j] == '+')? '-' : '+';
					if(!flag && str[j] == '-'){
						tmp = j;
						flag = true;
					}
				}
				if(flag)
					i = tmp;
				else
					i = i+k;
			}

			while( i < n && str[i] == '+')
				i++;
		}

		if(ans == -1){
			printf("Case #%d: IMPOSSIBLE\n",p);
		}
		else
			printf("Case #%d: %d\n",p,ans);

    }
    return 0;
}
