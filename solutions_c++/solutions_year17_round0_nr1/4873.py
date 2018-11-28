	#include <iostream>
	#include <cstdio>
	using namespace std;
	int array[10001];
	int Problem(int cant,int k){
		int ind=0,cont=0,ans=0;
		while(ind<=(cant-k)){
			while((ind<cant) && (array[ind]==1)) ind++;
			if (ind<=(cant-k)) ans++;
			else break;
			
			cont=ind;
			int flag=0;
			
			for(int i=cont;i<cont+k;i++){
				array[i]=!array[i];
				if (flag==0){
					if(!array[i]) flag++;
					else ind++;
				}
			}
			//for(int i=0;i<cant;i++) printf("%d",array[i]);
			//printf("\n");
			
		}
		for(int i=cant-k;i<cant;i++){
			if(!array[i]) return -1;
		}
		return ans;
	}	
	int main() {
		int t,k,cant;
		char c;
		scanf("%d\n",&t);
		for(int i=1;i<=t;i++){
			cant=0;
			while((c=getchar())!=' '){
				if(c=='+') array[cant++]=1;
				else array[cant++]=0;
			}
			scanf("%d\n",&k);
			int ans=Problem(cant,k);
			if(ans!=-1)
				printf("Case #%d: %d\n",i,ans);
			else
				printf("Case #%d: IMPOSSIBLE\n",i);
			
		}
		return 0;
	}